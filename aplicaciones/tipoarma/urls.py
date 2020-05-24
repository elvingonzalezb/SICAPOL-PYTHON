from django.urls import path
from aplicaciones.tipoarma.views import ListarTipoArma, RegistrarTipoArma, ActualizarTipoArma, EliminarTipoArma

urlpatterns = [   
    path('listar/', ListarTipoArma.as_view(), name='listar_tipo_arma'),
    path('registrar/', RegistrarTipoArma.as_view(), name='registrar_tipo_arma'),
    path('editar/<int:pk>/', ActualizarTipoArma.as_view(), name='editar_tipo_arma'),
    path('eliminar/<int:pk>/', EliminarTipoArma.as_view(), name='eliminar_tipo_arma'),
]