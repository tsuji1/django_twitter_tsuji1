from django.shortcuts import render
from .models import UserInformation
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy

def LogInOrSignUp(request):
 return render(request,'twitter/loginorsignup.html',{})


"""
class SignUpView(CreateView):
  form_class=UserCreationForm
  template_name = 'twitter/signup.html'
  model = UserInformation
  fields = ['username','password']
  
  success_url = reverse_lazy('twitter:loginorsignup')
"""