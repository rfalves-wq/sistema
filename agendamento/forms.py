from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'status']

        widgets = {
            'data': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'text'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }