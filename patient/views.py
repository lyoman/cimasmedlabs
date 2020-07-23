from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

# Create your views here. 
@login_required
def patient_dashboard(request):
    username = request.user.username
    patient = User.objects.filter(username=username, is_patient = True)
    # patient = patient.order_by('username')
    print(patient)

    context = {
        'patient': patient, 
        'username':username,
    }
    return render(request,'patient/view.html', context)