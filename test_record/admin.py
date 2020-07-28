from django.contrib import admin
from .models import RegisterPatient

# Register your models here.
class RegisterPatientModelAdmin(admin.ModelAdmin):
    exclude             = ('user', 'refference')
    list_display 	    = ["refference", "user", "doctor", "age", "patient_name", 'email',  "gender", "updated", "timestamp"]
    list_display_links  = ["updated", "patient_name"]
    list_editable		= ["refference"]
    list_filter			= ["email", "age", "gender", "updated", "timestamp"]
    search_fields		= ["patient", "email"]
    class Meta:
        model = RegisterPatient

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.refference = obj.timestamp
    #     obj.save()
  
admin.site.register(RegisterPatient, RegisterPatientModelAdmin)
