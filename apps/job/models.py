from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    
    SIZE_1_9 = 'size_1-9'
    SIZE_10_49 = 'size_1-49'
    SIZE_50_99 = 'size_50-99'
    SIZE_100 = 'size_100'
    
    CHOICES_SIZE = (
        (SIZE_1_9, '1-9'),
        (SIZE_10_49, '10-49'),
        (SIZE_50_99, '50-99'),
        (SIZE_100, '100+')
    )
    
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_zipcode = models.CharField(max_length=255, blank=True, null=True)
    company_place = models.CharField(max_length=255, blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=255, choices=CHOICES_SIZE, default=SIZE_1_9)
    
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    
    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)