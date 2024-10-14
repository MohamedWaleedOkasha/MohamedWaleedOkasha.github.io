# from django.shortcuts import render
# from .models import Article

# def article_list(request):
#     articles = Article.objects.all()
#     return render(request, 'content/article_list.html', {'articles': articles})
# from django.shortcuts import render, get_object_or_404
# from .models import Article

# def article_list(request):
#     articles = Article.objects.all()
#     return render(request, 'content/article_list.html', {'articles': articles})

# def article_detail(request, id):
#     article = get_object_or_404(Article, id=id)
#     return render(request, 'content/article_detail.html', {'article': article})
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
