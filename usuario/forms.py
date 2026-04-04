from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'tipo_usuario']
        widgets = {
            'password': forms.PasswordInput()
        }