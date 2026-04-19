from django.shortcuts import render, get_object_or_404, redirect
from triagem.models import Triagem
from .models import AtendimentoMedico

# FILA DO MÉDICO (NÃO SOME PACIENTE)
def fila_medico(request):
    triagens = Triagem.objects.filter(status='espera').order_by('-prioridade', '-data_triagem')

    return render(request, 'medico/fila.html', {
        'triagens': triagens
    })


# INICIAR ATENDIMENTO
def iniciar_atendimento(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)

    triagem.status = 'atendimento'
    triagem.save()

    atendimento, created = AtendimentoMedico.objects.get_or_create(
        triagem=triagem
    )

    return redirect('atendimento_detalhe', atendimento.id)


# ATENDIMENTO MÉDICO (DECISÃO FINAL)
def atendimento_detalhe(request, atendimento_id):
    atendimento = get_object_or_404(AtendimentoMedico, id=atendimento_id)

    if request.method == 'POST':
        acao = request.POST['acao']

        if acao == 'internacao':
            atendimento.triagem.status = 'internacao'

        elif acao == 'medicacao':
            atendimento.triagem.status = 'medicacao'

        elif acao == 'alta':
            atendimento.triagem.status = 'alta'
        elif acao == 'dispensar':
            atendimento.triagem.status = 'dispensado'

        atendimento.triagem.save()

        atendimento.diagnostico = request.POST.get('diagnostico', '')
        atendimento.prescricao = request.POST.get('prescricao', '')
        atendimento.status = 'finalizado'
        atendimento.save()

        return redirect('fila_medico')

    return render(request, 'medico/atendimento.html', {
    'atendimento': atendimento,
    'triagem': atendimento.triagem
})
    
    
from django.template.loader import render_to_string
from django.http import JsonResponse

def fila_medico_ajax(request):
    triagens = Triagem.objects.filter(status='espera').order_by('-data_triagem')

    html = render_to_string('medico/partials/_fila_lista.html', {
        'triagens': triagens
    })

    return JsonResponse({'html': html})