from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.job.models import Application, Job
from apps.userprofile.models import ConversationMessage

@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
        
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            coversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)
            return redirect('view_application', application_id=application_id)
        
    return render(request, 'userprofile/view_application.html', {'application': application})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    return render(request, 'userprofile/view_dashboard_job.html', {'job': job})