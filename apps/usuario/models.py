from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

'''
class UsuarioManager(BaseUserManager):
    def create_user(self, username, nombres, apellidos, password = None):
        usuario = self.model(username = username,
                             nombre = nombres,
                             apellidos = apellidos
                             )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, nombres, apellidos, password):
        usuario = self.create_user(
            username = username,
            nombres = nombres,
            apellidos = apellidos
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuarios(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellido', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


'''
