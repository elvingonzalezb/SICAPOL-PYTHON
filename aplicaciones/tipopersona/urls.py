from django.urls import path
from aplicaciones.tipopersona.views import listar, registrar, editar, eliminar
from aplicaciones.tipopersona.class_view import TipopersonaList, TipopersonaCreate, TipopersonaUpdate, TipopersonaDelete


urlpatterns = [   
    path('listar/', TipopersonaList.as_view(), name='listar_tipopersona'),
    path('registrar/', TipopersonaCreate.as_view(), name='registrar_tipopersona'),
    path('editar/<int:pk>/', TipopersonaUpdate.as_view(), name='editar_tipopersona'),
    path('eliminar/<int:pk>/', TipopersonaDelete.as_view(), name='eliminar_tipopersona'),
]