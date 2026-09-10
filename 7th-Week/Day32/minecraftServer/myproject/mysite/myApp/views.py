from django.shortcuts import render
from .models import Player


# Create your views here.




def home(request):
    server_info = {
        "edition": "Java",
        "version": "1.26",
        "IP": "63729.re",
        "number_of_members":Player.objects.count()
        
    }

    return render(request, "home.html", {"server": server_info})





from django.shortcuts import render, redirect
from .models import Player


def apply(request):
    error = ""

    if request.method == "POST":
        gamertag = request.POST.get("gamertag")
        age = request.POST.get("age")
        discord = request.POST.get("discord")

        if Player.objects.filter(gamertag=gamertag).exists() or Player.objects.filter(discord=discord).exists():
            error = "This player is already registered."

        else:
            Player.objects.create(
                gamertag=gamertag,
                age=age,
                discord=discord
            )

            return redirect("success")

    return render(request, "apply.html", {"error": error})


def rules(request):
    rules_list = [
        "No stealing from other players",
        "No cheating or hacks",
        "Respect all members",
        "Do not destroy other players' builds !!!"
    ]

    return render(request, "rules.html", {"rules": rules_list})

def success(request):
    return render(request, "success.html")
