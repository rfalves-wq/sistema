from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),

    path('', views.listar_usuario, name='listar_usuario'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
path('dashboard/medico/', views.dashboard_medico, name='dashboard_medico'),
path('dashboard/enfermeiro/', views.dashboard_enfermeiro, name='dashboard_enfermeiro'),
path('dashboard/recepcionista/', views.dashboard_recepcionista, name='dashboard_recepcionista'),
path('dashboard/tecnico/', views.dashboard_tecnico, name='dashboard_tecnico'),
]