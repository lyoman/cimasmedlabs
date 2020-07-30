from django import forms
from django.utils.translation import gettext as _
from .models import GeneratedReport

class ReportDataForm(forms.ModelForm):

    class Meta:
        model = GeneratedReport
        fields = ["specimendata", "test_name", "hemoglobin", "RBC", "weight_result"]
