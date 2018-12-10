from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', home, name='home_logado'),
    path('postar', postar, name='postar'),
    path('grupos', grupos, name='grupos'),
]