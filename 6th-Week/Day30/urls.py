from django.urls import path
from .views import home, ReportsView

app_name = "dashboard"

urlpatterns = [
    path("", home, name="home"),
    path("reports/", ReportsView.as_view(), name="reports"),
]