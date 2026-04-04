from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('listar/', views.listar_pacientes, name='listar_pacientes'),

    path('editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),

    path('buscar-pacientes/', views.buscar_pacientes, name='buscar_pacientes'),
]