from django import forms
from .models import Arma

class ArmaForm(forms.ModelForm):    
    class Meta:Arma
        model = Arma      
        fields = [
            'id',      
            'login',
            'tipo',
            'nombre',
            'password',
            'Arma',
            'correo',
            'elimina',
        ]
        labels = {
            'id': 'Codigo',      
            'login': 'Login Arma',
            'tipo': 'Tipo Arma',
            'nombre': 'Nombre Arma',
            'password': 'Clave Arma',
            'Arma': 'Arma registro',
            'correo': 'Correo electronico',
            'elimina': 'Activo', 
        }
        widgets = {          
            'id': forms.HiddenInput(
                attrs = {             
                    'id': 'id'
                }
            ),      
            'login': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el login de Arma',
                    'id': 'login'
                }
            ),         
            'tipo': forms.Select(
                attrs= {
                    'class':'form-control', 
                    'id': 'tipo'
                },
                choices=TIPO_Arma),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre de Arma',
                    'id': 'nombre'
                }
            ),
            'password': forms.TextInput(
                attrs = {
                    'type': 'password',
                    'class':'form-control',
                    'placeholder': 'Ingrese el clave de Arma',
                    'id': 'password'
                }
            ),
            'Arma': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'correo': forms.EmailInput( 
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el correo de Arma',
                    'id': 'correo'
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
