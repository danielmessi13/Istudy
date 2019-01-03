from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from usuarios.forms import *
from social.models import *
from django.contrib.auth.models import User
from django.views.generic.base import View


class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create_user(username=dados_form['nome'],
                                          email=dados_form['email'],
                                          password=dados_form['senha'])

            Usuario.objects.create(telefone=dados_form['telefone'],
                                           nome_empresa=dados_form['nome_empresa'],
                                           usuario=usuario)

            return redirect('login')

        return render(request, self.template_name, {'form': form})
