from django.shortcuts import render
from .models import Aeropuerto, Aerolinea
from django.http import HttpResponse
from .models import Ticket 

def flight(request):
    # Aquí puedes agregar la lógica y acciones que deseas realizar en la página flight.html
    return render(request, 'flight.html')



from django.shortcuts import get_object_or_404

def registrar_vuelo(request):
    aerolineas = Aerolinea.objects.all()
    aeropuertos = Aeropuerto.objects.all()

    if request.method == 'POST':
        codigo_aerolinea = request.POST.get('codigo_aerolinea')
        codigo_iata_salida = request.POST.get('codigo_iata_salida')
        codigo_iata_llegada = request.POST.get('codigo_iata_llegada')

        aeropuerto_salida = get_object_or_404(Aeropuerto, codigo_aeropuerto=codigo_iata_salida)
        aeropuerto_llegada = get_object_or_404(Aeropuerto, codigo_aeropuerto=codigo_iata_llegada)

        aerolineas = Aerolinea.objects.filter(codigo_aerolinea=codigo_aerolinea)
        aerolineas_count = aerolineas.count()

        if aerolineas_count == 0:
            return HttpResponse('No se encontró una aerolínea con el código especificado')
        elif aerolineas_count > 1:
            return HttpResponse('Hay múltiples aerolíneas con el mismo código, se requiere un código único')
        
        aerolinea = aerolineas.first()

        ticket = Ticket(
            id_vuelo=request.POST.get('id_vuelo'),
            aerolinea=aerolinea,
            codigo_iata_salida=aeropuerto_salida,
            codigo_iata_llegada=aeropuerto_llegada,
            id_pais_salida=aeropuerto_salida.id_pais,
            id_pais_llegada=aeropuerto_llegada.id_pais,
            id_ciudad_salida=aeropuerto_salida.id_ciudad,
            id_ciudad_llegada=aeropuerto_llegada.id_ciudad,
            fecha_salida=request.POST.get('fecha_salida'),
            fecha_llegada=request.POST.get('fecha_llegada'),
            categoria_vuelo=request.POST.get('categoria_vuelo')
        )

        ticket.save()

        return HttpResponse('Registro de vuelo exitoso')

    return render(request, 'flight.html', {'aerolineas': aerolineas, 'aeropuertos': aeropuertos})












def registrar_aeropuerto(request):
    if request.method == 'POST':
        codigo_aeropuerto = request.POST.get('codigo_aeropuerto')
        nombre_aeropuerto = request.POST.get('nombre_aeropuerto')
        nombre_pais = request.POST.get('nombre_pais')
        id_pais = request.POST.get('id_pais')
        nombre_ciudad = request.POST.get('nombre_ciudad')
        id_ciudad = request.POST.get('id_ciudad')

        # Crear una instancia del modelo Aeropuerto
        aeropuerto = Aeropuerto(codigo_aeropuerto=codigo_aeropuerto, nombre_aeropuerto=nombre_aeropuerto, nombre_pais=nombre_pais, id_pais=id_pais, nombre_ciudad=nombre_ciudad, id_ciudad=id_ciudad)
        aeropuerto.save()


        return HttpResponse('Aeropuerto registrado exitosamente')

    return render(request, 'flight.html')

def registrar_aerolinea(request):
    if request.method == 'POST':
        codigo_aerolinea = request.POST.get('codigo_aerolinea')
        nombre_aerolinea = request.POST.get('nombre_aerolinea')

        # Crear una instancia del modelo Aerolinea
        aerolinea = Aerolinea(codigo_aerolinea=codigo_aerolinea, nombre_aerolinea=nombre_aerolinea)
        aerolinea.save()

        return HttpResponse('Aerolínea registrada exitosamente')

    return render(request, 'flight.html')
# Create your views here.

from ticket.models import tiquete

def ver_tickets(request):
    if request.method == 'POST':
        id_vuelo = request.POST.get('id_vuelo_t')
        tickets = tiquete.objects.filter(id_vuelo=id_vuelo)
        return render(request, 'flight.html', {'tickets': tickets})
    return render(request, 'flight.html')
