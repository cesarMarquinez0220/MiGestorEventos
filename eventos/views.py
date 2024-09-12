# eventos/views.py

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear_evento.html'
    success_url = reverse_lazy('lista_eventos')

@method_decorator(login_required, name='dispatch')
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/editar_evento.html'
    success_url = reverse_lazy('lista_eventos')

class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/lista_organizadores.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'eventos/crear_organizador.html'
    success_url = reverse_lazy('lista_organizadores')
