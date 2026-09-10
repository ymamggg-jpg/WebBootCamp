
# from django.contrib import admin
from django.urls import path
from pages.views import index, faq, team
# from . import views

urlpatterns = [

    path('', index, name='index'),
    path('about', faq, name='faq'),
    path('contact', team, name='team'),
]