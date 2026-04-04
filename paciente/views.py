from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from .models import Paciente
from .forms import PacienteForm

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Paciente
# -------------------
# CADASTRAR
# -------------------
def cadastrar_paciente(request):
    form = PacienteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_pacientes')

    return render(request, 'paciente/cadastrar.html', {'form': form})


# -------------------
# LISTAR
# -------------------


def listar_pacientes(request):
    pacientes_list = Paciente.objects.all().order_by('-id')

    paginator = Paginator(pacientes_list, 25)  # 5 pacientes por página

    page_number = request.GET.get('page')
    pacientes = paginator.get_page(page_number)

    return render(request, 'paciente/listar.html', {
        'pacientes': pacientes
    })


# -------------------
# BUSCA EM TEMPO REAL (AJAX)
# -------------------
def buscar_pacientes(request):
    termo = request.GET.get('q', '')

    pacientes = Paciente.objects.filter(
        Q(nome__icontains=termo) |
        Q(cpf__icontains=termo)
    )

    data = list(pacientes.values('id', 'nome', 'cpf'))
    return JsonResponse(data, safe=False)


# -------------------
# EDITAR
# -------------------
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_pacientes')

    return render(request, 'paciente/editar.html', {
        'form': form,
        'paciente': paciente
    })


# -------------------
# DELETAR
# -------------------
def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')

    return render(request, 'paciente/confirmar_delete.html', {
        'paciente': paciente
    })