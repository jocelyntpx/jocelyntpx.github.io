from django.shortcuts import render
from django.http import HttpResponse
from .models import userInfo

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

	user_info = userInfo(user_name=user_name,user_number=user_number,user_email=user_email,faculty =faculty,user_password=user_password)
	user_info.save()
	return render(request,"nusmerch/signup.html")