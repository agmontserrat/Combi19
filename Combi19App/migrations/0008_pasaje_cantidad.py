# Generated by Django 3.2 on 2021-06-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0007_merge_0006_alter_ruta_nombre_0006_pasaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasaje',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]