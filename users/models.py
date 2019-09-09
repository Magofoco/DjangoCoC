from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length=100, default='')
  last_name = models.CharField(max_length=100, default='')
  organization = models.CharField(max_length=100, default='')
  location = models.CharField(max_length=100, default='')
  postcode = models.CharField(max_length=100, default='')
  phone = models.CharField(max_length=100, default='')
  agree_conditions = models.BooleanField(default=True)
  is_nhs = models.BooleanField(default=False)

  def __str__(self):
    return self.email
