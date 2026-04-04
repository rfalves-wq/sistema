from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    TIPO_USUARIO_CHOICES = [
        ('tecnico', 'Técnico'),
        ('enfermeiro', 'Enfermeiro'),
        ('recepcionista', 'Recepcionista'),
        ('medico', 'Médico'),
        ('administrador', 'Administrador'),
    ]

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES
    )

    def __str__(self):
        return self.username