# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'RechercheCV'

urlpatterns = [
    url(r'^upload/saved/$',views.SaveCV,name='saved'),
    url(r'^upload/',views.upload_CV,name='upload'),
    url(r'^$',views.BusinessUnit,name='bu')
]