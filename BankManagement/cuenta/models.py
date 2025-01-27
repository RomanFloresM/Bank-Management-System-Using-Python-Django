from django.db import models

from datetime import datetime

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    contra = models.CharField(max_length=100)
    fechaalta = models.DateTimeField(default=datetime.now, blank=True)