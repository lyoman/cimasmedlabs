from django.urls import path
from .views import (
                    pathologist_dashboard, 
           
                    )


app_name = 'Lab_Pathologist'

urlpatterns = [
    path('pathologist_dashboard/', pathologist_dashboard, name='pathologist_dashboard'),

]
 