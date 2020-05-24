from django.shortcuts import render, redirect
from .models import Tipopersona
from .forms import TipopersonaForm

def listar(request):
    tipopersona = Tipopersona.objects.all()
    oTipoPersona = {
        'tipopersonas': tipopersona
    }
    return render(request, 'tipopersona/listar.html', oTipoPersona)

def registrar(request):
    if request.method == 'GET':
        form = TipopersonaForm()
        oTipoPersona = {
            'form': form
        }        
    else:
        form = TipopersonaForm(request.POST)        
        oTipoPersona = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listar_tipopersona')
    return render(request, 'tipopersona/registrar.html', oTipoPersona)

def editar(request, id):
    tipopersona = Tipopersona.objects.get(id= id)
    if request.method == 'GET':
        form = TipopersonaForm(instance=tipopersona)
        oTipoPersona = {
            'form': form
        }
    else:
        form = TipopersonaForm(request.POST, instance=tipopersona)
        oTipoPersona = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listar_tipopersona')
    return render(request, 'tipopersona/registrar.html', oTipoPersona)

def eliminar(request, id):
    tipopersona = Tipopersona.objects.get(id = id)
    tipopersona.delete()
    return redirect('listar_tipopersona')
