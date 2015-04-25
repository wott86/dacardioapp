# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patient_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_card_number',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together=set([('id_card_prefix', 'id_card_number')]),
        ),
    ]
