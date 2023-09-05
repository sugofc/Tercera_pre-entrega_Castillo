from django.urls import path
from RentApp.views import * # Importa las Rendericiones
from . import views

urlpatterns = [
    path('', home, name='Home'),
    path('agregar_vehiculos/', agregar_vehiculos, name='Agregar_Vehiculos'),
    path('listar_vehiculos/', listar_vehiculos, name='Listar_Vehiculos'),
    path('agregar_clientes/', agregar_cliente, name='Agregar_Clientes'),
    path('listar_clientes/', listar_clientes, name='Listar_Clientes'),
    path('arrendar/', arrendar, name='Arrendar'),
    path('arrendados/', views.arrendados, name='Arrendados'),
]