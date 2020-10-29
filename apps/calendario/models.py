from django.db import models

class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 200, blank= False, null=False)
    estado = models.BooleanField('Estado', default= True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Username', max_length=200, blank=False, null=False)
    password = models.CharField('Password', max_length=200, blank=False, null=False)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'
        ordering = ['username']

    def __str__(self):
        return self.username


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    login_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombres']

    def __str__(self):
        return self.nombres

class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=False, null=False)
    horaInicial = models.TimeField('horaInicial', blank=False, null=False)
    horaFinal = models.TimeField('horaFinal', blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'