from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Eighthquestion(models.Model):
  eighth_one = models.TextField()
  eighth_two = models.TextField()
  eighth_three = models.TextField()
  eighth_four = models.TextField()
  eighth_five = models.FileField(upload_to='documents/')
  eighth_six = models.FileField(upload_to='documents/')
  eighth_seven = models.FileField(upload_to='documents/')
  eighth_eight = models.FileField(upload_to='documents/')
  eighth_nine = models.FileField(upload_to='documents/')
  eighth_ten = models.TextField()
  eighth_eleven = models.TextField()
  eighth_twelve = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)
