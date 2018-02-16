# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home), #accueil de l'application centrale
    url(r'BaseCV/',views.filter_cv),
    url(r'list_CV/display/',views.pdf_view)
]