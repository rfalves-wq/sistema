from django.db import models
from paciente.models import Paciente

class Agendamento(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    data = models.DateField()
    hora = models.TimeField()

    motivo = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('AGENDADO', 'Agendado'),
           
        ],
        default='AGENDADO'
    )
    tempo_espera = models.DurationField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora}"