# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# # Create your models here.


list_bu = (
    ('DS','Data Science'),
    ('EMA','Enterprise Marketing Automation'),
    ('CRM','Customer Relationship Management'),
    ('SUP','Support'),
    ('DF','Digital Factory'),
    ('BC','Business Consulting'),
)

class Bu(models.Model):
    keywords = models.CharField(max_length=500,blank=False,verbose_name="Compétences clées")
    localisation = models.CharField(max_length=500,verbose_name="Localisation recherchée")
    experience = models.IntegerField(verbose_name="Années d'expérience")
    email_adress = models.EmailField(verbose_name="Votre adresse e-mail")
    bu = models.CharField(max_length=3,choices=list_bu)

    class Meta:
        db_table = "Bu"

    def __unicode__(self):
        return self.localisation



class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.FileField(upload_to = 'photos/')

   class Meta:
      db_table = "Profile"