from django.shortcuts import render
from django.urls import reverse,reverse_lazy

def LogInOrSignUp(request):
 return render(request,'twitter/loginorsignup.html',{})
 