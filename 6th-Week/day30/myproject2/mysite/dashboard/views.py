from django.shortcuts import render
from django.views import View

# Create your views here.



def home(request):
    return render(request, "dashbord/home.html")


def reports(request):
    return render(request, "dashboard/reports.html")

class ReportsView(View):
    def get(self, request):
        return render(request, "dashborad/reports.html")