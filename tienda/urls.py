from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registro/estudiante/", views.registro_estudiante, name="registro_estudiante"),
    path("registro/profesor/", views.registro_profesor, name="registro_profesor"),
    path("login/", views.login_unificado, name="login"),
    path("dashboard/", views.redirigir_dashboard, name="redirigir_dashboard"),
    path("dashboard/estudiante/", views.dashboard_estudiante, name="dashboard_estudiante"),
    path("dashboard/profesor/", views.dashboard_profesor, name="dashboard_profesor"),
    path("dashboard/profesor/estudiante/<int:estudiante_id>/", views.editar_estudiante, name="editar_estudiante"),
    path("logout/", views.cerrar_sesion, name="logout"),
]
