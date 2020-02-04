from django.shortcuts import render

# Create your views here.

def pres(request):
    return render(request,"locate_me/home.html",{})
