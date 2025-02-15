from django.db import models

from datetime import datetime

# Create your models here.

class NivelAceeso(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class User(models.Model):
    nombre = models.CharField(max_length=50)
    contra = models.CharField(max_length=100)
    fechaalta = models.DateTimeField(default=datetime.now, blank=True)
    nivel = models.ForeignKey(NivelAceeso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre