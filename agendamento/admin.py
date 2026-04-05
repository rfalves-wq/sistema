from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'paciente',
        'data',
        'hora',
        'status',
        'criado_em',
    )

    list_filter = (
        'status',
        'data',
    )

    search_fields = (
        'paciente__nome',
    )

    ordering = ('-data', '-hora')

    list_per_page = 20