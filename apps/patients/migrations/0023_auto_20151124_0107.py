# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_auto_20151124_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='id_card_number',
            field=models.IntegerField(null=True, verbose_name='c\xe9dula de identidad'),
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together=set([('id_card_prefix', 'id_card_number')]),
        ),
    ]
