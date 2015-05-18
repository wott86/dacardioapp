from apps.patients.forms import PatientBaseForm
from apps.patients.models import Patient
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from faker import Factory

fake = Factory.create()

# Create your views here.
from django.template.context import RequestContext


class PatientList(View):
    form_class = PatientBaseForm

    def get(self, request):
        return HttpResponse(render(request, 'patient_list.html',
                                   context=RequestContext(request)))

    def post(self, request):
        """
        Process user creation
        :param request:
        :return:
        """
        # processing form
        form = self.form_class(request.POST, request.FILES)

        patient = None
        if form.is_valid():
            patient = form.save()

        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))


class PatientDetail(View):
    form_class = PatientBaseForm

    def get(self, request, patient_id):
        patient = Patient.objects.get(pk=1)
        return HttpResponse(render(request, 'patient_detail.html',
                                   context=RequestContext(request, {'patient': patient})))

    def post(self, request, patient_id):
        """
        Saves an user edit
        :param request:
        :param patient_id:
        :return:
        """
        patient = Patient.objects.get(pk=1)
        # processing form
        form = self.form_class(request.POST, request.FILES, instance=patient)

        if form.is_valid():
            patient = form.save()

        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))


class PatientEdit(View):
    form_class = PatientBaseForm

    def get(self, request, patient_id):
        """
        Shows patient edit form
        :param request:
        :param patient_id:
        :return:
        """
        patient = Patient.objects.get(pk=1)
        form = self.form_class(instance=patient)
        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))


class PatientNew(View):
    form_class = PatientBaseForm

    def get(self, request):
        """
        Shows patient creation form
        :param request:
        :return:
        """
        form = self.form_class()
        data = {
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))
