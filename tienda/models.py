from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    class Rol(models.TextChoices):
        ESTUDIANTE = "estudiante", "Estudiante"
        PROFESOR = "profesor", "Profesor"

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    rol = models.CharField(max_length=20, choices=Rol.choices)

    def __str__(self):
        return f"{self.usuario.username} ({self.get_rol_display()})"


class PerfilEstudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_estudiante")
    nombre_completo = models.CharField(max_length=150)
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=30)
    nota_contabilidad = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota_programacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota_lenguaje_comunicacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre_completo


class PerfilProfesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_profesor")
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre_completo
