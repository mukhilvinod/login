from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [

    re_path('register/',views.register,name='register'),
    re_path('login/',views.login,name='login'),
    re_path('home/',views.home,name='home'),
    



    
]