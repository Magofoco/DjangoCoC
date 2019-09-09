# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Fourthquestion(models.Model):
  fourth_one = models.TextField()
  fourth_two = models.TextField()
  fourth_three = models.TextField()
  fourth_four = models.TextField()
  fourth_five = models.TextField()
  fourth_six = models.FileField(upload_to='documents/')
  fourth_seven = models.FileField(upload_to='documents/')
  fourth_eight = models.TextField()
  fourth_nine = models.FileField(upload_to='documents/')

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)
