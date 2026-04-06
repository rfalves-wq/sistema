from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from triagem.models import Triagem
from .models import AtendimentoMedico

# FILA DO MÉDICO
def fila_medico(request):
    triagens = Triagem.objects.filter(status='espera').order_by('-prioridade', '-data_triagem')

    return render(request, 'medico/fila.html', {
        'triagens': triagens
    })


# INICIAR ATENDIMENTO
def iniciar_atendimento(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)

    # muda status da triagem
    triagem.status = 'atendimento'
    triagem.save()

    # cria atendimento médico
    atendimento, created = AtendimentoMedico.objects.get_or_create(
        triagem=triagem
    )

    return redirect('atendimento_detalhe', atendimento.id)


# DETALHE DO ATENDIMENTO
def atendimento_detalhe(request, atendimento_id):
    atendimento = get_object_or_404(AtendimentoMedico, id=atendimento_id)

    if request.method == 'POST':
        atendimento.diagnostico = request.POST['diagnostico']
        atendimento.prescricao = request.POST['prescricao']
        atendimento.status = 'finalizado'
        atendimento.save()

        atendimento.triagem.status = 'finalizado'
        atendimento.triagem.save()

        return redirect('fila_medico')

    return render(request, 'medico/atendimento.html', {
        'atendimento': atendimento
    })