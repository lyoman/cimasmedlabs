from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,ReadOnlyPasswordHashField
from .models import (
    User,
)

class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email', 'gender', "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_active = True
        if commit:
            user.save()
        return user