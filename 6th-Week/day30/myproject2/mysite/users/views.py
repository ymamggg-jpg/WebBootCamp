from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request , "uesrs/login.html")

def profile (request):
    return render(request , "users/profile.html")