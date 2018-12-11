from django.db import models
from django.utils import timezone


# Create your models here.
class Usuario(models.Model):
    TIPOS = (
        ('A', 'Aluno'),
        ('M', 'Mentor'),
    )

    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    foto = models.ImageField(null=True)
    amigos = models.ManyToManyField('Usuario', related_name='amigos_usuario')

    def convidar(self, perfil_convidado):
        Convite.objects.create(convidado=perfil_convidado, solicitante=self)

    def timeline(self):
        pass

    def __str__(self):
        return self.nome


class Anexo(models.Model):
    TIPOS = (
        ('I', 'imagem'),
        ('P', 'pdf'),
    )

    arquivo = models.FileField(upload_to='anexos')
    tipo = models.CharField(max_length=30, choices=TIPOS)
    postagem = models.ForeignKey('Postagem', related_name='anexo_postagem', on_delete=models.CASCADE, null=True,
                                 blank=True)


class Questao(models.Model):
    texto_questao = models.TextField()
    data_publicacao = models.DateField(default=timezone.now)


class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, related_name='alternativas', on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=30)
    correta = models.BooleanField(default=False)


class Comentario(models.Model):
    texto_comentario = models.TextField()
    data = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_comentario')
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='postagem_comentario')


class Reacao(models.Model):
    TIPOS = (
        ('L', 'like'),
        ('D', 'dislike'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE)
    tipo_reacao = models.CharField(max_length=30, choices=TIPOS)


class Mensagem(models.Model):
    emissor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emissor')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
    texto_mensagem = models.TextField()
    lida = models.BooleanField(default=False)


class Grupo(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    criador = models.ForeignKey(Usuario,related_name='criador',on_delete=models.CASCADE, default=1)
    usuarios = models.ManyToManyField(Usuario, related_name='grupo_usuario')
    img = models.FileField(upload_to='grupos')

    def __str__(self):
        return self.titulo


class Postagem(models.Model):
    texto = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, related_name='usuario_postagem', on_delete=models.CASCADE)
    questao = models.OneToOneField(Questao, related_name='questao_postagem', on_delete=models.CASCADE, null=True,
                                   blank=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.texto


class Convite(models.Model):
    convidado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='convites_recebidos')
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='convites_feitos')

    def aceitar(self):
        self.convidado.amigos.add(self.solicitante)
        self.solicitante.amigos.add(self.convidado)
        self.delete()
