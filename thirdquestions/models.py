# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Thirdquestion(models.Model):
  third_one = models.TextField()
  third_two = models.TextField()
  third_three = models.TextField()
  third_four = models.TextField()
  third_five = models.TextField()
  third_six = models.TextField()
  third_seven = models.FileField(upload_to='documents/')
  third_eight = models.TextField()
  third_nine = models.TextField()
  third_ten = models.FileField(upload_to='documents/')
  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)



