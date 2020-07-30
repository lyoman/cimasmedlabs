from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import Specimen
from .forms import SpecimenForm, SpecimenDataForm
from django.contrib.auth.decorators import login_required
from doctor.models import SpecimenData, Doctor
from Lab_Pathologist.models import GeneratedReport

from datetime import datetime

from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

# Create your views here. 
@login_required
def patient_dashboard(request):
    username = request.user.username
    id       = request.user.id
    patient  = User.objects.filter(id=id, is_patient = True)
    print(patient)

    context = {
        'patient': patient, 
        'username':username,
    }
    return render(request,'patient/view.html', context)


@login_required
def specimen_home(request,id):
    specimen   = Specimen.objects.filter(user=id)
    # specimen   = Specimen.objects.all() 
    patient    = get_object_or_404(User, pk=id)
    username   = request.user.username

    context     = {
        "specimen"  : specimen,
        "patient"   : patient,
        "username"  : username,
    }
    return render(request, 'patient/specimen.html', context)

@login_required
def add_specimen(request, id):
    form     = SpecimenForm(request.POST or None, request.FILES or None)
    username = request.user.username
    patient  = get_object_or_404(User, pk=id)

    if form.is_valid():
        specimen = form.save(commit=False)
        specimen.user = request.user
        specimen.save()
        messages.success(request, specimen.specimen_name + " has been successfully added !!!")
        return redirect('patient:specimen_home', patient.id)
    context = {
        'username': username,
        "form": form,
        'patient': patient,
        'header': 'Add a New Specimen',
        'save': 'Save',
        'title': 'Add Specimen',
    }
    return render(request, 'patient/add_specimen.html', context)


@login_required
def edit_specimen(request, id, template_name='patient/add_specimen.html'):
    specimen = get_object_or_404(Specimen, pk=id)
    patient  = specimen.user
    username = request.user.username

    form = SpecimenForm(request.POST or None, instance=specimen)
    if form.is_valid():
        update_specimen = form.save(commit=False)
        update_specimen.save()
        print(update_specimen)
        messages.success(request, update_specimen.specimen_name + " has been successfully Updated !!!")
        return redirect('patient:specimen_home', patient.id)

    context = { 'form':form, 
                'username':username,
                'patient':patient,
                'header': 'Update Specimen',
                'save': 'Update',
                'title': 'Edit Specimen',
            }
    return render(request, template_name, context)


@login_required
def delete_specimen(request, id):
    specimen = get_object_or_404(Specimen, pk=id)
    print(specimen)
    patient  = specimen.user
    username = request.user.username

    specimen.delete()
    messages.info(request, specimen.specimen_name + "Specimen has been successfully deleted !!!")
    return redirect('patient:specimen_home', patient.id)

@login_required
def send_specimen(request, id):
    # dt = datetime.now()
    # milliseconds = int(round(dt.timestamp() *1000))
    # print(milliseconds)
    form     = SpecimenDataForm(request.POST or None, request.FILES or None)
    username = request.user.username
    specimen = get_object_or_404(Specimen, pk=id)
    patient  = specimen.user
    doctor   = User.objects.filter(is_doctor = True)
    print(doctor[0].id)
    doctor   = doctor[0]

    # if form.is_valid():
    specimendata = form.save(commit=False)
    specimendata.patient  = patient
    specimendata.doctor   = doctor
    specimendata.specimen = specimen
    specimendata.save()
    specimen.status = 'sent'
    specimen.save()
    messages.success(request,"Specimen has been successfully sent to the Doctor !!!")
    return redirect('patient:specimen_home', patient.id)

@login_required
def doctor_home(request,id):
    patient    = get_object_or_404(User, pk=id)
    doctors    = Doctor.objects.all()
    username   = request.user.username

    context     = {
        "patient"    : patient,
        "doctors"    : doctors,
        "username"   : username,
    }
    return render(request,'padoctors/view.html', context)


@login_required
def doctors_details(request, id):
    docdata     = get_object_or_404(Doctor, pk=id)
    username    = request.user.username
    patient     = request.user
    print(patient)

    context     = {
        "patient"      : patient,
        "docdata"      : docdata,
        "username"     : username,
    }
    return render(request,'padoctors/doctor_details.html', context)

@login_required
def report_home(request, id):
    specimendata    = SpecimenData.objects.filter(patient=request.user)
    specimendata    = specimendata[0]
    print(specimendata)
    reportdata      = GeneratedReport.objects.filter(specimendata=specimendata)
    username        = request.user.username
    patient         = get_object_or_404(User, pk=id)
    print(reportdata)
    context     = {
        "reportdata"    : reportdata,
        "username"      : username,
        "patient"       : patient,
    }
    return render(request,'preport/view.html', context)


@login_required
def report_details(request, id):
    reportdata      = get_object_or_404(GeneratedReport, pk=id)
    username        = request.user.username
    patient         = request.user
    print(reportdata)

    context     = {
        "reportdata"    : reportdata,
        "username"      : username,
        "patient"       : patient,
    }
    return render(request,'preport/preport_details.html', context)