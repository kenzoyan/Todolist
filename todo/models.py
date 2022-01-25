from venv import create
from django.db import models

# Create your models here.
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title