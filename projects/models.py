from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_audited = models.TextField(default="No")
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
