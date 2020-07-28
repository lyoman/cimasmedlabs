from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required
from test_record.models import RegisterPatient
from doctor.models import SpecimenData

from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q


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
def patients_home(request,id):
    pathologist = get_object_or_404(User, pk=id)
    patients    = User.objects.filter(is_patient=True)
    username    = request.user.username

    context     = {
        "pathologist": pathologist,
        "patients"   : patients,
        "username"   : username,
    }
    return render(request,'patients/view.html', context)

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