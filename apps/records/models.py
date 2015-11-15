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


class Channel(models.Model):
    CHANNEL_TYPES = (
        ('n', _('Normal')),
        ('i', _('Integrada')),
        ('c', _(u'Cuadrática')),
        ('r', _('Original')),
        ('d', _('Derivada')),
        ('f', _('Filtrada')),
        ('r', _('RR'))
    )

    record = models.ForeignKey(Record, verbose_name=_('registro'), related_name='channels')
    type = models.CharField(max_length=2, default='n', choices=CHANNEL_TYPES, verbose_name=_('tipo'))
    name = models.CharField(max_length=50, blank=True, default='', verbose_name=_('nombre'))
    description = models.TextField(blank=True, default='', verbose_name=_(u'descripción'))

    class Meta:
        verbose_name = _('canal')
        verbose_name_plural = _('canales')

    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.record), self.get_type_display(), self.name)

    def get_media_points(self, initial_time, final_time, interval):
        y = []
        while initial_time < final_time:
            points = self.points.filter(x__gte=initial_time, x__lte=initial_time+interval).order_by('x')
            count = points.count()
            y.append(sum([p.y for p in points])/count if count > 0 else 0)
            initial_time += interval
        return range(1, len(y) + 1), y



class Point(models.Model):
    WAVES_TYPES = (
        (None, 'None'),
        ('p', 'p'),
        ('q', 'q'),
        ('r', 'r'),
        ('s', 's'),
        ('u', 'u')
    )

    channel = models.ForeignKey(Channel, verbose_name=_('canal'), related_name='points')
    x = models.FloatField(db_index=True)
    y = models.FloatField()
    wave = models.CharField(max_length=1, choices=WAVES_TYPES, null=True, blank=True, verbose_name=_('onda detectada'))
    flagged = models.BooleanField(default=False, verbose_name=_('marca'))

    def __unicode__(self):
        return u'%s - %s - %s' % (unicode(self.channel), self.x, self.y)

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
