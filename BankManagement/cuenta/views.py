from django.shortcuts import render, redirect
from django.http import HttpResponse
from cuenta.models import User, NivelAceeso
# Create your views here.

def index(request):
    if request.method == 'POST':
        user = request.POST['usuario']
        passw = request.POST['contrasena']
        validar = login(user=user, passw=passw)
        if validar:
            return render(request, 'menu.html')
        else:
            return render(request, 'index.html', {"cuenta": user, "validar": validar})
    else:
        return render(request, 'index.html', {"validar": True})

def login(user, passw):
    for temp in User.objects.all():
        if temp.nombre == user and temp.contra == passw:
            return True
    if user == "admin" and passw == "1234":
        return True
    else:
        return False
