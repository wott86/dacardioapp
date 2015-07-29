# -*- coding: utf-8 -*-
from apps.users.models import User
from django.db import models
from django.utils.translation import ugettext as _
import os
import uuid
import mimetypes
from django.utils import timezone


# managers
class OrderManager(models.Manager):
    def get_queryset(self):
        return super(OrderManager, self).get_queryset().order_by('order')


class OrderNameManager(OrderManager):
    def get_queryset(self):
        return super(OrderNameManager, self).get_queryset().order_by('name')


# ################## Info models
class Ses(models.Model):
    """
    Socioeconomic status
    """
    name = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=0)

    objects = OrderNameManager()

    def __unicode__(self):
        return self.name


class Education(models.Model):
    """
    Education level
    """
    name = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=0)

    objects = OrderManager()

    def __unicode__(self):
        return self.name


class Occupation(models.Model):
    """
    What the patient does
    """
    name = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=0)

    objects = OrderManager()

    def __unicode__(self):
        return self.name


class Habit(models.Model):
    name = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=0)

    objects = OrderManager()

    def __unicode__(self):
        return self.name


class RelationshipType(models.Model):
    name = models.CharField(max_length=256)
    order = models.PositiveSmallIntegerField(default=0)

    objects = OrderManager()

    def __unicode__(self):
        return self.name


def get_upload_path(instance, filename):
        return os.path.join('patients', str(uuid.uuid4()) +
                            ('.' + filename.split('.')[-1] if filename not in (None, '') else
                            mimetypes.guess_extension(instance.image.file.content_type)))


# ################## Patient data models
class Patient(models.Model):
    """
    The patient
    """
    # Constants
    ID_CARD_PREFIXES = (
        ('V', 'V'),
        ('J', 'J'),
        ('G', 'G'),
        ('E', 'E')
    )

    GENDERS = (
        ('M', _('Masculino')),
        ('F', _('Femenino')),
    )

    MARITAL_STATUS = (
        ('s', _('Soltero')),
        ('m', _('Casado')),
        ('w', _('Viudo')),
        ('d', _('Divorciado')),
    )

    # Fields
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    id_card_prefix = models.CharField(max_length=1, choices=ID_CARD_PREFIXES, default='V')
    id_card_number = models.CharField(max_length=32)
    picture = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    dwelling = models.BooleanField(default=True)
    city = models.ForeignKey('cities.City', related_name='patients', null=True, blank=True)
    street = models.TextField(default='', blank=True)
    street_2 = models.TextField(default='', blank=True)
    phone_home = models.CharField(max_length=50, default='', blank=True)
    phone_mobile = models.CharField(max_length=50, default='', blank=True)
    phone_office = models.CharField(max_length=50, default='', blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS, default='s')
    ses = models.ForeignKey(Ses, verbose_name=_(u'Estatus socioeconómico'), related_name='patients')
    occupation = models.ForeignKey(Occupation, related_name='patients')
    education = models.ForeignKey(Education, related_name='patients')
    personal_record = models.TextField(default='', blank=True)
    family_record = models.TextField(default='', blank=True)
    habits = models.ManyToManyField(Habit, related_name='patients', blank=True)

    class Meta:
        verbose_name = _('Paciente')
        verbose_name_plural = _('Pacientes')

    @property
    def full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()

    @property
    def id_card(self):
        return '%s-%s' % (self.id_card_prefix, self.id_card_number)

    @property
    def age(self):
        today = timezone.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month,
                                                                                self.birth_date.day))

    @property
    def address(self):
        return ('%s, %s' % (self.street, self.city.name)) if self.city else self.street

    @property
    def first_history(self):
        if self.history.all().exists():
            return self.history.all().order_by('id')[0]
        else:
            return None

    @property
    def last_history(self):
        if self.history.all().exists():
            return self.history.all().order_by('-id')[0]
        else:
            return None

    def __unicode__(self):
        return self.full_name

    class Meta:
        unique_together = ('id_card_prefix', 'id_card_number')


class History(models.Model):
    ALL = 'ALL'
    SEPARATOR = '[|]'

    modified_by = models.ForeignKey(User, related_name='history')
    patient = models.ForeignKey(Patient, related_name='history')
    date = models.DateTimeField(auto_now_add=True)
    modified_field = models.TextField(default=ALL)
    modified_old_value = models.TextField(default='')
    modified_new_value = models.TextField(default='')

    def __unicode__(self):
        return 'Patient: %s / M.D. %s' % (unicode(self.patient), self.modified_by.get_full_name())


"""class PersonalRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='personal_records')

    def __unicode__(self):
        return '%s - %s ' % (self.patient.full_name, self.name)"""


"""class FamilyRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='family_records')
    relationship_type = models.ForeignKey(RelationshipType, related_name='family_records')

    def __unicode__(self):
        return '%s - %s (%s)' % (self.patient.full_name, self.name, self.relationship_type.name)"""
