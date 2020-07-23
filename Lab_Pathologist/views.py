from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.template.loader import render_to_string

from django.db.models import Q

# Create your views here. 
@login_required
def pathologist_dashboard(request):
    username = request.user.username
    pathologist = User.objects.filter(username=username, is_pathologist = True)
    # pathologist = pathologist.order_by('username')
    print(pathologist)

    context = {
        'pathologist': pathologist, 
        'username':username,
    }
    return render(request,'pathologist/view.html', context)