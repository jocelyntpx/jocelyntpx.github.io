from django.http import HttpResponse
from .models import userInfo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
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

	user_info = userInfo(user_name=user_name,user_number=user_number,user_email=user_email,faculty=faculty,user_password=user_password,user_repeatpass=user_repeatpass)
	user_info.save()
	messages.success(request,'Account created successfully') 
	return render(request,"nusmerch/signupsuccessful.html")

def home_page(request):
	return render(request, "nusmerch/index.html")

def about_page(request):
	return render(request, "nusmerch/generic.html")

def elements_page(request):
	return render(request, "nusmerch/elements.html")

def sign_in(request):
	return render(request,"nusmerch/login.html")


""" def sign_in_form(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# log in user
			form.save()
			user = form.cleaned_data.get('email')
			messages.success(request,'Account created successfully for {user_name}:')
			return redirect('nusmerch/loggedin.html')
	else:
		form = UserCreationForm()
	return render(request,'nusmerch/login.html',{'form':form}) 
"""


def logged_in(request):
	return render(request,"nusmerch/loggedin.html")