from django.shortcuts import render, redirect, get_object_or_404
from .models import Triagem
from paciente.models import Paciente

def fila_triagem(request):
    pacientes = Paciente.objects.all()
    return render(request, 'triagem/fila_triagem.html', {'pacientes': pacientes})

def realizar_triagem(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        pressao = request.POST['pressao']
        sintomas = request.POST['sintomas']
        classificacao = request.POST['classificacao']

        Triagem.objects.create(
            paciente=paciente,
            pressao=pressao,
            sintomas=sintomas,
            classificacao=classificacao
        )

        return redirect('fila_triagem')

    return render(request, 'triagem/form_triagem.html', {'paciente': paciente})