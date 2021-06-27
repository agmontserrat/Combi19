# Generated by Django 3.2 on 2021-06-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0017_testeo_viaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='cancelado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de sintomas'),
        ),
    ]
