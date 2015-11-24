# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_auto_20150904_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-id'], 'verbose_name': 'paciente'},
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id_card_number',
        ),
    ]
