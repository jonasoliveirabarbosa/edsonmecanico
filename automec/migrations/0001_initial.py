# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=200)),
                ('placa', models.CharField(max_length=9)),
                ('ano', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200, blank=True)),
                ('telefone', models.CharField(max_length=15, blank=True)),
                ('celular', models.CharField(max_length=15, blank=True)),
                ('endereco', models.CharField(max_length=150, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPagamento', models.CharField(max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('parcelas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorMaoObra', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data', models.DateField(verbose_name='data')),
                ('km', models.IntegerField()),
                ('carro', models.ForeignKey(to='automec.Carro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='peca',
            name='servico',
            field=models.ForeignKey(to='automec.Servico'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='servico',
            field=models.ForeignKey(to='automec.Servico'),
        ),
        migrations.AddField(
            model_name='carro',
            name='dono',
            field=models.ForeignKey(to='automec.Cliente'),
        ),
    ]
