from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'twitter'

urlpatterns = [
    path('',views.LogInOrSignUp,name="loginorsignup"),
    
]