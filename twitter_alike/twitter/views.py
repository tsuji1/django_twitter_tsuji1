from django.shortcuts import render
from .models import UserInformation
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy

def LogInOrSignUp(request):
 return render(request,'twitter/loginorsignin.html',{})

def LogIn(request):
  return render(request,'twitter/login.html',{})

class SignUpView(CreateView):
  template_name = 'twitter/signup.html'
  model = UserInformation
  fields = ['username','password']
  
  success_url = reverse_lazy('twitter:login')
