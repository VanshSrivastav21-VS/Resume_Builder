from django.db import models
from django.contrib.auth.models import User

class contactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField()