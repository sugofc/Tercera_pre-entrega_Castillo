select
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