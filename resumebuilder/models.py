from django.db import models
from django.contrib.auth.models import User

class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resume_templates/')

    def __str__(self):
        return self.name
    

    