from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from admins.views import admins_dashboard
# from patient.views import patient_dashboard
# from visitor.views import home_page
from django.contrib import messages
from .forms import (PatientSignUpForm)
# Create your views here.

@login_required
def redirect_logged (request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    elif request.user.is_patient:
        return redirect('patient:patient_dashboard')
    elif request.user.is_doctor:
        return redirect('doctor:doctor_dashboard')
    else:
        return redirect('users:login')
        

def dashboard(request):
    return HttpResponseRedirect('admin/')


def home_page(request):
    print('Hello world')
    if request.user.is_authenticated:
        return redirect('users:dash')
    else:
        return redirect('users:login')
    
    # return render(request,'base.html')

def registration_redirect(request):
    if request.user.is_authenticated:
        return redirect('users:dash')
    else:
        return redirect('users:register_patient')


def about(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'about.html', {'username':username,})
    else:
        return render(request,'visitor_about.html')

def contact(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'contact.html', {'username':username,})
    else:
        return render(request,'visitor_contact.html')


def register_patient(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!!!')
            return redirect('users:login')
    else:
        form = PatientSignUpForm()
    
    if request.user.is_authenticated:
        return redirect('users:dash')
    else:
        return render(request,'users/register_patient.html',{'form':form})