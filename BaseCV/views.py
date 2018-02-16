# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from RechercheCV.models import Bu,Profile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, FileResponse,Http404

# Create your views here.

def home(request):
    return render(request,'BaseCV/accueil.html')

def filter_cv(request):
    list_CV = Profile.objects.all()
    return render(request,'BaseCV/list_CV.html',{'base_globale' : list_CV})

# def pdf_view(request):
#     fs = FileSystemStorage()
#     filename = 'mypdf.pdf'
#     if fs.exists(filename):
#         with fs.open(filename) as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#             return response
#     else:
#         return HttpResponseNotFound('The requested pdf was not found in our server.')

def pdf_view(request):
    ref = request.GET.get('sku')
    try:
        return FileResponse(open('media/'+ ref, 'rb'), content_type='application/pdf')
    except:
        raise Http404()