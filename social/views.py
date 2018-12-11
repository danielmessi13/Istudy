from django.shortcuts import render, redirect, get_object_or_404
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

    context = {
        "usuario": usuario_logado(request)
    }
    return render(request, 'home.html', context)



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

def perfil(request):
    return render(request, 'perfil.html')

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

def postar_editar(request, id):
    postagem = get_object_or_404(Postagem, id=id)
    if request.method == "POST":
        form = PostagemForm(request.POST, instance=postagem)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.usuario = usuario_logado(request)
            model_instance.save()
        else:
            print(form.errors)
    return redirect('home_logado')

def postar_deletar(request, id):
    postagem = Postagem.objects.get(id=id)
    postagem.delete()
    return redirect('home_logado')

def pesquisar_amigo(request):
    pesquisa =  request.GET['q']
    resultado  = Usuario.objects.filter(nome__contains = pesquisa).exclude(nome = "Joao")
    context = {
        "usuario": usuario_logado(request),
        "resultado": resultado,
        "pesquisa": pesquisa
    }
    return render(request, 'pesquisa.html', context )

def grupos(request):
    if request.method == "POST":
        form = BuscaGrupoForm(request.POST)
        print('entroiu')
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            titulo = request.POST['titulo']
            if titulo:
                print(titulo)

        else:
            print(form.errors)

    return render(request,'grupos.html', {"usuario": usuario_logado(request)})

def sair_grupo(request,id):

    usuario = usuario_logado(request)
    usuario.grupo_usuario.remove(Grupo.objects.get(id=id))
    return redirect('home_logado')


def check_logado(request):
    if request.session.get('usuario_logado'):
        return True
    return False

def usuario_logado(request):
     usuario = request.session.get('usuario_logado')
     return Usuario.objects.get(id=usuario["id"])