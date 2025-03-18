from django.urls import path

from . import views
from menu import views as menuvie

urlpatterns = [
    path('', views.index, name='index'),
    path('afectar', menuvie.afectar, name='afectar'),
    path('restar', menuvie.restar, name='restar'),
    ]