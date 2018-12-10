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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)