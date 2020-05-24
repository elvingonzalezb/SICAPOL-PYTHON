from django import forms
from .models import Tipoarma

class TipoarmaForm(forms.ModelForm):    
    class Meta:
        model = Tipoarma
        fields = [
            'id',
            'nom_tipo_arma',
            'ind_activo',
        ]
        labels = {
            'nom_tipo_arma': 'Nombre tipo de arma',
        }
        widgets = {
            'id': forms.HiddenInput(
                attrs = {             
                    'id': 'id'                   
                }
            ), 
            'nom_tipo_arma': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'id': 'tipoArma'
                }
            ),
            'ind_activo': forms.Select(
                attrs= {
                    'class':'form-control',
                    'id': 'indActivo'
                },
                choices=[
                    (True, 'ACTIVO'),
                    (False, 'INACTIVO'),               
                ]
            ),
        }