from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import *


class Inicio(TemplateView):
    template_name = 'index2.html'

class ListadoActividad(ListView):
    model = Actividad
    template_name = 'listar.html'
    context_object_name = 'actividades'
    queryset = Actividad.objects.filter(estado=True)
    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        actividades = Actividad.objects.filter(estado=True)
        if queryset:
            actividades = Actividad.objects.filter(
                Q(descripcion__icontains=queryset),
                estado=True
            ).distinct()
        paginator = Paginator(actividades, 5)
        page = request.GET.get('page')
        actividades = paginator.get_page(page)
        return render(request, self.template_name, {'actividades': actividades})

class ActualizarActividad(UpdateView):
    model = Actividad
    template_name = 'crear.html'
    form_class = ActividadForm
    success_url = reverse_lazy('listar')

class CrearActividad(CreateView):
    model = Actividad
    template_name = 'crear.html'
    form_class = ActividadForm
    success_url = reverse_lazy('listar')

class EliminarActividad(DeleteView):
    Model = Actividad
    success_url = reverse_lazy('listar')

def crearActividad(request):
    if request.method == 'POST':
        print(request.POST)
        actividad_form = ActividadForm(request.POST)
        if actividad_form.is_valid():
            actividad_form.save()
            return redirect('/calendario/listar')
    else:
        actividad_form = ActividadForm()
    return render(request, 'crear.html', {'actividad_form': actividad_form})

def listarAcividad(request):
    queryset = request.GET.get("buscar")
    actividades = Actividad.objects.filter(estado=True)
    if queryset:
        actividades = Actividad.objects.filter(
            Q(descripcion__icontains = queryset),
            estado = True
        ).distinct()

    paginator = Paginator(actividades, 5)
    page = request.GET.get('page')
    actividades = paginator.get_page(page)
    return render(request, 'listar.html', {'actividades':actividades})

def editarActividad(request, id):
    actividad_form = None
    error = None
    try:
        actividad = Actividad.objects.get(id=id)
        if request.method == 'GET':
            actividad_form = ActividadForm(instance=actividad)
        else:
            actividad_form = ActividadForm(request.POST, instance=actividad)
            if actividad_form.is_valid():
                actividad_form.save()
            return redirect('/calendario/listar')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'crear.html', {'actividad_form': actividad_form, 'error': error})

def eliminarActividad(request, id):
    actividad =Actividad.objects.get(id=id)
    if request.method == 'POST':
        actividad.estado = False
        actividad.save()
        return redirect('/calendario/listar')
    return render(request, 'eliminar.html', {'actividad': actividad})
'''
def crearRol(request):
    if request.method == 'POST':
        print(request.POST)
        rol_form = RolForm(request.POST)
        if rol_form.is_valid():
            rol_form.save()
            return redirect('index')
    else:
        rol_form = RolForm()
    return render(request, 'calendario/crear_rol.html', {'rol_form':rol_form})

def listarRol(request):
    roles = Rol.objects.filter(estado = True)
    return render(request, 'calendario/listar_rol.html', {'roles': roles})

def editarRol(request, id):
    rol_form = None
    error = None
    try:
        rol = Rol.objects.get(id=id)
        if request.method == 'GET':
            rol_form = RolForm(instance=rol)
        else:
            rol_form = RolForm(request.POST, instance=rol)
            if rol_form.is_valid():
                rol_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'calendario/crear_rol.html', {'rol_form': rol_form, 'error': error})

def eliminarRol(request, id):
    rol = Rol.objects.get(id = id)
    if request.method == 'POST':
        rol.estado = False
        rol.save()
        return redirect('calendario:listar_rol')
    return render(request, 'calendario/eliminar_rol.html', {'rol':rol})

def crearLogin(request):
    if request.method == 'POST':
        print(request.POST)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.save()
            return redirect('index')
    else:
        login_form = LoginForm()
    return render(request, 'calendario/crear_login.html', {'login_form':login_form})

def listarLogin(request):
    logins = Login.objects.filter(estado = True)
    return render(request, 'calendario/listar_login.html', {'logins':logins})


def editarLogin(request, id):
    login_form = None
    error = None
    try:
        login = Login.objects.get(id=id)
        if request.method == 'GET':
            login_form = LoginForm(instance=login)
        else:
            login_form = LoginForm(request.POST, instance=login)
            if login_form.is_valid():
                login_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'calendario/crear_login.html', {'login_form': login_form, 'error': error})

def eliminarLogin(request, id):
    login = Login.objects.get(id = id)
    if request.method == 'POST':
        login.estado = False
        login.save()
        return redirect('calendario:listar_login')
    return render(request, 'calendario/eliminar_login.html', {'login':login})

def crearUsuario(request):
    if request.method == 'POST':
        print(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('index')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'calendario/crear_usuario.html', {'usuario_form':usuario_form})

def listarUsuario(request):
    usuarios = Usuario.objects.filter(estado = True)
    return render(request, 'calendario/listar_usuario.html', {'usuarios': usuarios})

def editarUsuario(request, id):
    usuario_form = None
    error = None
    try:
        usuario = Usuario.objects.get(id=id)
        if request.method == 'GET':
            usuario_form = UsuarioForm(instance=usuario)
        else:
            usuario_form = UsuarioForm(request.POST, instance=usuario)
            if usuario_form.is_valid():
                usuario_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'calendario/crear_usuario.html', {'usuario_form': usuario_form, 'error': error})

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.estado = False
        usuario.save()
        return redirect('calendario:listar_usuario')
    return render(request, 'calendario/eliminar_usuario.html', {'usuario':usuario})

def crearActividad(request):
    if request.method == 'POST':
        print(request.POST)
        actividad_form = ActividadForm(request.POST)
        if actividad_form.is_valid():
            actividad_form.save()
            return redirect('index')
    else:
        actividad_form = ActividadForm()
    return render(request, 'calendario/crear_actividad.html', {'actividad_form':actividad_form})

def listarActividad(request):
    actividades = Actividad.objects.filter(estado = True)
    return render(request, 'calendario/listar_actividad.html', {'actividades': actividades})

def editarActividad(request, id):
    actividad_form = None
    error = None
    try:
        actividad = Actividad.objects.get(id=id)
        if request.method == 'GET':
            actividad_form = ActividadForm(instance=actividad)
        else:
            actividad_form = ActividadForm(request.POST, instance=actividad)
            if actividad_form.is_valid():
                actividad_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'calendario/crear_actividad.html', {'actividad_form': actividad_form, 'error': error})

def eliminarActividad(request, id):
    actividad =Actividad.objects.get(id=id)
    if request.method == 'POST':
        actividad.estado = False
        actividad.save()
        return redirect('calendario:listar_actividad')
    return render(request, 'calendario/eliminar_actividad.html', {'actividad': actividad})
    '''

