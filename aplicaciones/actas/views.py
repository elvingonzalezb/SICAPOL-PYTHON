from django.shortcuts import render
from .models import Actas
from .forms import ActasForm

def listar(request):
    actas = Actas.objects.all() #obtengo todos las actas
    contexto = {
        "actas": actas
    }
    return render(request, 'actas/listar_actas.html', contexto)

def registrar(request):
    form = ActasForm()
    contexto = {
        'form': form,
    }
    return render(request, 'actas/registrar_actas.html', contexto)

