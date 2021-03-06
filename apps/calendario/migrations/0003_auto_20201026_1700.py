# Generated by Django 3.1.2 on 2020-10-26 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_auto_20201026_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nombres'], 'verbose_name': 'usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='nombres',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='login_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.login'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.rol'),
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('horaInicial', models.TimeField(verbose_name='horaInicial')),
                ('horaFinal', models.TimeField(verbose_name='horaFinal')),
                ('descripcion', models.TextField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.usuario')),
            ],
        ),
    ]
