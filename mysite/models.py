from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notifications(models.Model):
    Date = models.DateTimeField()
    content = models.CharField(max_length=600)
    topic = models.CharField(max_length=150)
    picture = models.CharField(null=True,blank=True,max_length=200)
