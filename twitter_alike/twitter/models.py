from django.db import models

class UserInformation(models.Model):
  """def __str__(self):
    return self.username"""
  username=models.CharField(
    max_length=20,
    unique=True,
  error_messages={
    'unique': ("A user with that username already exists."),
    'blank':("Username cannot be blank")
  }
    )
  password = models.CharField(("password"), max_length=20)



# Create your models here.
