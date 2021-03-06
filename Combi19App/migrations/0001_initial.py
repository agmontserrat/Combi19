# Generated by Django 3.2 on 2021-06-05 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='insumos')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Lugar')),
                ('provincia', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo_postal', models.IntegerField(blank=True, null=True, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='ciudades')),
            ],
            options={
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('km', models.IntegerField()),
                ('destino', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='Combi19App.lugar')),
                ('origen', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='Combi19App.lugar')),
            ],
            options={
                'unique_together': {('origen', 'destino')},
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10, unique=True)),
                ('capacidad', models.IntegerField()),
                ('modelo', models.IntegerField()),
                ('chofer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.chofer')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('combi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Combi19App.vehiculo')),
                ('comentarios', models.ManyToManyField(blank=True, default=None, to='Combi19App.Comentario')),
                ('insumo', models.ManyToManyField(blank=True, default=None, to='Combi19App.Insumo')),
                ('pasajeros', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
                ('ruta', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Combi19App.ruta')),
            ],
            options={
                'unique_together': {('fecha', 'combi')},
            },
        ),
    ]
