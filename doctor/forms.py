from django import forms
from django.utils.translation import gettext as _
from .models import SpecimenData

class SpecimenDataForm(forms.ModelForm):

    class Meta:
        model = SpecimenData
        fields = ["temperature", "weight"]
