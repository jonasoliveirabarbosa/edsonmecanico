# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('automec', '0002_auto_20160314_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(verbose_name='data', default=datetime.datetime(2016, 3, 23, 22, 22, 53, 375776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(verbose_name='data', default=datetime.datetime(2016, 3, 23, 22, 22, 53, 375776, tzinfo=utc)),
        ),
    ]
