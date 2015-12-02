#!/usr/bin/env python
import os
import sys
import django
from faker import Factory
import random

fake = Factory.create()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardio.settings")
    django.setup()

    from apps.users.models import User
    from apps.patients.models import Patient, Ses, Occupation, Education, History

    user = User.objects.get(pk=1)
    number_patients = 3
    if len(sys.argv) == 2:
        try:
            number_patients = int(sys.argv[1])
        except ValueError:
            pass

    for x in xrange(number_patients):
        gender = random.choice(dict(Patient.GENDERS).keys())
        patient = Patient.objects.create(
            first_name=fake.first_name_female() if gender == 'f' else fake.first_name_male(),
            last_name=fake.last_name(),
            id_card_prefix=random.choice(dict(Patient.ID_CARD_PREFIXES).keys()),
            id_card_number=random.randint(100000, 29000000),
            birth_date=fake.date(),
            birth_place=fake.city(),
            gender=gender,
            marital_status=random.choice(dict(Patient.MARITAL_STATUS).keys()),
            ses=Ses.objects.all()[0],
            occupation=Occupation.objects.all()[0],
            education=Education.objects.all()[0],
        )

        History.objects.create(
            modified_by=user,
            patient=patient
        )


