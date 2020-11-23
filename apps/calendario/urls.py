from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear/', login_required(CrearActividad.as_view()), name='crear'),
    path('listar/', login_required(ListadoActividad.as_view()), name='listar'),
    path('editar/<int:pk>/', login_required(ActualizarActividad.as_view()), name='editar'),
    path('eliminar/<int:pk>/', login_required(EliminarActividad.as_view()), name='eliminar'),
    path('calendario/', login_required(Calendario.as_view()), name='calendario'),

    path('crearLogin/', CrearLogin.as_view(), name='crearLogin'),
    path('crearUsuario/', CrearUsuario.as_view(), name='crearUsuario')
]
