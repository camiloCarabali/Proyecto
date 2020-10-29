from django.urls import path
from .views import crearRol, listarRol, editarRol, eliminarRol
from .views import crearLogin
from .views import crearUsuario
urlpatterns = [
    path('crear_rol/', crearRol, name = 'crear_rol'),
    path('listar_rol/', listarRol, name = 'listar_rol'),
    path('editar_rol/<int:id>', editarRol, name = 'editar_rol'),
    path('eliminar_rol/<int:id>', eliminarRol, name = 'eliminar_rol'),
    path('crear_login/', crearLogin, name = 'crear_login'),
    path('crear_usuario/', crearUsuario, name = 'crear_usuario')
]
