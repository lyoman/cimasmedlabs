from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

# Create your views here. 
@login_required
def doctor_dashboard(request):
    username = request.user.username
    doctor = User.objects.filter(username=username, is_doctor = True)
    # doctor = doctor.order_by('username')
    print(doctor)

    context = {
        'doctor': doctor, 
        'username':username,
    }
    return render(request,'doctor/view.html', context)