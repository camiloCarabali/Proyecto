from django import forms
from .models import Rol
from .models import Login

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']