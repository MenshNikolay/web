from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    group_id = models.IntegerField(default=1)

    def __str__(self):
        return self.last_name


class Kid(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    group_number = models.IntegerField()

# Create your models here.
