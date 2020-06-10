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
from django.contrib.auth import (
    login, logout
)
from django.contrib.auth.views import (
    LoginView, PasswordResetView,  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 
)



urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^add_user/$',views.addUser,name='add_user'),
	url(r'^add_user_form_submission/$',views.add_user_form_submission,name='add_user_form_submission'),
	url(r'^home_page/$',views.home_page,name='home_page'),
	url(r'^about_page/$',views.about_page,name='about_page'),
	url(r'^elements_page/$',views.elements_page,name='elements_page'),
    url(r'^login/$', LoginView.as_view(template_name='nusmerch/login.html'), name="login"),
    url(r'^logged_in/$',views.logged_in,name='logged_in'),
    url(r'^logout/$', logout, {'template_name': 'nusmerch/logout.html'}, name='logout'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^logged_in/profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^logged_in/profile/view/$',views.view_profile,name='view_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    
    url(r'^password/reset/$', PasswordResetView.as_view(template_name='nusmerch/reset_password.html'), name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='nusmerch/reset_password_done.html'), name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='nusmerch/reset_password_confirm.html'), name='password_reset_confirm'),

    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name='nusmerch/reset_password_complete.html'), name='password_reset_done'),

    url(r'^merch/$',views.merch,name='merch'),
]
