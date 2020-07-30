from django.urls import path
from .views import (
                    patient_dashboard, 
                    add_specimen,
                    edit_specimen,
                    delete_specimen,
                    specimen_home,
                    send_specimen,
                    doctor_home,
                    doctors_details,
                    report_home,
                    report_details,
                    )


app_name = 'patient'

urlpatterns = [
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('<int:id>/view_specimen/', specimen_home, name='specimen_home'),
    path('<int:id>/view_specimen/add_specimen/', add_specimen, name='add_specimen'),
    path('view_specimen/<int:id>/edit_specimen/', edit_specimen, name='edit_specimen'),
    path('view_specimen/<int:id>/delete_specimen/', delete_specimen, name='delete_specimen'),
    path('view_specimen/<int:id>/send_specimen/', send_specimen, name='send_specimen'),
    path('<int:id>/doctors_home/', doctor_home, name='doctor_home'),
    path('doctors_home/<int:id>/doctor_details/', doctors_details, name='doctors_details'),
    path('<int:id>/report_home/', report_home, name='report_home'),
    path('report_home/<int:id>/report_details/', report_details, name='report_details'),

]
 