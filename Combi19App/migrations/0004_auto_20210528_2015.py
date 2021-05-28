# Generated by Django 3.2 on 2021-05-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0003_auto_20210527_0129'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='viaje',
            name='viaje_unico',
        ),
        migrations.AddField(
            model_name='lugar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='ciudades'),
        ),
        migrations.AlterUniqueTogether(
            name='viaje',
            unique_together={('fecha', 'combi')},
        ),
    ]
