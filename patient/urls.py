from django.urls import path
from .views import (
                    patient_dashboard, 
           
                    )


app_name = 'patient'

urlpatterns = [
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),

]
 