# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-12 17:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bacia_Hidrografica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Casos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao_iap', models.CharField(max_length=45)),
                ('classificacao_iva', models.CharField(max_length=45)),
                ('risco', models.CharField(max_length=1)),
                ('solucao_sugerida', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_coleta', models.DateField(verbose_name=b'Data da Coleta')),
            ],
        ),
        migrations.CreateModel(
            name='Coleta_Substancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_coletado', models.FloatField()),
                ('coleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Coleta')),
            ],
        ),
        migrations.CreateModel(
            name='Entorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variavel_entorno', models.CharField(max_length=45)),
                ('cor', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('data_emissao', models.DateField()),
                ('imagem', models.ImageField(upload_to=b'imagem/')),
                ('coleta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Coleta')),
            ],
        ),
        migrations.CreateModel(
            name='Monitoramento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_monitoramento', models.DateField(verbose_name=b'Data do Monitoramento')),
                ('classificacao_iap', models.CharField(max_length=45, null=True)),
                ('classificacao_iva', models.CharField(max_length=45, null=True)),
                ('risco', models.CharField(max_length=1, null=True)),
                ('solucao_sugerida', models.TextField(null=True)),
                ('coleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Coleta')),
                ('entorno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Entorno')),
                ('imagem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Ponto_Monitoramento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('dimensao', models.FloatField()),
                ('bacia_hidrografica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Bacia_Hidrografica')),
            ],
        ),
        migrations.CreateModel(
            name='Substancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11)),
                ('pergunta', models.CharField(max_length=20)),
                ('resposta', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='ponto_monitoramento',
            name='rio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Rio'),
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='ponto_monitoramento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='imagem',
            name='ponto_monitoramento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='coleta_substancia',
            name='substancia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Substancia'),
        ),
        migrations.AddField(
            model_name='coleta',
            name='ponto_monitoramento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Ponto_Monitoramento'),
        ),
        migrations.AddField(
            model_name='coleta',
            name='substancia',
            field=models.ManyToManyField(through='rbcapp.Coleta_Substancia', to='rbcapp.Substancia'),
        ),
        migrations.AddField(
            model_name='casos',
            name='entorno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbcapp.Entorno'),
        ),
    ]
