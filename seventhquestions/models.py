# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Seventhquestion(models.Model):
  seventh_one = models.FileField(upload_to='documents/')
  seventh_two = models.FileField(upload_to='documents/')
  seventh_three = models.FileField(upload_to='documents/')
  seventh_four = models.FileField(upload_to='documents/')
  seventh_five = models.TextField()
  seventh_six = models.TextField()
  seventh_seven = models.TextField()
  seventh_eight = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
