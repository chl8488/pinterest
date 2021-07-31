from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribe'
urlpatterns = [
    path('subscribe/',SubscriptionView.as_view(),name='subscribe'),
]