# Generated by Django 3.2 on 2021-06-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0019_alter_viaje_cancelado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='estado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
