from django.db import models
from django.utils import timezone
from users.models import User
from doctor.models import SpecimenData
from patient.models import Specimen
from datetime import datetime

dt = datetime.now()
milliseconds = int(round(dt.timestamp() *1000))
# print(milliseconds)

class GeneratedReport(models.Model):
    user          = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    specimendata  = models.ForeignKey(SpecimenData, on_delete = models.CASCADE)
    reffnumber    = models.CharField(max_length=200, blank=False, default = milliseconds)
    test_name     = models.CharField(max_length=200, blank=False, default="Hematology Blood Test")
    hemoglobin    = models.CharField(max_length=200, blank=False, null=False,)
    RBC           = models.CharField(max_length=200, null=False, blank=False)
    weight_result = models.CharField(max_length=200, null=False, blank=False)
    updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.test_name

    class Meta:
        ordering = ["-timestamp", "-updated"]