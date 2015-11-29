# coding=utf-8
from apps.patients.forms import PatientForm, DiagnosisForm
from apps.patients.models import Patient, History, Diagnosis
from django.core.urlresolvers import reverse
from django.db.models import Model
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from faker import Factory
from django.template.context import RequestContext

fake = Factory.create()


class PatientList(View):
    form_class = PatientForm
    paginator_class = Paginator

    def get(self, request):

        order = request.GET.get('order', '-id')
        paginator = self.paginator_class(Patient.get_ordered_items(order), getattr(settings, 'MAX_ELEMENTS_PER_PAGE', 25))
        try:
            page = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        data = {
            'page': page,
            'order': order
        }
        return HttpResponse(render(request, 'patient_list.html',
                                   context=RequestContext(request, data)))

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
            History.objects.create(
                modified_by=request.user,
                patient=patient
            )
            messages.success(
                request,
                _('Los datos del paciente %(name)s han sido guardados &eacute;xitosamente') % {'name': patient.full_name})
            return HttpResponseRedirect(reverse('patient_detail', args=(patient.id,)))

        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))


class PatientDetail(View):
    form_class = PatientForm

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        return HttpResponse(render(request, 'patient_detail.html',
                                   context=RequestContext(request, {'patient': patient})))


class PatientEdit(View):
    form_class = PatientForm

    def get(self, request, patient_id):
        """
        Shows patient edit form
        :param request:
        :param patient_id:
        :return:
        """
        patient = get_object_or_404(Patient, id=patient_id)
        form = self.form_class(instance=patient)
        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))

    def post(self, request, patient_id):
        """
        Saves a patient edit
        :param request:
        :param patient_id:
        :return:
        """
        patient = get_object_or_404(Patient, id=patient_id)
        # processing form
        form = self.form_class(request.POST, request.FILES, instance=patient)

        if form.is_valid():
            patient = form.save()
            for changed in form.changed_data:
                History.objects.create(
                    modified_by=request.user,
                    patient=patient,
                    modified_field=changed,
                    modified_old_value=unicode(form.initial[changed]) if not isinstance(form.initial[changed], Model) else str(form.initial[changed].id),
                    modified_new_value=unicode(form.cleaned_data[changed]) if not isinstance(form.cleaned_data[changed], Model) else str(form.cleaned_data[changed].id)
                )
            messages.success(
                request,
                _('Los datos del paciente %(name)s han sido guardados &eacute;xitosamente') % {
                    'name': patient.full_name
                })
            return HttpResponseRedirect(reverse('patient_detail', args=(patient.id,)))

        data = {
            'patient': patient,
            'form': form
        }
        return HttpResponse(render(request, 'patient_detail.html', context=RequestContext(request, data)))


class PatientDelete(View):

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)

        patient.active = False
        patient.save()
        messages.success(
                         request,
                         _(u'El paciente %(name)s han desactivado éxitosamente') % {'name': patient.full_name})
        return HttpResponseRedirect(reverse('patient_list'))


class PatientNew(View):
    form_class = PatientForm

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


class DiagnosisList(View):
    paginator_class = Paginator

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        paginator = self.paginator_class(patient.diagnosis.all().order_by('-id'), 25)
        try:
            page = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        data = {
            'patient': patient,
            'page': page,
        }
        return HttpResponse(render(request, 'diagnosis_list.html', context=RequestContext(request, data)))


class DiagnosisNew(View):
    form_class = DiagnosisForm

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        data = {
            'patient': patient,
            'form': self.form_class()
        }

        return HttpResponse(render(request, 'diagnosis_form.html', context=RequestContext(request, data)))

    def post(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)

        form = self.form_class(request.POST)
        if not form.is_valid():
            data = {
                'patient': patient,
                'form': form
            }
            return HttpResponse(render(request, 'diagnosis_form.html', context=RequestContext(request, data)))

        diagnosis = form.save(commit=False)
        diagnosis.made_by = request.user
        diagnosis.patient = patient
        diagnosis.save()
        form.save_m2m()
        messages.success(
            request,
            _(u'El diagnóstico del paciente %(name)s ha sido guardado éxitosamente') % {
                'name': patient.full_name
            }
        )
        return HttpResponseRedirect(reverse('diagnosis_list', args=(patient_id,)))


class DiagnosisDetail(View):
    def get(self, request, diagnosis_id):
        diagnosis = get_object_or_404(Diagnosis, id=diagnosis_id)
        data = {
            'diagnosis': diagnosis
        }
