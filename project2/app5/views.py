from django.shortcuts import render

def other(request):
    return render(request,"app5/other.html")

def relative_url(request):
    return render(request,"app5/relative_url.html")
