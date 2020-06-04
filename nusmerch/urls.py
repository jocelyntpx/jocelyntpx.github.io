"""nusmerchd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include



urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^add_user/$',views.addUser,name='add_user'),
	url(r'^add_user_form_submission/$',views.add_user_form_submission,name='add_user_form_submission'),
	url(r'^home_page/$',views.home_page,name='home_page'),
	url(r'^about_page/$',views.about_page,name='about_page'),
	url(r'^elements_page/$',views.elements_page,name='elements_page'),
    url(r'^sign_in/$',auth_views.LoginView.as_view(template_name='nusmerch/login.html'),name='sign_in'),
    url(r'^logged_in/$',views.logged_in,name='logged_in'),

]
