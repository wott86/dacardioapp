# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20150425_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(default=b's', max_length=1, choices=[(b's', 'Soltero'), (b'm', 'Casado'), (b'w', 'Viudo'), (b'd', 'divorciado')]),
        ),
    ]
