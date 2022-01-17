from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime as dt
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls,username):
        return cls.objects.fiter(user__username__icontains = username).all()

class Vitals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vitals")
    temperature = models.CharField(max_length = 10,blank =True)
    pulserate = models.CharField(max_length = 10,blank =True)
    bloodpressure = models.CharField(max_length = 10,blank =True)
    symptoms = models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save_vitals(self):
        self.save()