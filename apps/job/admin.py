from django.contrib import admin

from apps.job.models import Application, Job

admin.site.register(Job)
admin.site.register(Application)