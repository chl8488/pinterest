from django.urls import path

from boardapp.views import *

app_name= 'board'
urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
]