from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context import RequestContext


@login_required
def list_patients(request):
    return HttpResponse(render(request, 'patient_list.html',
                               context=RequestContext(request)))