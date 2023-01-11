from django import forms

from apps.job.models import Application, Job

class AddJobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ("title", "short_description", "long_description",)
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("content", "experience",)
