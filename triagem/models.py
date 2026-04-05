from django.db import models

class Triagem(models.Model):

    paciente = models.ForeignKey(
        'paciente.Paciente',
        on_delete=models.CASCADE
    )

    pressao = models.CharField(max_length=20)
    sintomas = models.TextField()

    STATUS_CHOICES = [
        ('vermelho', 'Emergência'),
        ('laranja', 'Muito urgente'),
        ('amarelo', 'Urgente'),
        ('verde', 'Pouco urgente'),
        ('azul', 'Não urgente'),
    ]

    classificacao = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    data_triagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.classificacao}"