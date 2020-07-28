from django.contrib import admin
from .models import Specimen

# Register your models here.
class SpecimenModelAdmin(admin.ModelAdmin):
    exclude             = ('user', "updated")
    list_display 	    = ["id", "user", "specimen_name", "age", "patient_name", "email",  "gender", "hemoglobin", "RBC", "status", "updated", "timestamp"]
    list_display_links  = ["updated", "patient_name"]
    list_editable		= ["specimen_name"]
    list_filter			= ["email", "age", "gender", "updated", "RBC", "hemoglobin", "timestamp"]
    search_fields		= ["patient_name", "email", "specimen_name"]
    class Meta:
        model = Specimen
  
admin.site.register(Specimen, SpecimenModelAdmin)