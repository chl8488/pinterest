from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribe'
urlpatterns = [
    path('subscribe/',SubscriptionView.as_view(),name='subscribe'),
    path('list/',SubscriptionListView.as_view(),name='list'),
]