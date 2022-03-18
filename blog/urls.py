from django.urls import path, include
from blog.views import article, detail_article

app_name = 'blog'

urlpatterns = [
    path('blog/', article, name = "article"),
    path('blog/article/<slug:slug_text>/', detail_article, name = "detail_article"),
]