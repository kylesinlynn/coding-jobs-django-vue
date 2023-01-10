from django.shortcuts import render

from apps.job.models import Job

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job/job_detail.html', {'job': job})