from django.urls import path
from .views import home, article_detail, chatbot


urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
]