# Generated by Django 3.2 on 2021-05-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210527_0105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chofer',
            options={'verbose_name_plural': 'Choferes'},
        ),
        migrations.AlterField(
            model_name='account',
            name='dni',
            field=models.IntegerField(unique=True, verbose_name='dni'),
        ),
    ]
