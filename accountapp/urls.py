from django.urls import path
from .views import hello_world

app_name= 'accountapp'
urlpatterns = [
    path('hello_word/', hello_world, name='hello_word')
]