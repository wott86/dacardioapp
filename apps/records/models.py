# coding=utf-8
from datetime import timedelta

from apps.patients.models import OrderManager
from django.db import models
from django.db.models.aggregates import Avg, StdDev, Sum
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
        ('o', _('Original')),
        ('d', _('Derivada')),
        ('f', _('Filtrada')),
        ('r', _('RR'))
    )

    record = models.ForeignKey(Record, verbose_name=_('registro'), related_name='channels')
    type = models.CharField(max_length=2, default='n', choices=CHANNEL_TYPES, verbose_name=_('tipo'))
    name = models.CharField(max_length=50, blank=True, default='', verbose_name=_('nombre'))
    description = models.TextField(blank=True, default='', verbose_name=_(u'descripción'))
    start_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Fecha de inicio'))
    #end_date = models.DateTimeField(null=True, blank=True, verbose_name=_(u'Fecha de finalización'))
    sampling_rate = models.IntegerField(default=500, verbose_name=_('Tasa de muestreo'))

    @property
    def end_date(self):
        milliseconds = self.duration
        return (self.start_date + timedelta(milliseconds=milliseconds)) if self.start_date else None

    @property
    def duration(self):
        if self.is_time:
            return self.points.all().aggregate(sum=Sum('y'))['sum']
        return self.points.all().count() * self.sampling_rate

    @property
    def is_time(self):
        """
        Says if Y represents time or not
        :return:
        """
        return self.type == 'r'

    @property
    def duration_str(self):
        return str(timedelta(milliseconds=self.duration))[:-4]

    class Meta:
        verbose_name = _('canal')
        verbose_name_plural = _('canales')

    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.record), self.get_type_display(), self.name)

    def get_media_points(self, initial_time, final_time, interval):
        y = []
        while initial_time < final_time:
            if self.is_time:
                y.append(
                    self.points.filter(y_accumulative__gte=initial_time,
                                       y_accumulative__lte=initial_time + interval).order_by('x').aggregate(
                        average=Avg('y'))['average']
                )
            else:
                y.append(
                    self.points.filter(y___gte=initial_time,
                                       x__lte=initial_time+interval).order_by('x').aggregate(average=Avg('y'))['average']
                )
            initial_time += interval
        return range(1, len(y) + 1), y

    def get_standard_deviation_points(self, initial_time, final_time, interval):
        y = []
        while initial_time < final_time:
            if self.is_time:
                std_dev = self.points.filter(y_accumulative__gte=initial_time,
                                             y_accumulative__lte=initial_time + interval).order_by('x').aggregate(
                    std_dev=StdDev('y'))
            else:
                std_dev = self.points.filter(x__gte=initial_time,
                                             x__lte=initial_time+interval).order_by('x').aggregate(std_dev=StdDev('y'))

            y.append(std_dev['std_dev'])
            initial_time += interval
        return range(1, len(y) + 1), y

    def get_standard_deviation(self, initial_time, final_time):

        if self.is_time:
            return self.points.filter(y_accumulative__gte=initial_time, y_accumulative__lte=final_time).order_by(
                'x').aggregate(std_dev=StdDev('y'))[
                'std_dev']

        return \
            self.points.filter(x__gte=initial_time, x__lte=final_time).order_by('x').aggregate(
                std_dev=StdDev('y'))[
                'std_dev']

    def get_media(self, initial_time, final_time):
        if self.is_time:
            return \
                self.points.filter(y_accumulative__gte=initial_time, y_accumulative__lte=final_time).order_by('x').aggregate(avg=Avg('y'))[
                    'avg']

        return \
            self.points.filter(x__gte=initial_time, x__lte=final_time).order_by('x').aggregate(avg=Avg('y'))[
                'avg']

    def get_return_map(self, initial_time, final_time):
        if self.is_time:
            points = [point.y for point in
                      self.points.filter(y_accumulative__gte=initial_time, y_accumulative__lte=final_time).order_by(
                          'x')]
        else:
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

    def get_PNN50(self, initial_time, final_time):
        if self.is_time:
            points = self.points.filter(y_accumulative__gte=initial_time, y_accumulative__lte=final_time).order_by('x')
        else:
            points = self.points.filter(x__gte=initial_time, x__lte=final_time).order_by('x')

        length = points.count()
        if length == 0:
            return None

        last_value = points[0].y
        counter = 0
        for point in points:
            if abs(last_value - point.y) > 50:
                counter += 1
            last_value = point.y
        return (counter / (length - 1)) * 100

    def get_SDNNindex(self, initial_time, final_time, segment_size):
        if self.is_time:
            points = self.points.filter(y_accumulative__gte=initial_time, y_accumulative__lte=final_time).order_by('x')
        else:
            points = self.points.filter(x__gte=initial_time, x__lte=final_time).order_by('x')

        # todo: finish this


    @property
    def SDNN(self):
        return self.points.all().aggregate(std_dev=StdDev('y'))['std_dev']

    @property
    def average(self):
        return self.points.all().aggregate(avg=Avg('y'))['avg']

    def fill_accumulatives(self):
        """
        Fills all Point.y_accumulative
        :return: NoneType
        """
        sum = 0
        for point in self.points.all().order_by('x'):
            sum += point.y
            point.y_accumulative = sum
            point.save()


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
    y_accumulative = models.FloatField(default=0, verbose_name=_('Y acumulativo'),
                                       help_text=_(
                                           'La sumatoria de todos los valores "Y" hasta el actual, se calcula con Channel.fill_accumulatives'))
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
