# Generated by Django 3.2 on 2021-05-13 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chofer',
            options={'permissions': (('es_chofer', 'Es un chofer'),), 'verbose_name_plural': 'Choferes'},
        ),
    ]