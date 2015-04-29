# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_patient_marital_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyrecord',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='familyrecord',
            name='relationship_type',
        ),
        migrations.RemoveField(
            model_name='personalrecord',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='family_record',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='patient',
            name='personal_record',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(default=b's', max_length=1, choices=[(b's', 'Soltero'), (b'm', 'Casado'), (b'w', 'Viudo'), (b'd', 'Divorciado')]),
        ),
        migrations.DeleteModel(
            name='FamilyRecord',
        ),
        migrations.DeleteModel(
            name='PersonalRecord',
        ),
    ]
