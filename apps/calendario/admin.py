from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class RolResources(resources.ModelResource):
    class Meta:
        model = Rol

class RolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ('id', 'nombre', 'estado')
    resources_class = RolResources

class LoginResources(resources.ModelResource):
    class Meta:
        model = Login

class LoginAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'username', 'password']
    list_display = ('id', 'username', 'password', 'estado')
    resources_class = LoginResources

class UsuarioResources(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'login_id', 'rol_id']
    list_display = ('nombres', 'apellidos', 'login_id', 'rol_id', 'estado')
    resources_class = UsuarioResources

class ActividadResources(resources.ModelResource):
    class Meta:
        model = Actividad

class ActividadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'fechaInicial', 'fechaFinal', 'descripcion', 'usuario_id']
    list_display = ('titulo','fechaInicial', 'fechaFinal', 'descripcion', 'estado')
    resources_class = ActividadResources


admin.site.register(Rol, RolAdmin)
admin.site.register(Login, LoginAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Actividad, ActividadAdmin)