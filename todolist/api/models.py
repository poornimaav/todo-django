
from django.db import models
from django import forms

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


