from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context import RequestContext


@login_required
def patient_list(request):
    return HttpResponse(render(request, 'patient_list.html',
                               context=RequestContext(request)))


@login_required
def patient_detail(request, patient_id):
    return HttpResponse(render(request, 'patient_detail.html',
                               context=RequestContext(request)))