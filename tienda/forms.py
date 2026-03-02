from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import PerfilEstudiante


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class RegistroBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class RegistroEstudianteForm(RegistroBaseForm):
    nombre_completo = forms.CharField(max_length=150)
    edad = forms.IntegerField(min_value=1)
    telefono = forms.CharField(max_length=30)


class RegistroProfesorForm(RegistroBaseForm):
    nombre_completo = forms.CharField(max_length=150)
    telefono = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=120)


class ActualizarEstudianteForm(forms.ModelForm):
    class Meta:
        model = PerfilEstudiante
        fields = [
            "nombre_completo",
            "edad",
            "telefono",
            "nota_contabilidad",
            "nota_programacion",
            "nota_lenguaje_comunicacion",
        ]
