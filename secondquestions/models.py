from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Secondquestion(models.Model):
  second_one = models.TextField()
  second_two = models.TextField()
  second_three = models.TextField()
  second_four = models.TextField()
  second_five = models.TextField()
  second_six = models.TextField()
  second_seven = models.TextField()
  second_eight = models.TextField()
  second_nine = models.TextField()
  developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.OneToOneField(Project, on_delete=models.CASCADE)


# class SecondquestionForm(ModelForm):
#   class Meta:
#     model = Secondquestion
#     fields = ['second_one', 'second_two', 'second_three', 'second_four', 'second_five', 'second_six', 'second_seven', 'second_eight', 'second_nine']
