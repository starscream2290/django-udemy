from django.shortcuts import render
from app4.forms import User_form
from . import forms
from app4.models import User

def index(request):
    return render(request,'app4/index.html')

def User_form_views(request):
    form = User_form()
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form Error")
    return render(request,"app4/form.html",{"form":form})
