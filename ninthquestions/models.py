# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Ninthquestion(models.Model):
  ninth_one =  models.TextField()
  ninth_two = models.FileField(upload_to='documents/')
  ninth_three = models.FileField(upload_to='documents/')
  ninth_four = models.TextField()
  ninth_five = models.TextField()
  ninth_six = models.TextField()
  ninth_seven = models.FileField(upload_to='documents/')
  ninth_nine = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
