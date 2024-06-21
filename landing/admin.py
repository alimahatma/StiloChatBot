from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis','publish_date')
    search_fields = ('judul', 'penulis')
    list_filter = ['publish_date']
    
    
admin.site.register(Article, ArticleAdmin)