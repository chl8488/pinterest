from django.urls import path

from ProfileApp.views import ProfileCreateView

app_name = 'profileapp'
urlpatterns = [
    path('create/',ProfileCreateView.as_view(),name='create'),
]