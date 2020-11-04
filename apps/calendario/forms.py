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
        fields = '__all__'
        exclude = ('id', 'estado')
        labels = {
            'usuario_id': 'Usuario'
        }