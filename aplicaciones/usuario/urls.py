from django.urls import path
from django.contrib.auth.decorators import login_required
from aplicaciones.usuario.views import ListarUsuario, RegistrarUsuario, ActualizarUsuario, EliminarUsuario


urlpatterns = [   
    path('listar/', login_required(ListarUsuario.as_view()), name='listar_usuario'),
    path('registrar/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('editar/<int:pk>/', login_required(ActualizarUsuario.as_view()), name='editar_usuario'),
    path('eliminar/<int:pk>/', login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),
]