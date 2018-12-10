# Generated by Django 2.0.9 on 2018-12-10 00:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_alternativa', models.CharField(max_length=30)),
                ('correta', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='static')),
                ('tipo', models.CharField(choices=[('I', 'imagem'), ('P', 'pdf')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_comentario', models.TextField()),
                ('data', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_mensagem', models.TextField()),
                ('lida', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data', models.DateField(verbose_name=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_questao', models.TextField()),
                ('data_publicacao', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_reacao', models.CharField(choices=[('L', 'like'), ('D', 'dislike')], max_length=30)),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Postagem')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('senha', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('A', 'Aluno'), ('M', 'Mentor')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='reacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='postagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagens', to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='emissor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emissor', to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='usuario',
            field=models.ManyToManyField(related_name='usuarios', to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='postagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagem', to='social.Postagem'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='social.Usuario'),
        ),
        migrations.AddField(
            model_name='alternativa',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='social.Questao'),
        ),
    ]