# Generated by Django 3.2 on 2021-06-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Combi19App', '0013_testeo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testeo',
            name='dificultad_respiratoria',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='dolor_cabeza',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='dolor_garganta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='dolor_muscular',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='perdida_gusto_olfato',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='tos',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='testeo',
            name='vomitos_diarrea',
            field=models.BooleanField(),
        ),
    ]
