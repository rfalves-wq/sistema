from django.db import models
from paciente.models import Paciente
from agendamento.models import Agendamento

class Triagem(models.Model):

    PRIORIDADE_CHOICES = [
        ('VERDE', 'Verde - Não urgente'),
        ('AMARELO', 'Amarelo - Pouco urgente'),
        ('VERMELHO', 'Vermelho - Emergência'),
    ]

    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    pressao = models.CharField(max_length=20)
    temperatura = models.FloatField()
    batimento_cardiaco = models.IntegerField()
    saturacao = models.IntegerField()

    queixa = models.TextField()

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='VERDE'
    )

    data_triagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Triagem - {self.paciente.nome}"