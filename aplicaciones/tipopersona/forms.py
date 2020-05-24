from django import forms
from .models import Tipopersona

class TipopersonaForm(forms.ModelForm):
    class Meta:
        model = Tipopersona
        fields = [
            'id',      
            'tip_per',
            'usuario',
            'opc_car',
            'fec_car',
            'hor_car',
            'elimina',
        ]
        labels = {
            'tip_per': 'Tipo de persona',
            'elimina': 'Estado', 
        }
        widgets = {
            'id': forms.HiddenInput(
                attrs = {             
                    'id': 'id'                   
                }
            ), 
            'tip_per': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'id': 'tipoPersona'
                }
            ),
            'usuario': forms.TextInput(
                attrs = {
                    'id':'usuario',
                    'value': 'elvin'
                }
            ),
            'opc_car': forms.TextInput(
                attrs = {
                    'id':'opc_car',
                    'value': 'I'
                }
            ),
            'fec_car': forms.TextInput(
                attrs = {
                    'id':'fec_car',
                    'value': '21-05-2020'
                }
            ),
            'hor_car': forms.TextInput(
                attrs = {
                    'id':'hot_car',
                    'value': '10:00'
                }
            ),
            'elimina': forms.Select(
                attrs= {
                    'class':'form-control',
                    'id': 'elimina'
                },
                choices=[
                    (True, 'ACTIVO'),
                    (False, 'INACTIVO'),               
                ]
            ),
        }
