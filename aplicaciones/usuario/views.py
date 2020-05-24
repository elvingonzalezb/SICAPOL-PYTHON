from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Usuario
from .forms import FormularioLogin, UsuarioForm

""" 
    dispatch() : valida la peticion y elije que metodo http se utilizo para la solicitud
    http_method_not_allowed(): retorna error cuando se utiliza un metodo http no soportado o definido
    options
"""
class Login(FormView):
    template_name = 'login.html'
    form_class    = FormularioLogin
    success_url   = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class inicio(TemplateView):
    """Clase que renderiza el index del sistema"""

    template_name = 'usuario/index.html'

class ListarUsuario(ListView):
    """Contiene la lógica para el listado de usuario.


    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str

    """
    model               = Usuario
    template_name       = 'usuario/listar.html'
    context_object_name = 'usuarios'
    def get_queryset(self):
        """Retorna una consulta a utilizarse en la clase.
        Esta funcion se encuentra en toda vista basada en  clase, se utiliza internamente por django para
        generar las consultas de a cuerdo a los valores que se definen en la clase, valores como MODEL,FORM_CLASS


        :return: una consulta
        :rtype: Queryset
        """

        
        return self.model.objects.filter(elimina=True)

    def get_context_data(self, **kwargs):
        """Retorna un contexto a enviar a template.
        Aquí definimos todas las variables que necesitamos enviar a nuestro template definido en TEMPLATE_NAME,
        se agregan a un diccionario general para poder ser enviados en la funcion RENDER.


        :return: un contexto
        :rtype: dict
        """


        contexto = {}
        contexto['usuarios'] = self.get_queryset()   #agregamos la consulta al contexto
        return contexto

    def get(self, request, *args, **kwargs):
        """Renderiza un template con un contexto dado.
        Se encarga de manejar toda petición enviada del navegador a Django a través del método GET
        del protocolo HTTP, en este caso renderiza un template definido en TEMPLATE_NAME junto con
        el contexto definido en GET_CONTEXT_DATA.


        :return: render
        :rtype: func
        """


        return render(request, self.template_name, self.get_context_data())
    

class RegistrarUsuario(CreateView):
    """Contiene la lógica para crear un usuario


    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL

    """

    model         = Usuario
    form_class    = UsuarioForm
    template_name = 'usuario/registrar.html'
    success_url   = reverse_lazy('listar_usuario')

class ActualizarUsuario(UpdateView):
    """Contiene la lógica para edición de un usuarios


    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL

    """
    model         = Usuario
    form_class    = UsuarioForm
    template_name = 'usuario/editar.html'
    success_url   = reverse_lazy('listar_usuario')

class EliminarUsuario(DeleteView):
    """Contiene la lógica para eliminar un usuario


    :parámetro model: Modelo a utilizarse
    :type model: Model

    """
    model         = Usuario

    def post(self, request, pk, *args, **kwargs):
        """Elimina logicamente un objeto.
        Se encarga de manejar las peticiones de tipo POST enviadas del navegador a Django.


        :parámetro pk: clave primaria
        :type pk: int
        :parámetro request: petición enviada del navegador
        :type request: request
        :return: redirect
        :rtype: func
        """

        object = Usuario.objects.get(id = pk)
        object.elimina = False
        object.save()
        return redirect('listar_usuario')
