# Generated by Django 3.1.2 on 2020-11-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0007_auto_20201028_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='horaFinal',
            field=models.TimeField(verbose_name='HoraFinal'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='horaInicial',
            field=models.TimeField(verbose_name='HoraInicial'),
        ),
    ]
