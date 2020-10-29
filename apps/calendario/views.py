from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import RolForm
from .forms import LoginForm
from .forms import UsuarioForm
from .models import Rol
from .models import Usuario

def Home(request):
    return render(request, 'index.html')

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
    rol.estado = False
    rol.save()
    return redirect('calendario:listar_rol')


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