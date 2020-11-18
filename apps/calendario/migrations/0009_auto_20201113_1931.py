# Generated by Django 3.1.2 on 2020-11-14 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0008_auto_20201104_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['titulo'], 'verbose_name': 'Actividad', 'verbose_name_plural': 'Actividades'},
        ),
        migrations.AddField(
            model_name='actividad',
            name='titulo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]