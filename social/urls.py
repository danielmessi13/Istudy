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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
