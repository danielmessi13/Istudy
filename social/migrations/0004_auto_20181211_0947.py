# Generated by Django 2.1.3 on 2018-12-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20181211_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='imagem',
            field=models.ImageField(default='group.png', upload_to='grupos'),
        ),
    ]
