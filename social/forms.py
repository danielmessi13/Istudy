from django import forms
from django.core.exceptions import ValidationError

from .models import *


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'tipo', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'tipo': forms.Select(attrs={'class': "form-control"}),
            'senha': forms.PasswordInput(attrs={'class': "form-control"})
        }

        def clean_email(self):
            data = self.cleaned_data['email']
            if len(Usuario.objects.filter(email = data)):
                raise ValidationError("Email já cadastrado! ")
            return data



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'tipo']
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
        fields = ["texto", "questao"]
        widgets = {
            'texto': forms.TextInput(attrs={'class': "form-control"}),
            'questao': forms.TextInput(attrs={'class': "form-control"}),
        }


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ["arquivo", "tipo"]
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': "form-control"}),
        }


class BuscaGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ["titulo"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': "form-control"})
        }


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['titulo','descricao']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': "form-control"}),
            'descricao': forms.TextInput(attrs={'class': "form-control"}),
        }
