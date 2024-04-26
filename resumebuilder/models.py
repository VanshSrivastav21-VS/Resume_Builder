from django.db import models
from django.contrib.auth.models import User

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resume_templates/')

    def __str__(self):
        return self.name
    

    