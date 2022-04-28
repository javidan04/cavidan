from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WebScrapingData
# Create your views here.

class IndexPage(ListView):
    queryset = WebScrapingData.objects.all()
    template_name = "newsaggregator/index.html"
    paginate_by = 12
    context_object_name = "all_news"


    def get_queryset(self):
        return self.queryset.filter(date_time__isnull=False).order_by("-date_time")


class NewsDetailView(DetailView):
    queryset = WebScrapingData.objects.all()
    template_name = "newsaggregator/news_detail.html"
    context_object_name = "news"