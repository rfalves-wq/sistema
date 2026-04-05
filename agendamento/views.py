from django.shortcuts import render, redirect
from paciente.models import Paciente
from .models import Agendamento
from .forms import AgendamentoForm

def agendar(request):

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save(commit=False)

            paciente_id = request.POST.get('paciente_id')

            if paciente_id:
                paciente = Paciente.objects.filter(id=paciente_id).first()

                if paciente:
                    agendamento.paciente = paciente
                else:
                    return render(request, 'agendamento/agendar.html', {
                        'form': form,
                        'erro': 'Paciente inválido'
                    })
            else:
                return render(request, 'agendamento/agendar.html', {
                    'form': form,
                    'erro': 'Selecione um paciente'
                })

            agendamento.save()
            return redirect('listar_agendamentos')

    else:
        form = AgendamentoForm()

    return render(request, 'agendamento/agendar.html', {
        'form': form
    })
    
from datetime import date
from django.shortcuts import render
from .models import Agendamento


from datetime import date
from django.shortcuts import render
from django.utils import timezone
from .models import Agendamento

def listar_agendamentos(request):
    hoje = date.today()

    agendamentos = Agendamento.objects.filter(
        data=hoje
    ).order_by('-hora')

    total_hoje = agendamentos.count()

    # ⏱️ CALCULAR TEMPO DE ESPERA
    for ag in agendamentos:
        ag.tempo_espera = timezone.now() - ag.criado_em
        ag.tempo_espera_formatado = str(ag.tempo_espera).split(".")[0]

    return render(request, 'agendamento/listar.html', {
        'agendamentos': agendamentos,
        'total_hoje': total_hoje,
        'hoje': hoje
    })

from django.http import JsonResponse
from paciente.models import Paciente

def buscar_paciente(request):
    termo = request.GET.get('term', '')

    pacientes = Paciente.objects.filter(nome__icontains=termo)[:10]

    data = []

    for p in pacientes:
        data.append({
            'id': p.id,
            'nome': p.nome,
            'cpf': p.cpf
        })

    return JsonResponse(data, safe=False)


from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from .models import Agendamento

def mudar_status(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    novo_status = request.POST.get('status')

    # ✔️ se estiver sendo finalizado, salva tempo de espera
    if agendamento.status == 'AGENDADO' and novo_status != 'AGENDADO':
        agendamento.tempo_espera = timezone.now() - agendamento.criado_em

    agendamento.status = novo_status
    agendamento.save()

    return redirect('listar_agendamentos')


