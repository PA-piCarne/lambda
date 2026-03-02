from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    ActualizarEstudianteForm,
    LoginForm,
    RegistroEstudianteForm,
    RegistroProfesorForm,
)
from .models import Perfil, PerfilEstudiante, PerfilProfesor


def home(request):
    return render(request, "home.html")


def registro_estudiante(request):
    if request.method == "POST":
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user, rol=Perfil.Rol.ESTUDIANTE)
            PerfilEstudiante.objects.create(
                usuario=user,
                nombre_completo=form.cleaned_data["nombre_completo"],
                edad=form.cleaned_data["edad"],
                telefono=form.cleaned_data["telefono"],
            )
            messages.success(request, "Registro de estudiante exitoso.")
            return redirect("login")
    else:
        form = RegistroEstudianteForm()
    return render(request, "registro_estudiante.html", {"form": form})


def registro_profesor(request):
    if request.method == "POST":
        form = RegistroProfesorForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user, rol=Perfil.Rol.PROFESOR)
            PerfilProfesor.objects.create(
                usuario=user,
                nombre_completo=form.cleaned_data["nombre_completo"],
                telefono=form.cleaned_data["telefono"],
                especialidad=form.cleaned_data["especialidad"],
            )
            messages.success(request, "Registro de profesor exitoso.")
            return redirect("login")
    else:
        form = RegistroProfesorForm()
    return render(request, "registro_profesor.html", {"form": form})


def login_unificado(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("redirigir_dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def redirigir_dashboard(request):
    if request.user.perfil.rol == Perfil.Rol.PROFESOR:
        return redirect("dashboard_profesor")
    return redirect("dashboard_estudiante")


@login_required
def dashboard_estudiante(request):
    if request.user.perfil.rol != Perfil.Rol.ESTUDIANTE:
        return redirect("dashboard_profesor")
    perfil = request.user.perfil_estudiante
    return render(request, "dashboard_estudiante.html", {"perfil": perfil})


@login_required
def dashboard_profesor(request):
    if request.user.perfil.rol != Perfil.Rol.PROFESOR:
        return redirect("dashboard_estudiante")
    estudiantes = PerfilEstudiante.objects.select_related("usuario").all().order_by("nombre_completo")
    return render(request, "dashboard_profesor.html", {"estudiantes": estudiantes})


@login_required
def editar_estudiante(request, estudiante_id):
    if request.user.perfil.rol != Perfil.Rol.PROFESOR:
        return redirect("dashboard_estudiante")

    estudiante = get_object_or_404(PerfilEstudiante, id=estudiante_id)
    if request.method == "POST":
        form = ActualizarEstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Información del estudiante actualizada correctamente.")
            return redirect("dashboard_profesor")
    else:
        form = ActualizarEstudianteForm(instance=estudiante)

    return render(request, "editar_estudiante.html", {"form": form, "estudiante": estudiante})


def cerrar_sesion(request):
    logout(request)
    return redirect("home")
