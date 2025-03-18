from django.shortcuts import render, redirect
from django.http import HttpResponse
from cuenta.models import User, NivelAceeso
# Create your views here.

def index(request):
    if request.method == 'POST':
        user = request.POST['usuario']
        passw = request.POST['contrasena']
        validar = login(user=user, passw=passw)
        if validar != 0:
            return render(request, 'menu.html', {"username": user, "iduser": validar})
        else:
            return render(request, 'index.html', {"cuenta": user, "validar": validar})
    else:
        return render(request, 'index.html', {"validar": True})

def login(user, passw):
    for temp in User.objects.all():
        if temp.nombre == user and temp.contra == passw:
            return temp.id
    return 0

