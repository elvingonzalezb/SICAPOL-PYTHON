from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


TIPO_USUARIO = [
    ('ADMINISTRADOR', 'ADMINISTRADOR'),
    ('SUPERVISOR', 'SUPERVISOR'),
    ('OPERADOR', 'OPERADOR'),
]

class UsuarioForm(forms.ModelForm):    
    class Meta:
        model = Usuario      
        fields = [
            'id',      
            'login',
            'tipo',
            'nombre',
            'password',
            'usuario',
            'correo',
            'elimina',
        ]
        labels = {
            'id': 'Codigo',      
            'login': 'Login usuario',
            'tipo': 'Tipo usuario',
            'nombre': 'Nombre usuario',
            'password': 'Clave usuario',
            'usuario': 'Usuario registro',
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
                    'placeholder': 'Ingrese el login de usuario',
                    'id': 'login'
                }
            ),         
            'tipo': forms.Select(
                attrs= {
                    'class':'form-control', 
                    'id': 'tipo'
                },
                choices=TIPO_USUARIO),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre de usuario',
                    'id': 'nombre'
                }
            ),
            'password': forms.TextInput(
                attrs = {
                    'type': 'password',
                    'class':'form-control',
                    'placeholder': 'Ingrese el clave de usuario',
                    'id': 'password'
                }
            ),
            'usuario': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'correo': forms.EmailInput( 
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el correo de usuario',
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
