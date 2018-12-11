from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *


# Create your views here.
def index(request):
    if check_logado(request): return redirect('home_logado')
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('home')
    else:
        form = CadastroForm()

    context = {
        "form": form,
        "btn_name": "Cadastrar"
    }
    return render(request, 'index.html', context)


def home(request):
    if check_logado(request):
        if request.method == "POST":
            form = BuscaGrupoForm(request.POST)
            if form.is_valid():
                if request.POST['titulo']:
                    print('entrou')
                    context = {
                        "busca_sair": usuario_logado(request).grupo_usuario.all().filter(titulo=request.POST['titulo']),
                        "busca": True,
                        "busca_entrar": Grupo.objects.all().exclude(usuarios=usuario_logado(request)),
                    }
                    return render(request, 'grupos.html', context)
            else:
                print(form.errors)

        form = BuscaGrupoForm()

        context = {
            "usuario": usuario_logado(request),
            "form": form,
            "btn_name": "Buscar",
        }

        return render(request, 'home.html', context)
    else:
        return index(request)


def login(request):
    collection = Usuario.objects.filter(email=request.POST['email'], senha=request.POST['senha'])
    if collection:
        usuario = collection[0]
        request.session["usuario_logado"] = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email
        }
        return redirect('home_logado')

    return redirect('home')


def logout(request):
    request.session["usuario_logado"] = None
    return redirect('home')


def postar(request):
    if request.method == "POST":
        form = PostagemForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.usuario = usuario_logado(request)
            model_instance.save()
            tipo = request.POST['tipo']
            if tipo:
                if tipo == 'P':
                    request.FILES['arquivo'] = request.FILES['pdf']
                elif tipo == 'I':
                    request.FILES['arquivo'] = request.FILES['imagem']
                anexo = AnexoForm(request.POST, request.FILES)
                if anexo.is_valid():
                    anexo_instance = anexo.save(commit=False)
                    anexo_instance.postagem = model_instance
                    anexo_instance.save()
                else:
                    print(anexo.errors)
        else:
            print(form.errors)
    return redirect('home_logado')


def grupos(request):
    if request.method == "POST":
        form = BuscaGrupoForm(request.POST)
        if form.is_valid():
            if request.POST['titulo']:
                print('entrou')
                context = {
                    "busca_sair": usuario_logado(request).grupo_usuario.all().filter(titulo=request.POST['titulo']),
                    "busca": True,
                    "busca_entrar": Grupo.objects.all().exclude(usuarios=usuario_logado(request)).filter(titulo=request.POST['titulo']),
                }
                return render(request, 'grupos.html', context)
        else:
            print(form.errors)

    form = BuscaGrupoForm()

    context = {
        "form": form,
        "btn_name": "Buscar",
        "usuario": usuario_logado(request),
        "grupos": Grupo.objects.all().exclude(usuarios=usuario_logado(request)),
    }

    return render(request, 'grupos.html', context)


def sair_grupo(request, id):
    usuario = usuario_logado(request)
    usuario.grupo_usuario.remove(Grupo.objects.get(id=id))
    return redirect('grupos')


def entrar_grupo(request, id):
    usuario = usuario_logado(request)
    usuario.grupo_usuario.add(Grupo.objects.get(id=id))
    return redirect('grupos')


def check_logado(request):
    if request.session.get('usuario_logado'):
        return True
    return False


def usuario_logado(request):
    usuario = request.session.get('usuario_logado')
    return Usuario.objects.get(id=usuario["id"])
