from django import forms
from .models import Actas

class ActasForm(forms.ModelForm):
    class Meta:
        model = Actas
        #fields = {'corre_act', 'cod_ccp',}
        fields = '__all__'
