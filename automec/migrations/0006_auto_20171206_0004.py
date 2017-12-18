# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('automec', '0005_auto_20170203_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='GastoSemanal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('diaVencimento', models.DecimalField(max_digits=2, decimal_places=0)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='GastoUnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('vencimento', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameModel(
            old_name='Gasto',
            new_name='GastoMensal',
        ),
        migrations.RenameField(
            model_name='gastomensal',
            old_name='periodicidade',
            new_name='vencimento',
        ),
        migrations.AlterField(
            model_name='custo',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 4, 27, 851120, tzinfo=utc), verbose_name=b'data'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 4, 27, 850497, tzinfo=utc), verbose_name=b'data'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 4, 27, 849246, tzinfo=utc), verbose_name=b'data'),
        ),
    ]
