from django.urls import path
from . import views

urlpatterns = [
    path('fila/', views.fila_medico, name='fila_medico'),
    path('atender/<int:triagem_id>/', views.iniciar_atendimento, name='iniciar_atendimento'),
    path('atendimento/<int:atendimento_id>/', views.atendimento_detalhe, name='atendimento_detalhe'),
]