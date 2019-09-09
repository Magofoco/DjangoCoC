from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Fifthquestion(models.Model):
  fifth_one = models.TextField()
  fifth_two = models.TextField()
  fifth_three = models.TextField()
  fifth_four = models.TextField()
  fifth_five = models.TextField()
  fifth_six = models.TextField()

  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)

