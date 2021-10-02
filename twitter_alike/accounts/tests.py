from django.template import context
from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import SignUpView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()

class TestsSignUp(TestCase):

  def setUp(self):
    url = reverse('accounts:signup')
    self.response = self.client.get(url)

  def test_signup_status_code(self):

    self.assertEquals(self.response.status_code, 200)

  def test_signup_url_resolves_signup_view(self):
    view = resolve('/accounts/signup/')
    self.assertEquals(view.func.view_class, SignUpView)

  def test_csrf(self):
    self.assertContains(self.response,'csrfmiddlewaretoken')

  def test_contains_form(self):
    form = self.response.context.get('form')
    self.assertIsInstance(form, UserCreationForm)

class SuccessfulSignUpTests(TestCase):
    def setUp(self):
      url = reverse('accounts:signup')
      data = {
          'username': 'test',
          'password1': 'abcdef123456',
          'password2': 'abcdef123456'
      }
      self.response = self.client.post(url, data)
      self.home_url = reverse('twitter:loginorsignup')

    def test_redirection(self):

      self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
      self.assertTrue(User.objects.exists())

class InvalidSignUpTests_blank(TestCase):
  def setUp(self):
    url = reverse('accounts:signup')
    self.response = self.client.post(url, {})  # submit an empty dictionary
    data_hiragana = {
    'username': 'テスト',
    'password1': 'abcdef123456',
    'password2': 'abcdef123456'
    }

  def test_signup_status_code(self):

    self.assertEquals(self.response.status_code, 200)

  def test_form_errors(self):
    form = self.response.context.get('form')
    self.assertTrue(form.errors)

  def test_dont_create_user(self):
    self.assertFalse(User.objects.exists())

class InvalidSignUpTests_hiragana(TestCase):
  def setUp(self):
    url = reverse('accounts:signup')
    data_hiragana = {
    'username': 'テスト',
    'password1': 'abcdef123456',
    'password2': 'abcdef123456'
    }
    self.response = self.client.post(url, data_hiragana)  # submit an empty dictionary


  def test_signup_status_code(self):

    self.assertEquals(self.response.status_code, 200)

  def test_form_errors(self):
    form = self.response.context.get('form')
    self.assertTrue(form.errors)

  def test_dont_create_user(self):
    self.assertFalse(User.objects.exists())

class LoginLogoutTest(TestCase):
  def setUp(self):
    url_signup = reverse('accounts:signup')
    url_login=reverse('login')
    self.home_url=reverse('twitter:loginorsignup')
    data_signup = {
    'username': 'test',
    'password1': 'abcdef123456',
    'password2': 'abcdef123456'
    }
    data_login={
    'username': 'test',
    'password': 'abcdef123456',
    }
    self.client.post(url_signup, data_signup)
    self.response  = self.client.post(url_login, data_login)
    
  def test_redirection(self):

    self.assertRedirects(self.response, self.home_url)
  
  def test_login_authorization(self):
    response = self.client.get(self.home_url)
    user = response.context.get('user')
    self.assertTrue(user.is_authenticated)
    self.assertFalse(user.is_anonymous)
  
  def test_logout_authorization(self):
    url_logout=reverse('logout')
    self.client.get(url_logout)
    response = self.client.get(self.home_url)
    user = response.context.get('user')
    self.assertFalse(user.is_authenticated)

class SuccessfulPasswordChangeTest(TestCase):
  
  def setUp(self):
    url_passwordchange=reverse('password_change')
    url_signup = reverse('accounts:signup')
    url_login=reverse('login')
    self.home_url=reverse('password_change_done')
    data_signup = {
      'username': 'test',
      'password1': 'abcdef123456',
      'password2': 'abcdef123456'
    }
    data_login={
      'username': 'test',
      'password': 'abcdef123456',
    }
    data_passchange ={
      'old_password':'abcdef123456',
      'new_password1':'abcdef1234567',
      'new_password2':'abcdef1234567'
    }
    self.client.post(url_signup, data_signup)
    self.client.post(url_login, data_login)
    self.response=self.client.post(url_passwordchange,data_passchange)
    
  def test_redirection(self):

    self.assertRedirects(self.response, self.home_url)
  
  def test_password_changed(self):
    now_password='abcdef1234567'
    response = self.client.get(self.home_url)
    user = response.context.get('user')
    self.assertTrue(user.password,now_password)

  



    










# Create your tests here.
