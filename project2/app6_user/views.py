from django.shortcuts import render
from app6_user.forms import UserForm,User_info_form

from django.contrib.auth import authenticate,login,logout
from django.http import  HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def special(request):
    return HttpResponse("you are logged-in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def index(request):
    return render(request,'app5/index.html')

def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info = User_info_form(data=request.POST)

        if user_form.is_valid() and user_info.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = user_info.save(commit=False)
            info.user = user
            if "profile_pic" in request.FILES:
                info.profile_pic = request.FILES["profile_pic"]
            info.save()

            registered = True

        else:
            print(user_form.errors,user_info.errors)
    else:
        user_form = UserForm()
        user_info = User_info_form()
    return render(request,"app6_user/registration.html",
                            {"user_form":user_form,
                             "user_info":user_info,
                             "registered":registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account is not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,"app6_user/login.html",{})
