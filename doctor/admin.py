from django.contrib import admin
from .models import Doctor, SpecimenData

# Register your models here.
class DoctorModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "user", "age", "doctor_name", 'email',  "gender", "qualification", "updated", "timestamp"]
    list_display_links  = ["updated", "doctor_name"]
    # list_editable		= []
    list_filter			= ["email", "age", "gender", "updated", "timestamp"]
    search_fields		= ["doctor_name", "email"]
    class Meta:
        model = Doctor

class SpecimenDataModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "reff", "patient", "doctor", "specimen", "temperature", "weight", "updated", "timestamp"]
    list_display_links  = ["updated", "doctor"]
    list_editable		= ["temperature", "weight"]
    list_filter			= ["patient"]
    search_fields		= ["reff"]
    class Meta:
        model = SpecimenData

admin.site.register(Doctor, DoctorModelAdmin)
admin.site.register(SpecimenData, SpecimenDataModelAdmin)