# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20151111_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='type',
            field=models.CharField(default=b'n', max_length=2, verbose_name='tipo', choices=[(b'n', 'Normal'), (b'i', 'Integrada'), (b'c', 'Cuadr\xe1tica'), (b'r', 'Original'), (b'd', 'Derivada'), (b'f', 'Filtrada'), (b'r', 'RR')]),
        ),
    ]
