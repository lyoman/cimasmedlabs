from django.db import models
from django.utils import timezone
from users.models import User
from patient.models import Specimen


from datetime import datetime

dt = datetime.now()
milliseconds = int(round(dt.timestamp() *1000))
print(milliseconds)

# Create your models here.
class Doctor(models.Model):
    user          = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    doctor_name   = models.CharField(max_length=200, blank=False)
    password      = models.CharField(max_length=200, blank=False)
    email         = models.CharField(max_length=200, blank=False)
    qualification = models.CharField(max_length=200, blank=False)
    age           = models.CharField(max_length=200, blank=False)
    gender        = models.CharField(max_length=200, null=False, blank=False)
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.doctor_name

    class Meta:
        ordering = ["-timestamp", "-updated"]


class SpecimenData(models.Model):
    patient       = models.ForeignKey(User, default=1, on_delete = models.CASCADE, related_name='patients')
    doctor        = models.ForeignKey(User, default=1, on_delete = models.CASCADE, related_name='doctors')
    specimen      = models.ForeignKey(Specimen, on_delete = models.CASCADE)
    reff          = models.CharField(max_length=200, blank=False, default = milliseconds)
    status        = models.CharField(max_length=200, blank=False, default="pending")
    pathologist   = models.CharField(max_length=200, blank=False, default = "no")
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)


    # def __str__(self):
    #     return self.reff

    class Meta:
        ordering = ["-timestamp", "-updated"]