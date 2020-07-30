from django.urls import path
from .views import (
                    doctor_dashboard, 
                    patients_home,
                    specimen_home,
                    dsamples_home,
                    specimen_details,
                    report_home,
                    report_details,
                    )


app_name = 'doctor'

urlpatterns = [
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('<int:id>/patients_home/', patients_home, name='patients_home'),
    path('<int:id>/specimen_home/', specimen_home, name='specimen_home'),
    path('specimen_home/<int:id>/specimen_details/', specimen_details, name='specimen_details'),
    path('<int:id>/samples_home/', dsamples_home, name='dsamples_home'),
    path('<int:id>/report_home/', report_home, name='report_home'),
    path('report_home/<int:id>/report_details/', report_details, name='report_details'),
]
 