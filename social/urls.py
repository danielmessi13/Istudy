from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as v



urlpatterns = [
    path('', index, name='home'),
    path('postar', postar, name='postar'),
    path('postagem/<int:id>/editar', postar_editar, name='postagem_editar'),
    path('postagem/<int:id>/deletar', postar_deletar, name='postagem_deletar'),
    path('pesquisar/amigo', pesquisar_amigo, name='pesquisar_amigo'),
    path('convidar/<int:id>', convidar, name='convidar'),
    path('amigos/convites', convites, name='convites'),
    path('amigos/convites/aceitar/<int:id>', aceitar, name='aceitar'),
    path('cadastrar/', RegistrarUsuarioView.as_view(), name='cadastrar'),
    path('login/', v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='login.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
