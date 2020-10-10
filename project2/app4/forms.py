from django import forms
from app4.models import User
#from django.forms import ModelForm
#from django.core import validators

Title_Choices=[ ("Mr"),("Ms")]

class User_form(forms.ModelForm):
    #name= forms.CharField
    class Meta:
        model = User
        fields = "__all__"
