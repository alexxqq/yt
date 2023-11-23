from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',index,name ='home'),
    path('register/',register_user,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('account/',account,name='account'),
    path('add_video/',add_video,name='add_video'),
    path('search/',search,name='search'),
]
