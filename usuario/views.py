from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def sem_permissao():
    return HttpResponse("Acesso negado")


# LOGIN# LOGIN
def login_usuario(request):
    erro = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario:
            login(request, usuario)

            if usuario.tipo_usuario == 'administrador':
                return redirect('dashboard_admin')

            elif usuario.tipo_usuario == 'medico':
                return redirect('dashboard_medico')

            elif usuario.tipo_usuario == 'enfermeiro':
                return redirect('dashboard_enfermeiro')

            elif usuario.tipo_usuario == 'recepcionista':
                return redirect('dashboard_recepcionista')

            elif usuario.tipo_usuario == 'tecnico':
                return redirect('dashboard_tecnico')

        else:
            erro = 'Usuário ou senha inválidos'

    return render(request, 'usuario/login.html', {'erro': erro})


# LOGOUT
def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')


# LISTAR
@login_required
def listar_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar.html', {'usuarios': usuarios})


# CRIAR
@login_required
def criar_usuario(request):
    if request.user.tipo_usuario not in ['administrador', 'recepcionista']:
        return sem_permissao()

    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        return redirect('listar_usuario')

    return render(request, 'usuario/form.html', {'form': form})


# EDITAR
@login_required
def editar_usuario(request, id):
    if request.user.tipo_usuario not in ['administrador', 'enfermeiro']:
        return sem_permissao()

    usuario = get_object_or_404(Usuario, id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        usuario = form.save(commit=False)

        if form.cleaned_data.get('password'):
            usuario.set_password(form.cleaned_data['password'])

        usuario.save()
        return redirect('listar_usuario')

    return render(request, 'usuario/form.html', {'form': form})


# DELETAR
from django.views.decorators.http import require_POST

@require_POST
@login_required
def deletar_usuario(request, id):
    if request.user.tipo_usuario != 'administrador':
        return sem_permissao()

    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuario')


@login_required
def dashboard_admin(request):
    total = Usuario.objects.count()
    return render(request, 'usuario/dashboard_admin.html', {'total': total})


@login_required
def dashboard_medico(request):
    return render(request, 'usuario/dashboard_medico.html')


@login_required
def dashboard_enfermeiro(request):
    return render(request, 'usuario/dashboard_enfermeiro.html')


@login_required
def dashboard_recepcionista(request):
    return render(request, 'usuario/dashboard_recepcionista.html')


@login_required
def dashboard_tecnico(request):
    return render(request, 'usuario/dashboard_tecnico.html')