from django import forms
from django.utils.translation import gettext as _
from .models import (
    Specimen,
)
from doctor.models import SpecimenData

class SpecimenForm(forms.ModelForm):

    class Meta:
        model = Specimen
        exclude = ('user', 'status',)
        fields = '__all__'


class SpecimenDataForm(forms.ModelForm):

    class Meta:
        model   = SpecimenData
        # exclude = ('patient',)
        fields  = '__all__'