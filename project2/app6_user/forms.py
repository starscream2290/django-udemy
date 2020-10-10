from django import forms
from django.contrib.auth.models import User
from app6_user.models import User_info

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username","email","password")

class User_info_form(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ("portfolio_site","profile_pic")
