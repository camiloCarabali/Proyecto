# Generated by Django 3.1.2 on 2020-10-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0004_auto_20201027_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
