from django.shortcuts import render, get_object_or_404, redirect
from agendamento.models import Agendamento
from .models import Triagem

def fila_triagem(request):
    agendamentos = Agendamento.objects.filter(status='AGENDADO')
    return render(request, 'triagem/fila.html', {'agendamentos': agendamentos})


def realizar_triagem(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == 'POST':

        Triagem.objects.create(
            agendamento=agendamento,
            paciente=agendamento.paciente,
            pressao=request.POST['pressao'],
            temperatura=request.POST['temperatura'],
            batimento_cardiaco=request.POST['batimento'],
            saturacao=request.POST['saturacao'],
            queixa=request.POST['queixa'],
            prioridade=request.POST['prioridade'],
        )

        # muda status do agendamento
        agendamento.status = 'TRIADO'
        agendamento.save()

        return redirect('fila_triagem')

    return render(request, 'triagem/realizar.html', {'agendamento': agendamento})