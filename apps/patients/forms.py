from apps.patients.models import Patient

__author__ = 'alvaro'
from django import forms


class PatientBaseForm(forms.ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'city': forms.TextInput,
            'habits': forms.SelectMultiple(attrs={'class': 'selectpicker'})
        }
        exclude = []


class PatientAdminForm(PatientBaseForm):
    class Meta(PatientBaseForm.Meta):
        pass


class PatientForm(PatientBaseForm):
    class Meta(PatientBaseForm.Meta):
        exclude = ['street_2']