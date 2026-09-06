from django.urls import path
from . import views

# urlpatterns ={
#  path('' , views.home , name = "list") ,
#  path('detail/' , views.detail , name = "detail") ,
#  path('category/' , views.category , name = "category") ,

# }
app_name = 'blog'


urlpatterns = [
    path('', views.list, name="list"),
    path("<int:id>/", views.detail, name="detail"),
    path("category/<str:category>/",views.category,name="category"),
]