from django.db import models
from django.utils import timezone


# TODO: As classes 'TipoAlgumaCoisa' poderiam ser trocadas por só um atributo na classe né? (tipo a classe Reacao)


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.CASCADE, related_name='tipo')

    def __str__(self):
        return self.nome


class TipoUsuario(models.Model):
    TIPOS = (
        ('A', 'Aluno'),
        ('M', 'Mentor'),
    )

    tipo = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return self.tipo


class Anexo(models.Model):
    arquivo = models.FileField(upload_to='static')
    tipo_anexo = models.OneToOneField('TipoAnexo', on_delete=models.CASCADE, related_name='tipo')


class TipoAnexo(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo


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
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    data_reacao = models.DateField(default=timezone.now)
    tipo_reacao = models.CharField(max_length=30, choices=TIPOS)


class Mensagem(models.Model):
    emissor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emissor')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
