from django import forms

from .models import *

class TipoDespesaForm(forms.ModelForm):

    class Meta:
        model = TipoDespesa
        fields = '__all__'
