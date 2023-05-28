from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import Usuario  # Importa el modelo Usuario desde tu aplicación
from django.contrib import messages 


def login(request):
    if request.method == 'POST':
        Name = request.POST.get('nombre')    
        id = request.POST.get('identificacion')

        try:
            usuario = Usuario.objects.get(nombre=Name)
        except Usuario.DoesNotExist:
            # Si el usuario no existe, mostrar un mensaje de error
            return render(request, 'inicio.html', {'error': 'El usuario no existe'})

        if id == usuario.identificacion:
            request.session['id_cliente'] = usuario.identificacion
            # Si la identificación coincide, redirigir a la página deseada
            return redirect('ticket')

        # Si la contraseña es incorrecta, mostrar un mensaje de error
        return render(request, 'inicio.html', {'error': 'Contraseña incorrecta'})
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        identificacion = request.POST.get('id')
        edad = request.POST.get('edad')
        email = request.POST.get('email')

        # Crea un nuevo objeto de Usuario y guárdalo en la base de datos
        usuario = Usuario(nombre=nombre, identificacion=identificacion, edad=edad, email=email)
        usuario.save()

        return HttpResponse('Registro exitoso')  # Puedes redirigir a otra página o mostrar un mensaje de éxito
    else:
        return render(request,'usuario.html')
