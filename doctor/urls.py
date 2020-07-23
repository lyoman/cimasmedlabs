from django.urls import path
from .views import (
                    doctor_dashboard, 
           
                    )


app_name = 'doctor'

urlpatterns = [
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),

]
 