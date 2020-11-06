from django.urls import path
from .views import *

urlpatterns = [
    path('crear/', crearActividad, name = 'crear'),
    path('listar/', ListadoActividad.as_view(), name = 'listar'),
    path('editar/<int:id>', editarActividad, name = 'editar'),
    path('eliminar/<int:id>', eliminarActividad, name = 'eliminar'),

]
