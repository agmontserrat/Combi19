# Generated by Django 3.2 on 2021-06-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0014_auto_20210626_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testeo',
            name='temperatura',
            field=models.FloatField(),
        ),
    ]
