from django.contrib import admin
from .models import WebScrapingData
# Register your models here.
@admin.register(WebScrapingData)
class WebScrapingDataAdmin(admin.ModelAdmin):
    pass