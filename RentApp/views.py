from django.shortcuts import render, redirect
from .models import Vehiculos, Clientes, Arriendos
from django.http import HttpResponse
from .forms import agregarVehiculoFormulario, agregarClienteFormulario, arrendarVehiculos

def home(req):
    return render(req, "home.html")

#! VEHICULOS
def agregar_vehiculos(req):
    form_add_vehiculo = agregarVehiculoFormulario(req.POST)
    if form_add_vehiculo.is_valid():
        print(form_add_vehiculo.cleaned_data)
        data = form_add_vehiculo.cleaned_data
        vehiculos = Vehiculos(
            patente = data["patente"],
            marca = data["marca"],
            tipo = data["tipo"],
            anio= data["anio"],
            arrendado = data['arrendado']
        ) 
        vehiculos.save()
        return redirect('Listar_Vehiculos')
    else:
        formulario_vehiculo = agregarVehiculoFormulario()

    context = {
        'form_agregar' : formulario_vehiculo,
    }
    return render(req, "agregar_vehiculos.html", context)


def listar_vehiculos(req):
    listar_vehiculos = Vehiculos.objects.all()
    context={'vehiculos_context':listar_vehiculos}
    return render(req, 'listar_vehiculos.html',context)
#! FIN VEHICULOS

#! CLIENTES
def agregar_cliente(req):
    form_add_cliente = agregarClienteFormulario(req.POST)
    if form_add_cliente.is_valid():
        print(form_add_cliente.cleaned_data)
        data = form_add_cliente.cleaned_data
        clientes = Clientes(
            nombre = data["nombre"],
            apellido = data["apellido"],
            rut = data["rut"],
            email= data["email"]
        ) 
        clientes.save()
        return redirect('Listar_Clientes')
    else:
        formulario_cliente = agregarClienteFormulario()

    context = {
        'form_agregar': formulario_cliente,
    }
    
    return render(req, 'agregar_clientes.html', context)


def listar_clientes(req):
    listar_query=Clientes.objects.all()
    context={'clientes_context':listar_query}
    return render(req, 'listar_clientes.html',context)
#! FIN CLIENTES

#! ARRIENDOS
def arrendar(req):
    form_add_arriendo = arrendarVehiculos(req.POST)
    if form_add_arriendo.is_valid():
        if req.method== 'POST':
            print(form_add_arriendo.cleaned_data)
            data = form_add_arriendo.cleaned_data

            arriendo = Arriendos(
                f_inicio = data["f_inicio"],
                f_fin = data["f_fin"],
                idCliente_id = data["idCliente"],
                idVehiculo_id = data["idVehiculo"]
                )
            arriendo.save()
            return redirect('Arrendados')
        else:
            return render(req, "arrendar.html",{"mensaje": "Formulario Invalido"})
    else:
        formulario_arriendo = arrendarVehiculos()
        
    context = {
        "form_arriendo": formulario_arriendo
    }

    return render(req, "arrendar.html", context)

def arrendados(req):
    sql_query = """
    select
        arr.id,
        cli.rut,
        cli.nombre,
        cli.apellido,
        cli.email,
        veh.tipo,
        veh.marca,
        veh.patente,
        arr.f_inicio,
        arr.f_fin
    from
        RentApp_clientes cli inner join RentApp_arriendos arr
        on cli.id = arr.idCliente_id inner join RentApp_vehiculos veh
        on veh.id = arr.idVehiculo_id;
    """
    listar_query = Arriendos.objects.raw(sql_query)
    #listar_query = Arriendos.objects.all()

    context = {'arriendos_context': listar_query,}
    return render(req, 'arrendados.html', context)
#! FIN ARRIENDOS