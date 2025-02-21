from django.db import models
from cuenta.models import User

# Create your models here.
class Transaction(models.Model):
    tipo = models.CharField(max_length=50)
    estatus = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    userOri = models.ForeignKey(User, on_delete=models.CASCADE)
    userDest = models.CharField(max_length=50)