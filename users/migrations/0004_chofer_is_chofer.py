# Generated by Django 3.2.2 on 2021-06-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_chofer_is_chofer'),
    ]

    operations = [
        migrations.AddField(
            model_name='chofer',
            name='is_chofer',
            field=models.BooleanField(default=True),
        ),
    ]