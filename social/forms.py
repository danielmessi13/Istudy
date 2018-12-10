from django import forms
from .models import *
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={ 'class': "form-control"}),
            'email': forms.TextInput(attrs={ 'class': "form-control"}),
            'tipo': forms.Select(attrs={ 'class': "form-control"}),
            'senha': forms.PasswordInput(attrs={ 'class': "form-control"})
        }
