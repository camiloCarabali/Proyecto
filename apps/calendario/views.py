from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import RolForm
from .forms import LoginForm
from .forms import UsuarioForm
from .forms import ActividadForm
from .models import Rol
from .models import Usuario
from .models import Actividad
from .models import Login

def Home(request):
    return render(request, 'index2.html')

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

