from django.db import models

# Create your models here.
class Profile(models.Model):
    name  = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    previous_work =models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name