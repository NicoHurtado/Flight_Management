from django.shortcuts import render
from django.shortcuts import render  
from django.http import HttpResponse
from .models import tiquete  
from flights.models import Ticket

def ticket(request):
    vuelos = Ticket.objects.all()
    if request.method == 'POST':
        id_cliente = request.session.get('id_cliente')  # Obtener el ID del cliente desde la sesión
        id_vuelo = request.POST.get('id_vuelo')
        grupo = request.POST.get('grupo')
        asiento = request.POST.get('asiento')
        categoria_pasajero = request.POST.get('categoria_pasajero')
        equipaje_mano = request.POST.get('equipaje_mano')
        equipaje_bodega = request.POST.get('equipaje_bodega')

        # Crea un nuevo objeto de Ticket y guárdalo en la base de datos
        ticket = tiquete(
            id_cliente=id_cliente,
            id_vuelo=id_vuelo,
            grupo=grupo,
            asiento=asiento,
            categoria_pasajero=categoria_pasajero,
            equipaje_mano=equipaje_mano,
            equipaje_bodega=equipaje_bodega
        )
        ticket.save()

        return  HttpResponse('Ticket comprado exitosamente')


    id_cliente = request.session.get('id_cliente')
    return render(request, 'tiquete.html', {'id_cliente': id_cliente, 'vuelos': vuelos})



# Create your views here.
