from django.db import models
from django.utils import timezone


# TODO: As classes 'TipoAlgumaCoisa' poderiam ser trocadas por só um atributo na classe né? (tipo a classe Reacao)


# Create your models here.
class Usuario(models.Model):
    TIPOS = (
        ('A', 'Aluno'),
        ('M', 'Mentor'),
    )

    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    tipo = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return self.nome


class Anexo(models.Model):
    arquivo = models.FileField(upload_to='static')
    tipo = models.CharField(max_length=30)


class Questao(models.Model):
    texto_questao = models.TextField()
    data_publicacao = models.DateField(default=timezone.now)


class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, related_name='alternativas', on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=30)
    correta = models.BooleanField(default=False)


class Comentario(models.Model):
    texto_comentario = models.TextField()


class Reacao(models.Model):
    TIPOS = (
        ('L', 'like'),
        ('D', 'dislike'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    postage = models.ForeignKey(Questao, on_delete=models.CASCADE)
    data_reacao = models.DateField(default=timezone.now)
    tipo_reacao = models.CharField(max_length=30, choices=TIPOS)


class Mensagem(models.Model):
    emissor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emissor')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
    texto_mensagem = models.TextField()
    lida = models.BooleanField(default=False)


class Grupo(models.Model):
    titulo = models.CharField(max_length=30)
    usuario = models.ManyToManyField(Usuario,related_name='usuarios')


class Postagem(models.Model):
    texto = models.TextField()
    data = models.DateField(timezone.now)
    usuario = models.ForeignKey(Usuario, related_name='postagens', on_delete=models.CASCADE)
