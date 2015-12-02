# coding=utf-8
from apps.patients.models import OrderManager
from django.db import models
from django.db.models.aggregates import Avg, StdDev
from django.utils.translation import ugettext as _


# Create your models here.
class Record(models.Model):
    patient = models.ForeignKey('patients.Patient', verbose_name=_('paciente'), related_name='records')
    taken_by = models.ForeignKey('users.User', verbose_name=_('registrado por'), related_name='records_loaded')
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
            y.append(
                self.points.filter(x__gte=initial_time,
                                   x__lte=initial_time+interval).order_by('x').aggregate(average=Avg('y'))['average']
            )
            initial_time += interval
        return range(1, len(y) + 1), y

    def get_standard_deviation_points(self, initial_time, final_time, interval):
        y = []
        while initial_time < final_time:
            std_dev = self.points.filter(x__gte=initial_time,
                                         x__lte=initial_time+interval).order_by('x').aggregate(std_dev=StdDev('y'))

            y.append(std_dev['std_dev'])
            initial_time += interval
        return range(1, len(y) + 1), y

    def get_return_map(self, initial_time, final_time):
        points = [point.y for point in self.points.filter(x__gte=initial_time, x__lte=final_time).order_by('x')]
        x = []
        y = []

        for index in xrange(len(points) - 1):
            try:
                y.append(points[index+1])
                x.append(points[index])
            except IndexError:
                break
        return x, y


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
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_('orden'))

    objects = OrderManager()

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
