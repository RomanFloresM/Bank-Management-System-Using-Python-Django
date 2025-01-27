from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("login para acceder")

def login(request, user, passw):
    if user == "admin" and passw == "1234":
        return render(request, 'cuenta/dashboard.html')
    else:
        return HttpResponse("Usuario o contraseña incorrectos")