# Generated by Django 3.2 on 2021-06-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_tarjeta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='cvv',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='fecha_vencimiento',
            field=models.IntegerField(default=None, null=True),
        ),
    ]