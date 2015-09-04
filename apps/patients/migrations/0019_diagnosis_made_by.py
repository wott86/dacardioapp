# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0018_patient_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='made_by',
            field=models.ForeignKey(verbose_name='Hecho por', null=True, help_text='', to=settings.AUTH_USER_MODEL),
        ),
    ]
