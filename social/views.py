from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def index(request):
    if check_logado(request): return redirect('home_logado')
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('home')
    else:
        form = CadastroForm()

    context = {
        "form": form,
        "btn_name": "Cadastrar"
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')


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
        else:
            print(form.errors)
    return redirect('home_logado')


def anexar(request):
    return redirect('home_logado')


def check_logado(request):
    if request.session.get('usuario_logado'):
        return True
    return False


def usuario_logado(request):
    usuario = request.session.get('usuario_logado')
    return Usuario.objects.get(id=usuario["id"])


def grupos(request):
    return render(request,'grupos',)
