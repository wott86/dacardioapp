# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_patient_birth_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Nivel educativo', 'verbose_name_plural': 'Niveles educativos'},
        ),
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'H\xe1bito', 'verbose_name_plural': 'H\xe1bitos'},
        ),
        migrations.AlterModelOptions(
            name='occupation',
            options={'verbose_name': 'Ocupaci\xf3n', 'verbose_name_plural': 'Ocupaciones'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Paciente'},
        ),
        migrations.AlterModelOptions(
            name='relationshiptype',
            options={'verbose_name': 'Parentesco'},
        ),
        migrations.AlterModelOptions(
            name='ses',
            options={'verbose_name': 'Estatus socioecon\xf3mico'},
        ),
    ]
