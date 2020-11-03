from django.urls import path
from .views import *

urlpatterns = [
    #path('', Inicio.as_view, name = 'index2'),
    path('crear/', crearActividad, name = 'crear'),
    path('listar/', listadoActividad.as_view(), name = 'listar'),
    path('editar/<int:id>', editarActividad, name = 'editar'),
    path('eliminar/<int:id>', eliminarActividad, name = 'eliminar'),

    #path('crear_rol/', crearRol, name = 'crear_rol'),
    #path('listar_rol/', listarRol, name = 'listar_rol'),
    #path('editar_rol/<int:id>', editarRol, name = 'editar_rol'),
    #path('eliminar_rol/<int:id>', eliminarRol, name = 'eliminar_rol'),
    #path('crear_login/', crearLogin, name = 'crear_login'),
    #path('listar_login/', listarLogin, name = 'listar_login'),
    #path('editar_login/<int:id>', editarLogin, name = 'editar_login'),
    #path('eliminar_login/<int:id>', eliminarLogin, name = 'eliminar_login'),
    #path('crear_usuario/', crearUsuario, name = 'crear_usuario'),
    #path('listar_usuario/', listarUsuario, name='listar_usuario'),
    #path('editar_usuario/<int:id>', editarUsuario, name='editar_usuario'),
    #path('eliminar_usuario/<int:id>', eliminarUsuario, name='eliminar_usuario'),
    #path('crear_actividad/', crearActividad, name='crear_actividad'),
    #path('listar_actividad/', listarActividad, name='listar_actividad'),
    #path('editar_actividad/<int:id>', editarActividad, name='editar_actividad'),
    #path('eliminar_actividad/<int:id>', eliminarActividad, name='eliminar_actividad')

]
