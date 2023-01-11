from django.urls import path

from apps.userprofile.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
