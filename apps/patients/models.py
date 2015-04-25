from apps.users.models import User
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
import os
import uuid
import mimetypes
from django.utils import timezone


# ################## Info models

class Ses(models.Model):
    """
    Socioeconomic status
    """
    name = models.CharField(max_length=128)


class Education(models.Model):
    """
    Education level
    """
    name = models.CharField(max_length=128)


class Occupation(models.Model):
    """
    What the patient does
    """
    name = models.CharField(max_length=128)


class Habit(models.Model):
    name = models.CharField(max_length=128)


class RelationshipType(models.Model):
    name = models.CharField(max_length=256)


def get_upload_path(instance, filename):
        return os.path.join(settings.MEDIA_ROOT, 'patients', str(uuid.uuid4()) +
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
        ('d', _('divorciado')),
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
    city = models.ForeignKey('cities.City', related_name='patients')
    street = models.TextField()
    street_2 = models.TextField()
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS, default='s')
    ses = models.ForeignKey(Ses, verbose_name='Socioeconomic status', related_name='patients')
    occupation = models.ForeignKey(Occupation, related_name='patients')
    education = models.ForeignKey(Education, related_name='patients')
    habits = models.ManyToManyField(Habit, related_name='patients')

    @property
    def full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()

    @property
    def id_card(self):
        return '%s - %s' % (self.id_card_prefix, self.id_card_number)

    @property
    def age(self):
        today = timezone.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month,
                                                                                self.birth_date.day))

    @property
    def address(self):
        return '%s, %s' % (self.street, self.city.name)

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
    modified_by = models.ForeignKey(User, related_name='history')
    patient = models.ForeignKey(Patient, related_name='history')
    date = models.DateTimeField(auto_now_add=True)
    modified_field = models.CharField(max_length=32)

    def __unicode__(self):
        return 'Patient: %s / M.D. %s' % (str(self.patient), self.modified_by.get_full_name())


class PersonalRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='personal_records')


class FamilyRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='family_records')
    relationship_type = models.ForeignKey(RelationshipType, related_name='family_records')


