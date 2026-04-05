from django.urls import path
from . import views

urlpatterns = [
    path('', views.fila_triagem, name='fila_triagem'),
    path('<int:id>/', views.realizar_triagem, name='realizar_triagem'),
]