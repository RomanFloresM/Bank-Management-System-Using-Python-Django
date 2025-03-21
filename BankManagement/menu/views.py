from django.shortcuts import render
from menu.models import BillUser, Transaction
from cuenta.models import User
from django.http import Http404
from decimal import Decimal

# Create your views here.

def afectar(request):
    if request.method == 'POST':
        usr = request.POST['idusu']
        amount = Decimal(request.POST['money'])
        usrname = request.POST['usuName']
        action = request.POST['abonar']
        if action == 'abonar':
            a = User.objects.get(id=usr)
            b = BillUser.objects.get(user=a)
            b.updateWallet(amount)
            row = Transaction(tipo = 'abonar', estatus='concluido', monto=amount, userOri=a, userDest=a.nombre, concepto="auto-abono", referencia="auto-abono")
            row.save()
            return render(request, 'menu.html', {"username": usrname, "iduser": usr})
        elif action == 'restar':
            a = User.objects.get(id=usr)
            b = BillUser.objects.get(user=a)
            if b.wallet < amount:
                return render(request, 'menu.html', {"username": usrname, "iduser": usr, "Error": True})
            b.updateWallet(amount*-1)
            row = Transaction(tipo = 'abonar', estatus='concluido', monto=amount, userOri=a, userDest=a.nombre, concepto="auto-retiro", referencia="auto-retiro")
            row.save()
            return render(request, 'menu.html', {"username": usrname, "iduser": usr})

def restar(request):
    if request.method == 'POST':
        abc = 1+1        
    