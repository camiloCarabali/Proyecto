from django import forms
from .models import Rol
from .models import Login
from .models import Usuario
from .models import Actividad


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'login_id', 'rol_id']
        labels = {
            'login_id': 'Usuario',
            'rol_id': 'Rol'
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'login_id': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rol_id': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['titulo', 'fechaInicial','fechaFinal', 'descripcion', 'usuario_id']
        labels = {
            'titulo': 'Titulo',
            'usuario_id': 'Usuarios'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fechaInicial': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fechaFinal': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'descripcion'
                }
            ),
            'usuario_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }
