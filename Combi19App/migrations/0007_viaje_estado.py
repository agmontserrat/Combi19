# Generated by Django 3.2 on 2021-05-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0006_auto_20210512_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]