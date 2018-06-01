from django import forms

class ProprietarioForm(forms.Form):
    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=20)