# Generated by Django 3.2 on 2021-05-05 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='insumos'),
        ),
    ]