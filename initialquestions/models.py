from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project
from django.db import models
from multiselectfield import MultiSelectField

class Initialquestion(models.Model):

    INITIAL_ONE_CHOICES = (
      ('Diagnostic', 'Diagnostic'),
      ('Therapeutic','Therapeutic'),
      ('Population health','Population health'),
      ('Care-based','Care-based'),
      ('Triage','Triage'),
      ('Self-care','Self-care'),
      ('Health promotion','Health promotion'),
      ('Remote Monitoring','Remote Monitoring'),
      ('Remote Consultation','Remote Consultation'),
      ('Other','Other'),
      )

    INITIAL_TWO_CHOICES = (
      ('Primary Care', 'Primary Care'),
      ('Secondary Care','Secondary Care'),
      ('Tertiary Care','Tertiary Care'),
      ('Individual Care of Self','Individual Care of Self'),
      ('Triage','Triage'),
      ('For the purposes of population screening','For the purposes of population screening'),
      ('Other','Other'),
      )


    initial_one = MultiSelectField(choices=INITIAL_ONE_CHOICES)
    initial_two = MultiSelectField(choices=INITIAL_TWO_CHOICES)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
