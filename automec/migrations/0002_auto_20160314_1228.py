# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('automec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='data',
            field=models.DateField(verbose_name='data', default=datetime.datetime(2016, 3, 14, 15, 28, 35, 159881, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(verbose_name='data', default=datetime.datetime(2016, 3, 14, 15, 28, 35, 158837, tzinfo=utc)),
        ),
    ]
