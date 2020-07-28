from django.db import models

from django.db import models
from users.models import User

# Create your models here.
class Specimen(models.Model):
    user          = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    patient_name  = models.CharField(max_length=200, blank=False)
    email         = models.CharField(max_length=200, blank=False)
    specimen_name = models.CharField(max_length=200, blank=False)
    hemoglobin    = models.CharField(max_length=200, blank=False)
    RBC           = models.CharField(max_length=200, null=False, blank=False)
    gender        = models.CharField(max_length=200, blank=False)
    age           = models.CharField(max_length=200, blank=False)
    status        = models.CharField(max_length=200, blank=False, default="available")
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.patient_name

    class Meta:
        ordering = ["-timestamp", "-updated"]