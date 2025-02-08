from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        user = request.POST['usuario']
        passw = request.POST['contrasena']
        validar = login(user=user, passw=passw)
        if validar:
            return redirect('menu')
        else:
            return render(request, 'index.html', {"cuenta": user, "validar": validar})
    else:
        return render(request, 'index.html', {"validar": True})

def login(user, passw):
    if user == "admin" and passw == "1234":
        return True
    else:
        return False
    
def menu(request):
    return render(request, 'menu.html')