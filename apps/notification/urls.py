from django.urls import path, include

from apps.notification.views import notifications

urlpatterns = [
    path('', notifications, name='notifications'),
]
