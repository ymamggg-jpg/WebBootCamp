from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
from django.views import View

class RegisterView(View):

    def get(slef , request):
        return render(request , "register.html")

    def post(self , request):
        username= request.POST.get("username")
        password= request.POST.get("password")

        request.session["username"] = username
        # request.session["password"]= password

        return redirect("profile")
########################################################

class LoginView(View):
    def get(slef , request):
            return render(request , "login.html")
    
    def post(self , request):
        username= request.POST.get("username")
        password= request.POST.get("password")
    
        if request.session["username"] == username:
        
           return redirect("profile")
        else:
            return HttpResponse("wrong username")
#############################################################


class ProfileView(View):

    def get(self, request):
        username = request.session.get("username")

        return render(request, "profile.html", {
            "username": username
        })

def status_view(request):
    return JsonResponse({
        "status": "ok"
    })