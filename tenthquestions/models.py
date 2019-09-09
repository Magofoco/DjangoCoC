# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Tenthquestion(models.Model):
  tenth_one =  models.FileField(upload_to='documents/')
  tenth_two = models.FileField(upload_to='documents/')
  tenth_three = models.FileField(upload_to='documents/')
  tenth_four = models.TextField()
  tenth_five = models.FileField(upload_to='documents/')
  tenth_six = models.TextField()
  tenth_seven = models.TextField()
  tenth_eight = models.TextField()
  tenth_nine = models.TextField()
  tenth_ten = models.TextField()
  tenth_eleven = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
