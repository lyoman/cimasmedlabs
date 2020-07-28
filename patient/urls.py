from django.urls import path
from .views import (
                    patient_dashboard, 
                    add_specimen,
                    edit_specimen,
                    delete_specimen,
                    specimen_home,
                    send_specimen,
                    )


app_name = 'patient'

urlpatterns = [
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('<int:id>/view_specimen/', specimen_home, name='specimen_home'),
    path('<int:id>/view_specimen/add_specimen/', add_specimen, name='add_specimen'),
    path('view_specimen/<int:id>/edit_specimen/', edit_specimen, name='edit_specimen'),
    path('view_specimen/<int:id>/delete_specimen/', delete_specimen, name='delete_specimen'),
    path('view_specimen/<int:id>/send_specimen/', send_specimen, name='send_specimen'),

]
 