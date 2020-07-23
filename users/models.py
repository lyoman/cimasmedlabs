from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_lab_pathologist  = models.BooleanField(default=False)
    is_doctor           = models.BooleanField(default=False)
    is_patient          = models.BooleanField(default=False)
    email               = models.EmailField(unique=True, blank=False)
    updated             = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp           = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
