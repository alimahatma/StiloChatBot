from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'landing/home.html', {'articles':articles})

def chatbot(request):
    return render(request,'landing/chatbot.html')

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'landing/article_detail.html', {'article': article})
