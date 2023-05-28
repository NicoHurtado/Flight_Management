"""
URL configuration for flight_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views as customer_views
from ticket import views as ticket_views
from flights import views as flights_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', customer_views.signup, name='signup'),
    path('registrar/', customer_views.signup, name='signup'),
    path('login/', customer_views.login, name='login'),
    path('ticket/', ticket_views.ticket, name='ticket'),
    path('registrar_vuelo/', flights_views.registrar_vuelo, name='registrar_vuelo'),
    path('registrar_aeropuerto/', flights_views.registrar_aeropuerto, name='registrar_aeropuerto'),
    path('registrar_aerolinea/', flights_views.registrar_aerolinea, name='registrar_aerolinea'),
    path('ver_tickets/', flights_views.ver_tickets, name='ver_tickets'),
    
]
