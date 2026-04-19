from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_tecnico, name='dashboard_tecnico'),
    path('fila/', views.fila_medicacao, name='fila_medicacao'),
    path('aplicar/<int:triagem_id>/', views.aplicar_medicacao, name='aplicar_medicacao'),
    path('historico/', views.historico_medicacao, name='historico_medicacao'),
]