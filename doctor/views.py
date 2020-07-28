from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required
from .models import SpecimenData


from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

# Create your views here. 
@login_required
def doctor_dashboard(request):
    username = request.user.username
    id       = request.user.id
    doctor = User.objects.filter(id=id, is_doctor = True)
    print(doctor)

    context = {
        'doctor': doctor, 
        'username':username,
    }
    return render(request,'doctor/view.html', context)


@login_required
def patients_home(request,id):
    doctor      = get_object_or_404(User, pk=id)
    patients    = User.objects.filter(is_patient=True)
    username    = request.user.username

    context     = {
        "doctor"     : doctor,
        "patients"   : patients,
        "username"   : username,
    }
    return render(request,'patients/view.html', context)


@login_required
def specimen_home(request, id):
    specimendata    = SpecimenData.objects.filter(doctor=request.user)
    username        = request.user.username
    doctor          = get_object_or_404(User, pk=id)

    context     = {
        "specimendata"  : specimendata,
        "username"      : username,
        "doctor"        : doctor,
    }
    return render(request,'patients/specimen.html', context)


@login_required
def specimen_details(request, id):
    specimendata    = get_object_or_404(SpecimenData, pk=id)
    username        = request.user.username
    doctor          = specimendata.doctor
    print(specimendata)

    context     = {
        "specimendata"  : specimendata,
        "username"      : username,
        "doctor"        : doctor,
    }
    return render(request,'patients/specimen_details.html', context)


@login_required
def send_specimen(request, id):
    specimen = get_object_or_404(SpecimenData, pk=id)
    print(specimen)
    doctor  = specimen.doctor
    username = request.user.username
    specimen.pathologist = 'yes'
    specimen.save()
    messages.info(request, "Specimen has been successfully sent to the Pathologist !!!")
    return redirect('doctor:specimen_home', doctor.id)