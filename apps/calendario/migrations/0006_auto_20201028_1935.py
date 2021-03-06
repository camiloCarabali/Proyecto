# Generated by Django 3.1.2 on 2020-10-29 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0005_rol_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='login',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
