from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user>/<str:passw>', views.login, name='login'),
    path('cuentas/<int:cuenta_id>/', views.cuenta, name='cuenta'),]