# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Record(models.Model):
    patient = models.ForeignKey('patients.Patient', verbose_name=_('paciente'))
    taken_by = models.ForeignKey('users.User', verbose_name=_('registrado por'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_(u'fecha de creación'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_(u'fecha de modificación'))

    def __unicode__(self):
        return u'%s (%s)' % (self.patient.full_name, self.created.isoformat())

    class Meta:
        verbose_name = _('registro')


class Point(models.Model):
    WAVES_TYPES = (
        (None, 'None'),
        ('p', 'p'),
        ('q', 'q'),
        ('r', 'r'),
        ('s', 's'),
        ('u', 'u')
    )

    record = models.ForeignKey('records.Record', verbose_name=_('registro'))
    x = models.FloatField(db_index=True)
    y = models.FloatField()
    wave = models.CharField(max_length=1, choices=WAVES_TYPES, null=True, blank=True, verbose_name=_('onda detectada'))
    flagged = models.BooleanField(default=False, verbose_name=_('marca'))

    def __unicode__(self):
        return u'%s - %s - %s' % (unicode(self.record), self.x, self.y)

    class Meta:
        verbose_name = _('punto')


class Anomaly(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('nombre'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'anomalía')


class Annotation(models.Model):
    point = models.ForeignKey('records.Point', verbose_name=_('punto'))
    annotation_type = models.CharField(max_length=45, verbose_name=_('tipo'))
    annotation = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name=_(u'fecha de creación'))
    created_by = models.ForeignKey('users.User', verbose_name=_('creado por'))
    anomaly = models.ForeignKey('records.Anomaly', null=True, blank=True, verbose_name=_(u'anomalía'))

    def __unicode__(self):
        return u'(%s) - %s - %s' % (unicode(self.point), self.created_by.full_name, self.created.isoformat())

    class Meta:
        verbose_name = _(u'anotación')
        verbose_name_plural = _('anotaciones')
