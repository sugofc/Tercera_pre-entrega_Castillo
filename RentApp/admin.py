from django.contrib import admin
from .models import Vehiculos, Clientes, Arriendos

#user: sugo / pass: 1234

# Register your models here.
admin.site.register(Vehiculos)
admin.site.register(Clientes)
admin.site.register(Arriendos)