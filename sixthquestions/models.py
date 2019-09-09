# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Sixthquestion(models.Model):
  sixth_one = models.FileField(upload_to='documents/')
  sixth_two = models.FileField(upload_to='documents/')
  sixth_three = models.FileField(upload_to='documents/')
  sixth_four = models.FileField(upload_to='documents/')
  sixth_five = models.FileField(upload_to='documents/')
  sixth_six = models.FileField(upload_to='documents/')
  sixth_seven = models.FileField(upload_to='documents/')
  sixth_eight = models.TextField()
  sixth_nine = models.TextField()
  sixth_ten = models.TextField()
  sixth_eleven = models.TextField()
  sixth_twelve = models.TextField()
  sixth_thirteen = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
