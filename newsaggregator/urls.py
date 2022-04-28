from django.urls import path
from .views import *
urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("news/<int:pk>", NewsDetailView.as_view(), name="news_detail"),
]
