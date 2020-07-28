from django.urls import path
from .views import (
                    doctor_dashboard, 
                    patients_home,
                    specimen_home,
                    send_specimen,
                    specimen_details,
                    # delete_patient,
                    # tests_home,
                    )


app_name = 'doctor'

urlpatterns = [
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('<int:id>/patients_home/', patients_home, name='patients_home'),
    path('<int:id>/specimen_home/', specimen_home, name='specimen_home'),
    path('specimen_home/<int:id>/send_specimen/', send_specimen, name='send_specimen'),
    path('specimen_home/<int:id>/specimen_details/', specimen_details, name='specimen_details'),
    # path('<int:id>/tests_home/', tests_home, name='tests_home'),

]
 