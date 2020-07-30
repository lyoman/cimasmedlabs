from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required
from test_record.models import RegisterPatient
from doctor.models import SpecimenData, Doctor
from .models import GeneratedReport

from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

from .forms import ReportDataForm

import time
from datetime import datetime

# Create your views here. 
@login_required
def pathologist_dashboard(request):
    username    = request.user.username
    pathologist = User.objects.filter(username=username, is_lab_pathologist = True)
    # pathologist = pathologist.order_by('username')
    print(pathologist)

    context = {
        'pathologist': pathologist, 
        'username'   :username,
    }
    return render(request,'pathologist/view.html', context)


@login_required
def ppatients_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    patients    = User.objects.filter(is_patient=True)
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "patients"   : patients,
        "username"   : username,
    }
    return render(request,'ppatients/view.html', context)

@login_required
def delete_patient(request, id):
    patient = User.objects.get(pk=id)
    username = request.user.username
    pathologist = request.user
    patient.delete()
    messages.info(request, patient.username + " has been successfully deleted !!!")
    return redirect('pathologist:patients_home', {'pathologist': pathologist, 'username': username})

@login_required
def tests_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    tests       = RegisterPatient.objects.all()
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "tests"      : tests,
        "username"   : username,
    }
    return render(request,'tests/view.html', context)


@login_required
def add_product(request, id):
    form = PatientTesttForm(request.POST or None, request.FILES or None)
    patient = get_object_or_404(User, id=id)
    real_user = pharmacy.user
    pharmacy_id = pharmacy.id
    business = BusinessHour.objects.filter(pharmacy=id)
    username = request.user.username
    print(pharmacy_id)

    if real_user == request.user:
        if "q" in request.POST:
            if form.is_valid():
                pharmacy_product = form.save(commit=False)
                pharmacy_product.pharmacy = pharmacy
                pharmacy_product.save()
                messages.success(request, pharmacy_product.product_name + " has been successfully added !!!")
                return redirect('pharmacy:add_product', id = pharmacy_id)
        else:
            if form.is_valid():
                pharmacy_product = form.save(commit=False)
                pharmacy_product.pharmacy = pharmacy
                pharmacy_product.save()
                messages.success(request, pharmacy_product.product_name + " has been successfully added !!!")
                return redirect('pharmacy:product_home', id = pharmacy_id)
        context = {
            "pharmacy":pharmacy,
            'business': business,
            "form": form,
            'username': username,
            'openclose': current_time.time(),
            'nhasi': nhasi,
        }
        return render(request, 'products/add_product.html', context)
    else:
        return redirect('pharmacy:pharmacys_dashboard')

@login_required
def specimen_home(request,id):
    specimendata = SpecimenData.objects.filter(pathologist = "yes")
    pathologist  = get_object_or_404(User, pk=id)
    username     = request.user.username

    context     = {
        "pathologist"  : pathologist,
        "specimendata" : specimendata,
        "username"     : username,
    }
    return render(request,'tests/specimen.html', context)


@login_required
def specimen_home1(request,id):
    specimendata = SpecimenData.objects.filter(pathologist = "yes")
    pathologist  = get_object_or_404(User, pk=id)
    username     = request.user.username

    context     = {
        "pathologist"  : pathologist,
        "specimendata" : specimendata,
        "username"     : username,
    }
    return render(request,'tests/completed_test.html', context)


@login_required
def perform_test(request,id):
    # specimendata = SpecimenData.objects.filter(pk=id)
    specimendata = get_object_or_404(SpecimenData, pk=id)
    pathologist  = request.user
    username     = request.user.username
    print(specimendata)

    context     = {
        "pathologist"  : pathologist,
        "specimendata" : specimendata,
        "username"     : username,
    }
    return render(request,'tests/perform_test.html', context)


@login_required
def generate_report(request,id):
    # specimendata = SpecimenData.objects.filter(pk=id)
    specimendata = get_object_or_404(SpecimenData, pk=id)
    pathologist  = request.user
    username     = request.user.username
    print(specimendata)

    form     = ReportDataForm(request.POST or None, request.FILES or None)
    print(form)
    reportdata = form.save(commit=False)
    reportdata.user = pathologist
    reportdata.specimendata = specimendata
    specimendata.weight = float(specimendata.weight)
    specimendata.temperature = float(specimendata.temperature)

    if specimendata.weight > 79:
        reportdata.weight_result = "Obese"
    elif specimendata.weight < 60:
        reportdata.weight_result = "Under Weight"
    else:
        reportdata.weight_result = "Normal Weight"

    if specimendata.temperature < 35:
        reportdata.hemoglobin = "11"
        reportdata.RBC = "3.1"
    elif specimendata.temperature > 37:
        reportdata.hemoglobin = "14"
        reportdata.RBC = "3.4"
    else:
        reportdata.hemoglobin = "12"
        reportdata.RBC = "3.3"

    reportdata.save()
    specimendata.status = 'completed'
    specimendata.save()

    context     = {
        "pathologist"  : pathologist,
        "specimendata" : specimendata,
        "username"     : username,
    }
    messages.success(request,"Report has been successfully Generated !!!")
    return redirect('pathologist:reports_home', pathologist.id)


@login_required
def reports_home(request, id):
    pathologist  = get_object_or_404(User, pk=id)
    reportdata = GeneratedReport.objects.filter(user = pathologist)
    print(id)
    username     = request.user.username
    print(reportdata)

    context     = {
        "pathologist"  : pathologist,
        "reportdata"   : reportdata,
        "username"     : username,
    }
    return render(request,'reports/view.html', context)


@login_required
def reports_detail(request, id):
    reportdata  = get_object_or_404(GeneratedReport, pk=id)
    username    = request.user.username
    pathologist = reportdata.user
    print(pathologist)

    context     = {
        "pathologist"  : pathologist,
        "reportdata"   : reportdata,
        "username"     : username,
    }
    return render(request,'reports/report_detail.html', context)


@login_required
def pdoctors_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    doctors    = Doctor.objects.all()
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "doctors"    : doctors,
        "username"   : username,
    }
    return render(request,'pathologist/pdoctors.html', context)


@login_required
def pdoctors_details(request, id):
    docdata  = get_object_or_404(Doctor, pk=id)
    username    = request.user.username
    pathologist = request.user
    print(pathologist)

    context     = {
        "pathologist"  : pathologist,
        "docdata"      : docdata,
        "username"     : username,
    }
    return render(request,'pathologist/pdoctor_detail.html', context)

@login_required
def lab_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "username"   : username,
    }
    return render(request,'tests/plab.html', context)


@login_required
def samples_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "username"   : username,
    }
    return render(request,'tests/psamples.html', context)