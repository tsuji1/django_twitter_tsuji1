from django.db import models
from django.core.validators import MinLengthValidator

class UserInformation(models.Model):
  """def __str__(self):
    return self.username"""
  username=models.CharField(
    max_length=20,
    validators=[MinLengthValidator(7)],
    unique=True,
  error_messages={
    'unique': ("A user with that username already exists."),
    'blank':("Username cannot be blank")
  }
    )
  password = models.CharField(("password"), max_length=20)



# Create your models here.
