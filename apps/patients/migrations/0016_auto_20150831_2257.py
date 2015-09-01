# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150831_2220'),
        ('patients', '0015_auto_20150831_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('anomalies', models.ManyToManyField(to='records.Anomaly', verbose_name='anomal\xedas')),
            ],
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'historial de cambios', 'verbose_name_plural': 'historial de cambios'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='street_2',
        ),
        migrations.AddField(
            model_name='patient',
            name='chart_number',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name='n\xfamero de historia', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=128, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='education',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=128, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='history',
            name='modified_by',
            field=models.ForeignKey(related_name='history', verbose_name='modificado por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='history',
            name='modified_field',
            field=models.TextField(default=b'ALL', verbose_name='campo modificado'),
        ),
        migrations.AlterField(
            model_name='history',
            name='modified_new_value',
            field=models.TextField(default=b'', verbose_name='nuevo valor'),
        ),
        migrations.AlterField(
            model_name='history',
            name='modified_old_value',
            field=models.TextField(default=b'', verbose_name='antiguo valor'),
        ),
        migrations.AlterField(
            model_name='history',
            name='patient',
            field=models.ForeignKey(related_name='history', verbose_name='paciente', to='patients.Patient'),
        ),
        migrations.AlterField(
            model_name='occupation',
            name='name',
            field=models.CharField(max_length=128, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='occupation',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(verbose_name='fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_place',
            field=models.CharField(default=b'', max_length=256, verbose_name='lugar de nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dwelling',
            field=models.BooleanField(default=True, verbose_name='\xbfPosee vivienda?'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='education',
            field=models.ForeignKey(related_name='patients', verbose_name='educaci\xf3n', to='patients.Education'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_record',
            field=models.TextField(default=b'', verbose_name='antecedentes familiares', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='sexo', choices=[(b'M', 'Masculino'), (b'F', 'Femenino')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='habits',
            field=models.ManyToManyField(related_name='patients', verbose_name='h\xe1bitos personales', to='patients.Habit', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_card_number',
            field=models.CharField(max_length=32, verbose_name='c\xe9dula de identidad'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_card_prefix',
            field=models.CharField(default=b'V', max_length=1, verbose_name='prefijo de la c\xe9dula', choices=[(b'V', b'V'), (b'J', b'J'), (b'G', b'G'), (b'E', b'E')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(default=b's', max_length=1, verbose_name='estado civil', choices=[(b's', 'Soltero'), (b'm', 'Casado'), (b'w', 'Viudo'), (b'd', 'Divorciado')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.ForeignKey(related_name='patients', verbose_name='ocupaci\xf3n', to='patients.Occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='personal_record',
            field=models.TextField(default=b'', verbose_name='antecedentes patol\xf3gicos', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_home',
            field=models.CharField(default=b'', max_length=50, verbose_name='tel\xe9fono casa', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_mobile',
            field=models.CharField(default=b'', max_length=50, verbose_name='tel\xe9fono m\xf3vil', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_office',
            field=models.CharField(default=b'', max_length=50, verbose_name='tel\xe9fono oficina', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='picture',
            field=models.ImageField(upload_to=apps.patients.models.get_upload_path, null=True, verbose_name='foto', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='street',
            field=models.TextField(default=b'', verbose_name='direcci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='name',
            field=models.CharField(max_length=256, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='ses',
            name='name',
            field=models.CharField(max_length=128, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='ses',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(verbose_name='paciente', to='patients.Patient'),
        ),
    ]
