from django import forms
from django.core.exceptions import ValidationError

from .models import *


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'senha': forms.PasswordInput(attrs={'class': "form-control"})
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'tipo': forms.Select(attrs={'class': "form-control"}),
            'senha': forms.PasswordInput(attrs={'class': "form-control"}),
            'foto': forms.FileInput(attrs={'class': "form-control"})
        }


class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ["texto"]
        widgets = {
            'texto': forms.TextInput(attrs={'class': "form-control"}),
        }


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ["arquivo", "tipo"]
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': "form-control"}),
        }
