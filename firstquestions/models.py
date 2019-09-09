from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models



class Firstquestion(models.Model):
    first_one = models.TextField()
    first_two = models.TextField()
    first_three = models.TextField()
    first_four = models.TextField()
    first_five = models.TextField()
    first_six = models.TextField()
    # first_seven = models.TextField()
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

