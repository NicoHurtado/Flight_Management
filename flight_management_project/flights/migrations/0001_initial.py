# Generated by Django 4.1.9 on 2023-05-26 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aerolinea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_aerolinea', models.CharField(max_length=2)),
                ('nombre_aerolinea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_aeropuerto', models.CharField(max_length=3)),
                ('nombre_aeropuerto', models.CharField(max_length=100)),
                ('nombre_ciudad', models.CharField(max_length=100)),
                ('id_ciudad', models.CharField(max_length=20)),
                ('nombre_pais', models.CharField(max_length=100)),
                ('id_pais', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pais_salida', models.CharField(max_length=20)),
                ('id_pais_llegada', models.CharField(max_length=20)),
                ('id_ciudad_salida', models.CharField(max_length=20)),
                ('id_ciudad_llegada', models.CharField(max_length=20)),
                ('fecha_salida', models.DateTimeField()),
                ('fecha_llegada', models.DateTimeField()),
                ('categoria_vuelo', models.CharField(max_length=100)),
                ('aerolinea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.aerolinea')),
                ('codigo_iata_llegada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llegada_tickets', to='flights.aeropuerto')),
                ('codigo_iata_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salida_tickets', to='flights.aeropuerto')),
            ],
        ),
    ]
