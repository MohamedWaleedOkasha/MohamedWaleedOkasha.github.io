# from django.urls import path
# from .views import article_list

# urlpatterns = [
#     path('', article_list, name='article_list'),
# ]
from django.urls import path
from .views import ArticleListCreate, ArticleDetail

urlpatterns = [
    path('', ArticleListCreate.as_view(), name='article-list-create'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
]
