from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WebScrapingData
from django.db.models import Q
# Create your views here.
from .similarity import find_similarity


class IndexPage(ListView):
    queryset = WebScrapingData.objects.all()
    template_name = "newsaggregator/index.html"
    paginate_by = 12
    context_object_name = "all_news"


    def get_queryset(self):
        return self.queryset.filter(date_time__isnull=False).exclude(
            Q(link__contains="report.az") |
            Q(link__contains="azxeber.com")
        ).order_by("-date_time")


class NewsDetailView(DetailView):
    queryset = WebScrapingData.objects.all()
    template_name = "newsaggregator/news_detail.html"
    context_object_name = "news"


    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context["similar"] = 12
        news = WebScrapingData.objects.get(pk=pk)
        all_news = WebScrapingData.objects. \
            filter(date_time__day=news.date_time.day, date_time__month=news.date_time.month). \
            exclude(pk=pk).exclude(
            Q(link__contains="report.az") |
            Q(link__contains="azxeber.com"))
        all_news_in_list = []
        all_ids_in_list = []
        for n in all_news:
            all_news_in_list.append(n.content)
            all_ids_in_list.append(n.id)

        result = find_similarity(news.content, all_news_in_list, all_ids_in_list)
        result = result[result['cos_similarities']>=0.2]
        col_ids_list = result['ids'].tolist()

        similar_news = WebScrapingData.objects.filter(pk__in=col_ids_list)
        context["similar_news"] = similar_news
        return context