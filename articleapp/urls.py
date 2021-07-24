from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreationView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ArticleListView

app_name = 'article'
urlpatterns = [
    path('list/',ArticleListView.as_view(),name='list'),
    path('create/', ArticleCreationView.as_view(),name='create'),
    path('detail/<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('update/<int:pk>',ArticleUpdateView.as_view(),name='update'),
    path('delte/<int:pk>',ArticleDeleteView.as_view(),name='delete'),
]
