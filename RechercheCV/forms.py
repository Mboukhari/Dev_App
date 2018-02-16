# -*- coding: utf-8 -*-

from django import forms
from models import list_bu,Bu,Profile

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Bu
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = '__all__'