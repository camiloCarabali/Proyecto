from django.db import models


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    estado = models.BooleanField('Estado', default=True)

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
        verbose_name = 'usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombres']

    def __str__(self):
        return self.nombres


class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, blank=False, null=True)
    fechaInicial = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=False, blank=True, null=True)
    fechaFinal = models.DateField('Fecha de Vencimiento', auto_now=False, auto_now_add=False, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=False)
    usuario_id = models.ManyToManyField(Usuario)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
