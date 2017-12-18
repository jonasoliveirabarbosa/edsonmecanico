# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('automec', '0004_auto_20160324_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('data', models.DateField(default=datetime.datetime(2017, 2, 3, 16, 6, 25, 309566, tzinfo=utc), verbose_name='data')),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('periodicidade', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 2, 3, 16, 6, 25, 308998, tzinfo=utc), verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 2, 3, 16, 6, 25, 307901, tzinfo=utc), verbose_name='data'),
        ),
        migrations.AddField(
            model_name='custo',
            name='servico',
            field=models.ForeignKey(to='automec.Servico'),
        ),
    ]
