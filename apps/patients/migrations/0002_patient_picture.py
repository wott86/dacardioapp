# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='picture',
            field=models.ImageField(null=True, upload_to=apps.patients.models.get_upload_path, blank=True),
        ),
    ]
