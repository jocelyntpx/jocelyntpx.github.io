from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import userInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password"}))
    class Meta():
        model = User
        fields = ('email','password')
        widgets={
            'email':forms.TextInput(attrs={'type':"text"}),
        }


class EditProfileForm(UserChangeForm):

    class Meta():
        model = userInfo
        fields = (
            'number',
            'password',
            'faculty',
            'major',
            'campus_residential_type',
            'image',

        )

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('name','number','matric','email','major','faculty','campus_residential_type','image')

        widgets={
            'faculty':forms.Select(attrs={'style':'width:220px'}),
            'campus_residential_type':forms.Select(attrs={'style':'width:130px'})
        }
