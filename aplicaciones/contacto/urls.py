from django.urls import path
from aplicaciones.contacto.views import index

urlpatterns = [   
    path('listar/', index),
]