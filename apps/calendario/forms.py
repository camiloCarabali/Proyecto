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


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('id', 'estado')


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['fecha', 'horaInicial', 'horaFinal', 'descripcion', 'usuario_id']
        labels = {
            'horaInicial': 'Hora de Inicio',
            'horaFinal': 'Hora de Finalizacion',
            'usuario_id': 'Usuario'
        }
        widgets = {
            'fecha': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horaInicial': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horaFinal': forms.TimeInput(
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
            'usuario_id': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
