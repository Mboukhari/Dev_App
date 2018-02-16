# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from RechercheCV.forms import ProfileForm, ResearchForm
from RechercheCV.models import Profile, Bu


def SaveCV(request):
    saved = False
    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'RechercheCV/saved.html', locals())


# def home_recherche_CV(request):
#     return render(request,'RechercheCV/RechercheCV.html')

def upload_CV(request):
    return render(request,'RechercheCV/upload.html')

def BusinessUnit(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ResearchForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        form.save()
        # Ici nous pouvons traiter les données du formulaire
        keywords = form.cleaned_data['keywords']
        localisation = form.cleaned_data['localisation']
        experience = form.cleaned_data['experience']
        email_adress = form.cleaned_data['email_adress']
        bu = form.cleaned_data['bu']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'RechercheCV/RechercheCV.html', locals())
