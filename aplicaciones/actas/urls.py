from django.urls import path
from aplicaciones.actas.views import listar, registrar

urlpatterns = [   
    path('listar/', listar),
    path('registrar/', registrar),
]