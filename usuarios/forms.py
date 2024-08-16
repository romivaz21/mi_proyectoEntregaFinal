from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Curso

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': _('Nombre de usuario'),
            'password1': _('Contraseña'),
            'password2': _('Confirmación de contraseña'),
        }
        help_texts = {
            'username': _('Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_'),
        }
        error_messages = {
            'password_mismatch': _('Las contraseñas no coinciden.'),
        }

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': _('mherrera')})
        self.fields['password1'].help_text = _(
            'Tu contraseña no puede ser demasiado similar a tu otra información personal.<br>'
            'Tu contraseña debe contener al menos 8 caracteres.<br>'
            'Tu contraseña no puede ser una contraseña de uso común.<br>'
            'Tu contraseña no puede ser completamente numérica.'
        )
        self.fields['password2'].help_text = _('Introduce la misma contraseña que antes, para verificación.')






class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'fecha']
