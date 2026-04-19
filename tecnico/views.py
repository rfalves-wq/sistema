from django.shortcuts import render, get_object_or_404, redirect
from triagem.models import Triagem
from .models import Medicacao
from django.contrib.auth.decorators import login_required


# DASHBOARD DO TÉCNICO
@login_required
def dashboard_tecnico(request):
    aguardando = Triagem.objects.filter(status='aguardando_medicacao').count()
    medicados = Triagem.objects.filter(status='medicado').count()

    return render(request, 'tecnico/dashboard.html', {
        'aguardando': aguardando,
        'medicados': medicados
    })


# FILA DE MEDICAÇÃO
@login_required
def fila_medicacao(request):
    triagens = Triagem.objects.filter(status='aguardando_medicacao')

    return render(request, 'tecnico/fila.html', {
        'triagens': triagens
    })


# APLICAR MEDICAÇÃO
@login_required
def aplicar_medicacao(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)

    if request.method == 'POST':
        medicamento = request.POST.get('medicamento')
        dose = request.POST.get('dose')
        observacao = request.POST.get('observacao')

        Medicacao.objects.create(
            triagem=triagem,
            tecnico=request.user,
            medicamento=medicamento,
            dose=dose,
            observacao=observacao
        )

        triagem.status = 'retorno_medico'
        triagem.save()

        return redirect('fila_medicacao')

    return render(request, 'tecnico/aplicar.html', {
        'triagem': triagem
    })


# HISTÓRICO
@login_required
def historico_medicacao(request):
    medicacoes = Medicacao.objects.all().order_by('-data_aplicacao')

    return render(request, 'tecnico/historico.html', {
        'medicacoes': medicacoes
    })