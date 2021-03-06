from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', home, name='home_logado'),
    path('postar', postar, name='postar'),
    path('grupos', grupos, name='grupos'),
    path('sair_grupo/<int:id>', sair_grupo, name='sair_grupo'),
    path('entrar_grupo/<int:id>', entrar_grupo, name='entrar_grupo'),
    path('postagem/<int:id>/editar', postar_editar, name='postagem_editar'),
    path('postagem/<int:id>/deletar', postar_deletar, name='postagem_deletar'),
    path('pesquisar/amigo', pesquisar_amigo, name='pesquisar_amigo'),
    path('grupos/add_grupo', add_grupo, name='add_grupo'),
    path('convidar/<int:id>', convidar, name='convidar'),
    path('usuario/<int:id>/perfil', perfil, name='perfil'),
    path('amigos/convites', convites, name='convites'),
    path('amigos/convites/aceitar/<int:id>', aceitar, name='aceitar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
