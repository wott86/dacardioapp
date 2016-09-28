from apps.patients.views import PatientList, PatientDetail,\
    PatientEdit, PatientNew, DiagnosisList, DiagnosisNew, \
    PatientDelete, PatientAdvanceSearch, PatientsActionView, \
    PatientActionDeactivate, PatientActionStatsGraphic, \
    PatientActionActivate, PatientActivate, PatientActionStats
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', login_required(PatientList.as_view()), name='patient_list'),
    url(r'^new/$', login_required(PatientNew.as_view()), name='patient_create'),
    url(r'^action/$',
        login_required(PatientsActionView.as_view()), name='patients_action'),
    url(r'^action/deactivate/$',
        login_required(PatientActionDeactivate.as_view()),
        name='patients_action_deactivate'),
    url(r'^action/activate/$',
        login_required(PatientActionActivate.as_view()),
        name='patients_action_activate'),
    url(r'^action/stats/$',
        login_required(PatientActionStats.as_view()),
        name='patients_action_stats'),
    url(r'^action/stats/graphic/$',
        login_required(PatientActionStatsGraphic.as_view()),
        name='patients_action_stats_graphic'),
    url(r'^(\d+)/$',
        login_required(PatientDetail.as_view()), name='patient_detail'),
    url(r'^(\d+)/edit/$',
        login_required(PatientEdit.as_view()), name='patient_edit'),
    url(r'^(\d+)/delete/$', login_required(PatientDelete.as_view()),
        name='patient_delete'),
    url(r'^(\d+)/activate/$',
        login_required(PatientActivate.as_view()), name='patient_activate'),

    url(r'^search/$',
        login_required(PatientAdvanceSearch.as_view()),
        name='patient_advanced_search'),

    url(r'^(\d+)/diagnosis/$',
        login_required(DiagnosisList.as_view()), name='diagnosis_list'),
    url(r'^(\d+)/diagnosis/new/$',
        login_required(DiagnosisNew.as_view()), name='diagnosis_new'),
    url(r'^(?P<patient_id>\d+)/records/', include('apps.records.urls')),
]
