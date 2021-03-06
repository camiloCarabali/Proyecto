# Generated by Django 3.1.2 on 2020-10-26 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('password', models.CharField(max_length=200, verbose_name='Username')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Logins',
                'ordering': ['username'],
            },
        ),
        migrations.AlterModelOptions(
            name='rol',
            options={'ordering': ['nombre'], 'verbose_name': 'Rol', 'verbose_name_plural': 'Roles'},
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calendario.login')),
                ('rol_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calendario.rol')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['nombre'],
            },
        ),
    ]
