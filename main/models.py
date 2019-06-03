from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from enum import Enum

class Messages(models.Model):

    firstname = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=200,default='')
    message = models.CharField(max_length=1000)
    def __str__(self): #method allows us to return ojects with question text and other texts unlike returning objects as objects
        return self.firstname[0:1].capitalize()+self.firstname[1:len(self.firstname)].lower() +' '+ self.lastname[0:1].capitalize()+self.lastname[1:len(self.lastname)].lower()

# Create your models here.
