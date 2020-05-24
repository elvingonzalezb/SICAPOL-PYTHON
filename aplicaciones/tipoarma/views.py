from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Tipoarma
from .forms import TipoarmaForm

class Inicio(TemplateView):
    template_name = 'tipoarma/index.html'

class ListarTipoArma(ListView):
    model               = Tipoarma
    template_name       = 'tipoarma/listar.html'
    context_object_name = 'tipoarmas'

    def get_queryset(self):
        return self.model.objects.filter(ind_activo=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['tipoarmas'] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, self.get_context_data())
    
class RegistrarTipoArma(CreateView):
    model         = Tipoarma
    form_class    = TipoarmaForm
    template_name = 'tipoarma/registrar.html'
    success_url   = reverse_lazy('listar_tipo_arma')

class ActualizarTipoArma(UpdateView):
    model         = Tipoarma
    form_class    = TipoarmaForm
    template_name = 'tipoarma/editar.html'
    success_url   = reverse_lazy('listar_tipo_arma')

class EliminarTipoArma(DeleteView):
    model         = Tipoarma

    def post(self, request, pk, *args, **kwargs):
        object = Tipoarma.objects.get(id = pk)
        object.ind_activo = False
        object.save()

        return redirect('listar_tipo_arma')