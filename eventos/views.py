from django.shortcuts import render
from .models import Evento
from .forms import EventoForm

def lista_eventos(request):
    eventos = Evento.objects.all().select_related('organizador')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  # Redirige a la lista de eventos después de guardar
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})