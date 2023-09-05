from django import forms

class agregarVehiculoFormulario(forms.Form):
    patente = forms.CharField(required=True)
    marca = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    anio = forms.IntegerField(required=True)
    arrendado = forms.BooleanField(required=False)

class agregarClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    rut = forms.CharField(required=True)
    email = forms.EmailField(required=True)

class arrendarVehiculos(forms.Form):
    f_inicio=forms.DateField(required=True)
    f_fin=forms.DateField(required=True)
    idVehiculo=forms.IntegerField(required=True)
    idCliente=forms.IntegerField(required=True)