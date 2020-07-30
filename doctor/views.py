from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required
from .models import SpecimenData
from Lab_Pathologist.models import GeneratedReport

from .forms import SpecimenDataForm

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
    # print(specimendata)
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
    form            = SpecimenDataForm(request.POST or None, request.FILES or None, instance=specimendata)
    if form.is_valid():
        specimen = form.save(commit=False)
        specimen.pathologist = 'yes'
        specimen.save()
        messages.success(request, "Specimen has been successfully sent to the Pathologist !!!")
        return redirect('doctor:specimen_home', doctor.id)
    context     = {
        "specimendata"  : specimendata,
        "username"      : username,
        "doctor"        : doctor,
        "form"          : form,
    }
    return render(request,'patients/specimen_details.html', context)


@login_required
def dsamples_home(request, id):
    username        = request.user.username
    doctor          = get_object_or_404(User, pk=id)

    context     = {
        "username"      : username,
        "doctor"        : doctor,
    }
    return render(request,'doctor/dsamples.html', context)


@login_required
def report_home(request, id):
    specimendata    = SpecimenData.objects.filter(doctor=request.user)
    specimendata    = specimendata[0]
    print(specimendata)
    reportdata      = GeneratedReport.objects.filter(specimendata=specimendata)
    username        = request.user.username
    doctor          = get_object_or_404(User, pk=id)
    print(reportdata)
    context     = {
        "reportdata"    : reportdata,
        "username"      : username,
        "doctor"        : doctor,
    }
    return render(request,'dreport/view.html', context)


@login_required
def report_details(request, id):
    reportdata      = get_object_or_404(GeneratedReport, pk=id)
    username        = request.user.username
    doctor          = request.user
    print(reportdata)

    context     = {
        "reportdata"    : reportdata,
        "username"      : username,
        "doctor"        : doctor,
    }
    return render(request,'dreport/dreport_details.html', context)
