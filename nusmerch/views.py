from django.http import HttpResponse
from .models import userInfo
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from nusmerch.forms import (
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,"nusmerch/index.html")

def addUser(request):
	return render(request,"nusmerch/signup.html")

def add_user_form_submission(request):
	print("User Registered Successfully")
	user_name = request.POST["user_name"]
	user_number = request.POST["user_number"]
	user_email = request.POST["user_email"]
	faculty = request.POST.get("faculty",False)
	user_password = request.POST["user_password"]
	user_repeatpass = request.POST["user_repeatpass"]
	image = request.POST["user_repeatpass"]

	user_info = userInfo(user_name=user_name,user_number=user_number,user_email=user_email,faculty=faculty,user_password=user_password,user_repeatpass=user_repeatpass,image=image)
	user_info.save()
	messages.success(request,'Account created successfully') 
	return render(request,"nusmerch/signupsuccessful.html")

def login_form_submission(request):
    return render(request,"nusmerch/loggedin.html")

def home_page(request):
	return render(request, "nusmerch/index.html")

def about_page(request):
	return render(request, "nusmerch/generic.html")

def elements_page(request):
	return render(request, "nusmerch/elements.html")

def login(request):
	return render(request,"nusmerch/login.html")

def logged_in(request):
	return render(request,"nusmerch/loggedin.html")

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('nusmerch:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'nusmerch/edit_profile.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'nusmerch/profile.html', args)
 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('nusmerch:view_profile'))
        else:
            return redirect(reverse('nusmerch:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'nusmerch/change_password.html', args)

def merch(request):
    return render(request, "nusmerch/merch.html")
