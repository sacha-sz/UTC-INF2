from django import forms
from django.http import HttpRequest
from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.http import require_http_methods
# from gestion_cours.forms import CoursForm, getIntervenantSelectFormUsingKey


@require_http_methods(["GET"])
def base(req: HttpRequest):
    return render(req, "base.html", {"prenom": req.GET.get("prenom")})


@require_http_methods(["GET", "POST"])
def creer_cours(req):
    pass
    if req.method == 'POST':
        '''
        - Remplir le formulaire du cours en utilisant le corps de la requête (HTTP)

        - Après avoir vérifié que toutes les informations concernant le cours ont bien été entrées,
        ajouter le cours en base

        - Utiliser le cours créé pour créer les groupes de TD et TP.
        Vous disposez pour cela de deux listes (req.POST.getlist(xxx)) contenant les id des intervenants:
             - intervenants_td
             - intervenants_tp
        Il faudra générer les numéros des groupes et ajouter les TD et TP en base en utilisant les modèles TP et TD.
        '''
        content = {'intervenants_td': req.POST.getlist('intervenants_td'),
                   'intervenants_tp': req.POST.getlist('intervenants_tp')}
    else:
        form = CoursForm()
        content = {'intervenants_td': [], 'intervenants_tp': []}

    TDInterForm = getIntervenantSelectFormUsingKey('td')
    TPInterForm = getIntervenantSelectFormUsingKey('tp')

    return render(req, 'creer_cours.html', {
        'form': form,
        'td_inter_form': TDInterForm(initial=content),
        'tp_inter_form': TPInterForm(initial=content)
    })
