from django.urls import path

from apps.job.views import add_job, apply_for_job, edit_job, job_detail, search
from apps.job.api import api_search

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('search', search, name='search'),
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('<int:job_id>/edit/', edit_job, name='edit_job'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job'),
]
