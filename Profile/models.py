from django.db import models

from django.contrib.auth.models import User 
 
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name
    
     
    