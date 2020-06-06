from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import userInfo


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = userInfo
        fields = (
            'user_name',
            'user_email',
            'user_number',
            'user_password',
            'faculty'
        )
