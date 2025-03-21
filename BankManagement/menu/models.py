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
    concepto = models.CharField(max_length=50, blank=True)
    referencia = models.CharField(max_length=50, blank=True)

class BillUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateTimeField(auto_now_add=True)

    def updateWallet(self, amount):
        self.wallet += amount
        self.save()