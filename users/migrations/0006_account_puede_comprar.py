# Generated by Django 3.2 on 2021-06-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_account_reactivar'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='puede_comprar',
            field=models.BooleanField(default=True),
        ),
    ]