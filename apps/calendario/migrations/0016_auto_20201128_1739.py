# Generated by Django 3.1.2 on 2020-11-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0015_auto_20201128_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='usuario_id',
            field=models.ManyToManyField(to='calendario.Usuario'),
        ),
    ]
