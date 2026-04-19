from django.db import models
from django.conf import settings
from triagem.models import Triagem

class Medicacao(models.Model):
    triagem = models.ForeignKey(Triagem, on_delete=models.CASCADE)

    tecnico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    medicamento = models.CharField(max_length=200)
    dose = models.CharField(max_length=100)

    observacao = models.TextField(blank=True, null=True)

    data_aplicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicamento} - {self.triagem.paciente.nome}"