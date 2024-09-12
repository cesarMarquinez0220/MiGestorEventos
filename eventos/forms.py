# eventos/forms.py
from django import forms
from .models import Evento, Organizador

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'organizador']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if 'Cancelado' in nombre:
            raise forms.ValidationError("El nombre del evento no puede contener la palabra 'Cancelado'.")
        return nombre
    
class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'email']