from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from nusmerch.models import userInfo, Product, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

from nusmerch.forms import (
    EditProfileForm, UserForm, UserProfileForm, UploadProductForm
)
from django.contrib.auth import authenticate, logout, login as login_check
from django.contrib.auth.views import (
    PasswordResetView,  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
import json
from django.db.models import Q


# Create your views here.
def index(request):
	return render(request,"nusmerch/index.html")

def addUser(request):
	return render(request,"nusmerch/signup.html")

def add_user_form_submission(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #user.is_active = False
            profile = profile_form.save(commit=False)
            user.set_password(user.password)
            user.save()

     #       current_site = get_current_site(request)
     #       mail_subject = 'Activate your NUSMERCH account.'
      #      message = render_to_string('nusmerch/acc_active_email.html', {
       #         'user': user,
        #        'domain': current_site.domain,21
         #       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
          #      'token': account_activation_token.make_token(user),
         #   })
          #  to_email = form.cleaned_data.get('email')
           # email = EmailMessage(
            #    mail_subject, message, to=[to_email]
           # )
          #  email.send()


            profile.user = user
            profile.email = user.email
            if not user.email.split('@')[1] == "u.nus.edu":
                user.delete()
                return render(request, "nusmerch/wrong_email.html")
          #  if 'profile_pic' in request.FILES:
            #    print('found it')
          #      profile.image = request.FILES['profile_pic']
            profile.save()
            registered = True

            #return HttpResponse('Please confirm your email address to complete the registration')
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = userInfo.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



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

def product(request):
    return render(request, "nusmerch/product.html")

def logged_in(request):	
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            user = form.get_user()
            login_check(request,user)
            products = Product.objects.filter(category = "Shirt")
            profile = userInfo.objects.get(user=user)

            pdt_nil = products.filter(filter="NO")
            pdt_faculty = products.filter(filter_faculty=profile.faculty)
            pdt_email = products.filter(filter_email__icontains=profile.email)
            pdt_matric = products.filter(filter_matric__icontains=profile.matric)
            pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
            products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

            context = {'products':products}
            return render(request, "nusmerch/shirt.html", context)
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
        profile =userInfo.objects.get(user=user)
        form = EditProfileForm(request.POST,request.FILES,instance=profile)
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

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'nusmerch/profile.html')

        else:
            return render(request, 'nusmerch/change_password.html')

    else:
        form = PasswordChangeForm(request.user)
        args = {'form': form}
        return render(request, 'nusmerch/change_password.html', args)



def merch(request):
    if request.user.is_authenticated:
        customer_email = request.user.email
        customer = userInfo.objects.get(email=customer_email)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderItem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "nusmerch/merch.html", context)


def shirt(request):
    products = Product.objects.filter(category = "Shirt")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/shirt.html", context)

def bottom(request):
    products = Product.objects.filter(category = "Bottom")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/buttom.html", context)

def outerwear(request):
    products = Product.objects.filter(category = "Outerwear")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/outerwear.html", context)

def lifestyle(request):
    products = Product.objects.filter(category = "Lifestyle")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/lifestyle.html", context)

def laptop(request):
    products = Product.objects.filter(category = "Laptop Accessories")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/laptop.html", context)

def others(request):
    products = Product.objects.filter(category = "Others")
    if request.user.is_authenticated:
        user = request.user
        profile = userInfo.objects.get(user=user)
        pdt_nil = products.filter(filter = "NO")
        pdt_faculty = products.filter(filter_faculty = profile.faculty)
        pdt_email = products.filter(filter_email__icontains = profile.email)
        pdt_matric = products.filter(filter_matric__icontains = profile.matric)
        pdt_campus = products.filter(filter_campus=profile.campus_residential_type)
        products = pdt_faculty | pdt_campus | pdt_nil | pdt_matric | pdt_email

    else:
        products = products

    context = {'products':products}
    return render(request, "nusmerch/others.html", context)


def search_results(request):
    query = request.GET.get('search')
    products = Product.objects.filter(Q(name_of_MERCH__icontains=query))
    context = {'products':products}
    return render(request, "nusmerch/search_results.html", context)

def logout(request):
    if request.method == "POST":
        logout(request)
        return render(request, "nusmerch/index.html")

def user_account(request):
    return render(request, "nusmerch/profile.html")

def cart(request):
    if request.user.is_authenticated:
        customer_email = request.user.email
        customer = userInfo.objects.get(email=customer_email)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request, 'nusmerch/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'nusmerch/checkout.html', context)

def delete_product(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)   

    product = Product.objects.get(id=productId)

    if action == 'delete':
        product.delete()

    return JsonResponse('Product has been deleted', safe=False)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer_email = request.user.email
    customer = userInfo.objects.get(email=customer_email)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
        orderItem.save()
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
        orderItem.save()
    elif action == 'removeAll':
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

def product(request, pk_test):
    product = Product.objects.get(id=pk_test)
    return render(request, "nusmerch/product.html", product)

@login_required
def sell_merch(request):
    if request.method == 'POST':
        form = UploadProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            user = request.user
            seller = userInfo.objects.get(user=user)
            product.user = seller
            product.save()
            products = Product.objects.filter(category="Shirt")
            context = {'products': products}
            return render(request, 'nusmerch/shirt.html', context)
        else:
            print(form.errors)
    else:
        form = UploadProductForm()
    user = request.user
    seller = userInfo.objects.get(user=user)
    listed = Product.objects.filter(user=seller)
    args = {'form': form,'listed':listed}
    return render(request, 'nusmerch/sell_merch.html', args)

def wrong_email(request):
    return render(request, "nusmerch/wrong_email.html")