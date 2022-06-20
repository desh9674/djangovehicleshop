from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Create your models here.
from django.db import models
from django.core.validators import RegexValidator


class Car(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    wheels = [("4", "Four Wheeler"), ("3", "Three Wheeler"), ("2", "Two Wheeler")]
    vNumber = models.CharField(max_length=20, blank=True, null=True, validators=[alphanumeric])
    
    vType = models.CharField(max_length=20, choices=wheels, default=4)
    vModel = models.TextField()
    vDescription = models.TextField()
    def __str__(self):
        return self.vModel
