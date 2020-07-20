from django.contrib.auth.models import User
from .models import userInfo, Product
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password"}))
    class Meta():
        model = User
        fields = ('username','email','password')


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
        fields = ('name','number','matric','faculty','campus_residential_type','image')

        widgets={
            'faculty':forms.Select(attrs={'style':'width:220px'}),
            'campus_residential_type':forms.Select(attrs={'style':'width:130px'})
        }

class UploadProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = (
            'name_of_MERCH','price','description','organisation','category','filter','filter_faculty',
            'filter_matric', 'filter_email', 'filter_campus','form','image', 'sizing','backview'
        )
        widgets={
            'category':forms.Select(attrs={'style':'width:220px'}),
            'filter': forms.Select(attrs={'style': 'width:220px'})
        }
