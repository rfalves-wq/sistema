from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar, name='agendar'),
    path('buscar-paciente/', views.buscar_paciente, name='buscar_paciente'),
        path('listar/', views.listar_agendamentos, name='listar_agendamentos'),
]