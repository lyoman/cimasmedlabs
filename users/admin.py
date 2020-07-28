from django.contrib import admin
from .models import User

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "username", "email", 'gender',  "is_lab_pathologist", "is_doctor", "is_patient", "is_active", "is_staff", "is_superuser", "updated", "timestamp"]
    list_display_links  = ["updated", "username"]
    list_editable		= ["is_active"]
    list_filter			= ["is_lab_pathologist", "is_doctor", "is_patient", "is_staff", "is_superuser", "updated", "timestamp", "email"]
    search_fields		= ["username", "email"]
    class Meta:
        model = User
  
admin.site.register(User, UserModelAdmin)