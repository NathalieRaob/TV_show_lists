from django.db import models
from datetime import datetime


# Create your models here.


class TV_showManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Shows title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors['network'] = 'Shows network should be at least 2 characters'
        if postData['description']!= '' and len(postData['description']) < 10:
            errors['description'] = 'Shows description should be at least 10 characters'
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Daet should be in the past'
        return errors 
        
        
class TV_show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 70)
    release_date = models.DateTimeField()
    release_date = models.DateTimeField()
    description = models.TextField(max_length = 255, default = 'anything')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TV_showManager()