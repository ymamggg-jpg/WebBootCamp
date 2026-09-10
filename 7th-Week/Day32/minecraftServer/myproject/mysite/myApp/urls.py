from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("apply/", views.apply, name="apply"),
    path("rules/", views.rules, name="rules"),
    path("success/", views.success, name="success"),
]