from django.urls import path

from Likeapp.views import LikeArticleView

app_name = 'likeapp'
urlpatterns = [
    path('article/likes/<int:pk>', LikeArticleView.as_view(), name='article_like'),
]