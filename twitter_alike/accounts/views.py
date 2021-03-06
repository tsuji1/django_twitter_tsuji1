from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy
from .forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(CreateView):
  form_class=UserCreationForm
  template_name = 'accounts/signup.html'
  success_url = reverse_lazy('twitter:loginorsignup')

class PasswordChangeView(CreateView):
  form_class=UserChangeForm
  template_name = 'accounts/signup.html'
  success_url = reverse_lazy('twitter:loginorsignup')
  

