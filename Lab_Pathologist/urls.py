from django.urls import path
from .views import (
                    pathologist_dashboard, 
                    patients_home,
                    delete_patient,
                    tests_home,
                    specimen_home,
                    perform_test,
                    )


app_name = 'Lab_Pathologist'

urlpatterns = [
    path('pathologist_dashboard/', pathologist_dashboard, name='pathologist_dashboard'),
    path('<int:id>/patients_home/', patients_home, name='patients_home'),
    path('patient_home/<int:id>/delete_patient/', delete_patient, name='delete_patient'),
    path('<int:id>/tests_home/', tests_home, name='tests_home'),
    path('<int:id>/specimen_home/', specimen_home, name='specimen_home'),
    path('specimen_home/<int:id>/perform_test', perform_test, name='perform_test'),
]
 