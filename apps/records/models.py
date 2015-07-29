from django.db import models

# Create your models here.
class Record(models.Model):
    patient = models.ForeignKey('patients.Patient')
    taken_by = models.ForeignKey('users.User')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.patient.full_name, self.created.isoformat())


class Point(models.Model):
    WAVES_TYPES = (
        (None, 'None'),
        ('p', 'p'),
        ('q', 'q'),
        ('r', 'r'),
        ('s', 's'),
        ('u', 'u')
    )

    record = models.ForeignKey('records.Record')
    x = models.FloatField(db_index=True)
    y = models.FloatField()
    wave = models.CharField(max_length=1, choices=WAVES_TYPES, null=True, blank=True)
    flagged = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s - %s' % (str(self.record), self.x, self.y)

class Anomaly(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Annotation(models.Model):
    point = models.ForeignKey('records.Point')
    annotation_type = models.CharField(max_length=45)
    annotation = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User')
    anomaly = models.ForeignKey('records.Anomaly', null=True, blank=True)

    def __unicode__(self):
        return u'(%s) - %s - %s' % (str(self.point), self.created_by.full_name, self.created.isoformat())

