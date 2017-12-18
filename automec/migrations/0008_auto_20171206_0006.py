# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('automec', '0007_auto_20171206_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custo',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 6, 37, 961959, tzinfo=utc), verbose_name=b'data'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 6, 37, 961303, tzinfo=utc), verbose_name=b'data'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 2, 6, 37, 959990, tzinfo=utc), verbose_name=b'data'),
        ),
    ]
