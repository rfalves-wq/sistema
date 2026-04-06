from django.db import models

# Create your models here.
from django.db import models
from triagem.models import Triagem

class AtendimentoMedico(models.Model):

    STATUS_CHOICES = [
        ('em_atendimento', 'Em atendimento'),
        ('finalizado', 'Finalizado'),
    ]

    triagem = models.OneToOneField(Triagem, on_delete=models.CASCADE)
    diagnostico = models.TextField(blank=True, null=True)
    prescricao = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='em_atendimento'
    )

    data_atendimento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Atendimento - {self.triagem.paciente.nome}"