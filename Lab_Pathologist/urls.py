from django.urls import path
from .views import (
                    pathologist_dashboard, 
                    ppatients_home,
                    delete_patient,
                    tests_home,
                    specimen_home,
                    specimen_home1,
                    perform_test,
                    reports_home,
                    generate_report,
                    reports_detail,
                    pdoctors_home,
                    pdoctors_details,
                    lab_home,
                    samples_home,
                    )


app_name = 'Lab_Pathologist'

urlpatterns = [
    path('pathologist_dashboard/', pathologist_dashboard, name='pathologist_dashboard'),
    path('<int:id>/ppatients_home/', ppatients_home, name='ppatients_home'),
    path('patient_home/<int:id>/delete_patient/', delete_patient, name='delete_patient'),
    path('<int:id>/tests_home/', tests_home, name='tests_home'),
    path('<int:id>/specimen_home/', specimen_home, name='specimen_home'),
    path('<int:id>/completed_tests/', specimen_home1, name='specimen_home1'),
    path('specimen_home/<int:id>/perform_test', perform_test, name='perform_test'),
    path('<int:id>/reports_home/', reports_home, name='reports_home'),
    path('reports_home/<int:id>/generate_report/', generate_report, name='generate_report'),
    path('reports_home/<int:id>/reports_detail/', reports_detail, name='reports_detail'),
    path('<int:id>/pdoctors_home/', pdoctors_home, name='pdoctors_home'),
    path('pdoctors_home/<int:id>/pdoctors_details/', pdoctors_details, name='pdoctors_details'),
    path('<int:id>/lab_home/', lab_home, name='lab_home'),
    path('<int:id>/samples_home/', samples_home, name='samples_home'),
]
 