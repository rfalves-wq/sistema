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
    
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data')
    return render(request, 'agendamento/listar.html', {'agendamentos': agendamentos})    

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