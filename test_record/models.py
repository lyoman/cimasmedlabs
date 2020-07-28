from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import Permission, User
from users.models import User
from doctor.models import Doctor

# import time
from datetime import datetime

dt = datetime.now()
milliseconds = int(round(dt.timestamp()))
# print(milliseconds)


izvezvi = timezone.now()
# Create your models here.
class RegisterPatient(models.Model):
    user          = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    doctor        = models.ForeignKey(Doctor, default=1, on_delete = models.CASCADE)
    patient_name  = models.CharField(max_length=200)
    email         = models.CharField(max_length=200)
    age           = models.CharField(max_length=200, blank=False)
    gender        = models.CharField(max_length=200, null=False, blank=False)
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)
    refference    = models.CharField(max_length=200, blank=False, default = milliseconds)
    # status        = models.CharField(max_length=200, default = "pending")


    def __str__(self):
        return self.patient_name

    class Meta:
        ordering = ["-timestamp", "-updated"]
