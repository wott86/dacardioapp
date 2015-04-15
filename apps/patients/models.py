from apps.users.models import User
from django.db import models
from django.utils.translation import ugettext as _


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

    # Fields
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    id_card_prefix = models.CharField(max_length=1, choices=ID_CARD_PREFIXES, default='V')
    id_card_number = models.CharField(max_length=32, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    dwelling = models.BooleanField(default=True)
    city = models.ForeignKey('cities.City', related_name='patients')
    street = models.TextField()
    street_2 = models.TextField()
    ses = models.ForeignKey(Ses, verbose_name='Socioeconomic status', related_name='patients')
    occupation = models.ForeignKey(Occupation, related_name='patients')
    education = models.ForeignKey(Education, related_name='patients')
    habits = models.ManyToManyField(Habit, related_name='patients')


class History(models.Model):
    modified_by = models.ForeignKey(User, related_name='history')
    patient = models.ForeignKey(Patient, related_name='history')
    date = models.DateTimeField(auto_now_add=True)
    modified_field = models.CharField(max_length=32)


class PersonalRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='personal_record')


class FamilyRecord(models.Model):
    name = models.CharField(max_length=256)
    patient = models.ForeignKey(Patient, related_name='family_record')
    relationship_type = models.ForeignKey(RelationshipType, related_name='family_record')


