from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tipopersona
from .forms import TipopersonaForm

""" 
class View()
funciona con puras funciones
el contexto que se envia con render debe ser un diccionario
def get_context_data(self):
    context = {}
    context[queryset] = slf.get_queryset()
    return context

dispatch : verifica el metodo de la solicitud http
http_not_allowed
    def get(self, request, argumentos, clavesdeargumentos)
        return render(request, )
get tiene un metodo que devuelve por defecto, solo le indicamos que modelo
 def get_queryset(self): 
  return self.model.objects.all()

    def get_templates_names()
      return render(request,  self.get_templates_names(), self.get_context_data())

def post(self, request, argumentos, clavesdeargumentos)"""

class TipopersonaList(ListView):
    model         = Tipopersona
    template_name = 'tipopersona/listar.html'


class TipopersonaCreate(CreateView):
    model         = Tipopersona
    form_class    = TipopersonaForm
    template_name = 'tipopersona/registrar.html'
    success_url   = reverse_lazy('listar_tipopersona')

class TipopersonaUpdate(UpdateView):
    model         = Tipopersona
    form_class    = TipopersonaForm
    template_name = 'tipopersona/registrar.html'
    success_url   = reverse_lazy('listar_tipopersona')

class TipopersonaDelete(DeleteView):
    model         = Tipopersona
    template_name = 'tipopersona/verificacion.html'
    success_url   = reverse_lazy('listar_tipopersona')