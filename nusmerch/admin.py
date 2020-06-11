from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import userInfo, Product
from .forms import UserForm, UserProfileForm

# Register your models here.
admin.site.register(userInfo)
admin.site.register(Product)
