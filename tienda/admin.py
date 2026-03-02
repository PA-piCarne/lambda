from django.contrib import admin

from .models import Perfil, PerfilEstudiante, PerfilProfesor


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "rol")
    search_fields = ("usuario__username", "usuario__email")
    list_filter = ("rol",)


@admin.register(PerfilEstudiante)
class PerfilEstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_completo",
        "usuario",
        "edad",
        "nota_contabilidad",
        "nota_programacion",
        "nota_lenguaje_comunicacion",
    )
    search_fields = ("nombre_completo", "usuario__username", "usuario__email")


@admin.register(PerfilProfesor)
class PerfilProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "usuario", "especialidad", "telefono")
    search_fields = ("nombre_completo", "usuario__username", "usuario__email", "especialidad")
