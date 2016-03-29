# coding=utf-8
from apps.patients.forms import PatientForm, DiagnosisForm
from apps.patients.helpers import get_patient_ids
from apps.patients.models import Patient, History, Diagnosis
from apps.records.models import Anomaly
from django.core.urlresolvers import reverse
from django.db.models import Model, Q
from django.db.models.aggregates import Avg, StdDev
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.template.context import RequestContext
from django.utils import timezone
from faker import Factory
import datetime
from apps.records.helpers import plot

fake = Factory.create()


class PatientList(View):
    form_class = PatientForm
    paginator_class = Paginator

    def get(self, request):

        order = request.GET.get('order', '-id')
        query = request.GET.get('q')
        deactivated_patients = 'deactivated' in request.GET
        patients = Patient.get_ordered_items(order)
        # search
        if query is not None:
            queries = Q()
            for q in query.split():
                queries |= Q(first_name__icontains=q) |\
                           Q(last_name__icontains=q) |\
                           Q(id_card_number__contains=q)
            patients = patients.filter(queries)

        # Filters in advanced search
        gender = request.GET.get('gender')
        if gender not in ('', None):
            patients = patients.filter(gender=gender)

        age_init = request.GET.get('age_init')
        age_end = request.GET.get('age_end')
        if age_init not in ('', None):
            now = timezone.now()
            if age_end not in ('', None):
                if age_end < age_init:
                    age_init, age_end = age_end, age_init
                date_init = now.year - int(age_end)
                date_end = now.year - int(age_init)
                patients = patients.filter(birth_date__range=(datetime.date(date_init, 1, 1),
                                                              datetime.date(date_end+1, now.month, now.day)))
            else:
                date_init = now.year - int(age_init)
                patients = patients.filter(birth_date__range=(datetime.date(date_init, 1, 1),
                                                              datetime.date(date_init+1, now.month, now.day)))

        anomaly = request.GET.get('anomaly')

        if anomaly not in ('', None):
            patients = patients.filter(diagnosis__anomalies__id=anomaly).distinct()

        if not deactivated_patients:
            patients = patients.filter(active=True)
        paginator = self.paginator_class(
            patients,
            request.GET.get('num_elements', getattr(settings, 'MAX_ELEMENTS_PER_PAGE', 25))
        )
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
        :param request: well, the request object
        :return: response
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


class PatientActivate(View):

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)

        patient.active = True
        patient.save()
        messages.success(
                         request,
                         _(u'El paciente %(name)s han activado éxitosamente') % {'name': patient.full_name})
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


class PatientAdvanceSearch(View):

    def get(self, request):
        data = {
            'anomalies': Anomaly.objects.all()
        }
        return HttpResponse(render(request, 'patient_advanced_search.html', context=RequestContext(request, data)))


# Diagnosis
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

        form = self.form_class(request.POST, request.FILES)
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


class PatientsActionView(View):

    TEMPLATES = {
        'deactivate': 'actions/patient_deactivate_bulk.html',
        'activate': 'actions/patient_activate_bulk.html',
        'stats': 'actions/patient_stats_form.html'
    }

    def post(self, request):
        ids = get_patient_ids(request.POST)
        action = request.POST.get('action')
        if action in ('', None):
            return HttpResponseRedirect(reverse('patient_list'))

        if len(ids) == 0:
            messages.error(
                request,
                _(u'Por favor seleccione uno o varios pacientes')
            )
            return HttpResponseRedirect(reverse('patient_list'))

        patients = Patient.objects.filter(id__in=ids)

        try:
            template = self.TEMPLATES[action]
        except KeyError:
            messages.error(
                request,
                _(u'Por favor escoja una opción válida')
            )
            return HttpResponseRedirect(reverse('patient_list'))

        data = {
            'patients': patients
        }

        return HttpResponse(render(request, template, context=RequestContext(request, data)))


class PatientActionDeactivate(View):

    def post(self, request):
        ids = get_patient_ids(request.POST)
        Patient.objects.filter(id__in=ids).update(active=False)
        messages.info(
            request,
            _(u'Pacientes desactivados éxitosamente')
        )
        return HttpResponseRedirect(reverse('patient_list'))


class PatientActionActivate(View):

    def post(self, request):
        ids = get_patient_ids(request.POST)
        Patient.objects.filter(id__in=ids).update(active=True)
        messages.info(
            request,
            _(u'Pacientes activados éxitosamente')
        )
        return HttpResponseRedirect(reverse('patient_list'))


class PatientActionStats(View):

    def post(self, request):
        request.GET = request.POST
        return HttpResponse(render(request, 'stats/bulk_graphic.html', context=RequestContext(request)))


class PatientActionStatsGraphic(View):
    MEDIA = 'media'
    STD_DEV = 'std_dev'
    RETURN = 'return'
    SDSD = 'sdsd'

    STAT_TYPES = [MEDIA, STD_DEV, RETURN, SDSD]

    def get(self, request):
        ids = get_patient_ids(request.GET)

        patients = Patient.objects.filter(id__in=ids)

        ys = []
        xs = []
        stat_type = request.GET.get('stat_type', 'media')
        interval_start = request.GET.get('interval_start', 0)
        interval_end = request.GET.get('interval_end')
        title = None

        if stat_type not in self.STAT_TYPES:
            return HttpResponse(status=400)

        if stat_type == self.MEDIA:
            title = _('Promedio de los RR de los pacientes')
            for patient in patients:
                channel = patient.get_last_channel()
                if channel is not None:
                    ys.append(channel.points.all().aggregate(average=Avg('y'))['average'])
                else:
                    ys.append(0)
        elif stat_type == self.STD_DEV:
            title = _(u'Desviación estándar de los RR de los pacientes')
            for patient in patients:
                channel = patient.get_last_channel()
                if channel is not None:
                    ys.append(channel.points.all().aggregate(std_dev=StdDev('y'))['std_dev'])
                else:
                    ys.append(0)

        xs = xrange(len(ys))
        response = HttpResponse(content_type='image/png')
        plot.get_image(xs, ys, response, title=title)

        return response
