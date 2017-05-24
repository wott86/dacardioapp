from apps.patients.models import Patient, Diagnosis
from django import forms
__author__ = 'alvaro'


class PatientBaseForm(forms.ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'city': forms.TextInput,
            'habits': forms.SelectMultiple(attrs={'class': 'selectpicker'})
        }
        exclude = []

    def clean_picture(self):
        picture = self.cleaned_data.get('picture', None)

        '''if picture:
            w, h = get_image_dimensions(picture)
            if abs(w - h) > 1:
                raise forms.ValidationError(_('La imagen debe ser cuadrada'))'''

        return picture


class PatientAdminForm(PatientBaseForm):
    class Meta(PatientBaseForm.Meta):
        pass


class PatientForm(PatientBaseForm):
    class Meta(PatientBaseForm.Meta):
        exclude = ['street_2', 'chart_number', 'active', 'created_by', 'updated_by']
        widgets = {
            'city': forms.TextInput,
            'habits': forms.SelectMultiple(attrs={'class': 'selectpicker'}),
            'picture': forms.ClearableFileInput(
                attrs={'class': 'testing_class'})
        }


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        exclude = ['patient', 'made_by']
        widgets = {
            'anomalies': forms.SelectMultiple(attrs={'class': 'selectpicker'}),
            'attachment': forms.ClearableFileInput(
                attrs={'class': 'testing_class'})
        }
