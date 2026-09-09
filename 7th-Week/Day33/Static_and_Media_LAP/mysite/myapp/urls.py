from django.conf.urls import static
from django.urls import path

from Static_and_Media_LAP.mysite.mysite import settings
from . import views

urlpatterns =[
    path('uploade/' , views.upload_image , name='upload_image'),
]
