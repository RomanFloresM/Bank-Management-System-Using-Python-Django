from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request, user, passw):
    if user == "admin" and passw == "1234":
        return render(request, 'cuenta/dashboard.html')
    else:
        return HttpResponse("Usuario o contraseña incorrectos")
    
def menu(request):
    return render(request, 'menu.html')