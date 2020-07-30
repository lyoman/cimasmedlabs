from django.contrib import admin
from .models import Specimen

# Register your models here.
class SpecimenModelAdmin(admin.ModelAdmin):
    exclude             = ('user', "updated")
    list_display 	    = ["id", "user", "age", "patient_name", "email",  "gender", "status", "updated", "timestamp"]
    list_display_links  = ["updated", "patient_name"]
    # list_editable		= []
    list_filter			= ["email", "age", "gender", "updated", "timestamp"]
    search_fields		= ["patient_name", "email", "gender"]
    class Meta:
        model = Specimen
  
admin.site.register(Specimen, SpecimenModelAdmin)