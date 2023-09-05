from django.contrib import admin
from django.urls import path, include #! Se agrega include
from RentApp.views import * # Se importan todas las views de RentApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('RentApp/',include('RentApp.urls')), # Ira a buscar la ruta a la carpeta RentApp donde esta el aplicativo, y buscara urls.py
]
