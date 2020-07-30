from django.contrib import admin
from .models import GeneratedReport

class GeneratedReportModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "user", "reffnumber", "specimendata", "test_name", "hemoglobin", "RBC", "updated", "timestamp"]
    list_display_links  = ["updated", "specimendata"]
    list_editable		= ["hemoglobin", "RBC"]
    list_filter			= ["reffnumber", "user", "test_name"]
    search_fields		= ["reffnumber"]
    class Meta:
        model = GeneratedReport

admin.site.register(GeneratedReport, GeneratedReportModelAdmin)