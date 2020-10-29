from django.urls import path
from .views import crearRol, listarRol, editarRol, eliminarRol
from .views import crearLogin
from .views import crearUsuario, listarUsuario, editarUsuario, eliminarUsuario
from .views import crearActividad, listarActividad, editarActividad, eliminarActividad
urlpatterns = [
    path('crear_rol/', crearRol, name = 'crear_rol'),
    path('listar_rol/', listarRol, name = 'listar_rol'),
    path('editar_rol/<int:id>', editarRol, name = 'editar_rol'),
    path('eliminar_rol/<int:id>', eliminarRol, name = 'eliminar_rol'),
    path('crear_login/', crearLogin, name = 'crear_login'),
    path('crear_usuario/', crearUsuario, name = 'crear_usuario'),
    path('listar_usuario/', listarUsuario, name='listar_usuario'),
    path('editar_usuario/<int:id>', editarUsuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id>', eliminarUsuario, name='eliminar_usuario'),
    path('crear_actividad/', crearActividad, name='crear_actividad'),
    path('listar_actividad/', listarActividad, name='listar_actividad'),
    path('editar_actividad/<int:id>', editarActividad, name='editar_actividad'),
    path('eliminar_actividad/<int:id>', eliminarActividad, name='eliminar_actividad')
]
