from django.http import HttpResponse, HttpResponseRedirect
from nusmerch.models import userInfo, Product
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from nusmerch.forms import (
    EditProfileForm, UserForm, UserProfileForm
)
from django.contrib.auth import authenticate, logout, login as login_check
from django.contrib.auth.views import (
    PasswordResetView,  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
	return render(request,"nusmerch/index.html")

def addUser(request):
	return render(request,"nusmerch/signup.html")

def add_user_form_submission(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return render(request,'nusmerch/signupsuccessful.html')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'nusmerch/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            user = form.get_user()
            login_check(request,user)
            products = Product.objects.all()
            context = {'products':products}
            return render(request, "nusmerch/merch.html", context)
      #  else:
            #messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'nusmerch/login.html', {})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "nusmerch/login.html",
                    context={"form":form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        form = EditProfileForm(request.POST, instance=userInfo)
        form.user = user
        if form.is_valid():
            form.save()
            return render(request, 'nusmerch/profile.html')
        else:
            print(form.errors)
    else:
        form = EditProfileForm()
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
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "nusmerch/merch.html", context)

def logout(request):
    if request.method == "POST":
        logout(request)
        return render(request, "nusmerch/logout.html")

def user_account(request):
    return render(request, "nusmerch/profile.html")

def cart(request):
    context = {}
    return render(request, 'nusmerch/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'nusmerch/checkout.html', context)