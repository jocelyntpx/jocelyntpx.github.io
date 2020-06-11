from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import userInfo, Image
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password"}))
    class Meta():
        model = User
        fields = ('username','password')


class EditProfileForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = (
            'number',
            'faculty',
            'campus_residential_type',
            'image',
        )
        widgets={
            'faculty':forms.Select(attrs={'style':'width:220px'}),
            'campus_residential_type':forms.Select(attrs={'style':'width:130px'})
        }

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('email','name','number','matric','faculty','campus_residential_type','image')

        widgets={
            'faculty':forms.Select(attrs={'style':'width:220px'}),
            'campus_residential_type':forms.Select(attrs={'style':'width:130px'})
        }

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ImageForm(forms.ModelForm):
    class Meta():
        model= Image
        fields= ["name", "imagefile"]
