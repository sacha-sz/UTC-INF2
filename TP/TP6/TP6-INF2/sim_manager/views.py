from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Simulation, Partage_Simulation
from .forms import UserProfileForm, SimuForm, Changer_MDP, Supprimer_Profil, Creation_Profil, Shared_Simulation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from pyfhn.fhn_runner import run_fhn_base
import matplotlib.pyplot as plt
from io import StringIO


# Create your views here.
def landing(request):
    return render(request, "base.html", locals())


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def simulation_list(request):
    """
    Vue permettant de lister l'ensemble des simulations liés à un utilisateur. A savoir celles qu'il a créé
    (en favori ou non) et celles qu'on lui a partagé
    """
    # Liste des simulations qu'il a créé
    simulation_user = Simulation.objects.filter(user_creator=request.user)

    # Liste des simulations qu'on lui a partagé
    # Récupération sous forme de liste des id de simulation pour lesquelles sont id est dans la classe destinataire
    shared_simulations_id = Partage_Simulation.objects.filter(destinataire=request.user).values_list('simulation')
    shared_simulations_id = list(elt[0] for elt in shared_simulations_id)  # Récupération brute des valeurs
    # Recherche dans la table de simulation des id des simulations
    shared_simulations = Simulation.objects.filter(id__in=shared_simulations_id)

    # Renvoie vers la page avec les deux listes
    return render(request, "simulation_list.html", {"user_sims": simulation_user, "user_shared": shared_simulations})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def edit_profile(request):
    """
    Vue permettant d'éditer les champs : first_name; last_name et email
    """
    # Valeurs booléennes pour le template
    envoi = False
    erreur_email = False

    # Gestion du formulaire
    if request.method == "POST":
        # Initialisation du formulaire
        user_profile_form = UserProfileForm(request.POST)
        # Récupération de l'utilisateur courant
        current_user = User.objects.get(username=request.user.username)

        # Test si le formulaire est correctement rempli
        if user_profile_form.is_valid() and user_profile_form.cleaned_data["email"]:

            # Test si l'utilisateur a changé ou non son adresse mail
            if current_user.email == request.POST["email"]:
                # Mise à jour des champs de l'utilisateur courant, s'il ne change pas son adresse mail
                current_user.first_name = user_profile_form.cleaned_data["first_name"]
                current_user.last_name = user_profile_form.cleaned_data["last_name"]
                # Sauvegarde dans la base de données
                current_user.save()
                # Changement de la valeur booléenne
                envoi = True

            # Sinon teste si l'email est disponible (méthode créé dans le forms.py)
            elif user_profile_form.email_disponible(user_profile_form.cleaned_data["email"]):
                # Mise à jour des champs de l'utilisateur courant, s'il change son adresse mai
                current_user.first_name = user_profile_form.cleaned_data["first_name"]
                current_user.last_name = user_profile_form.cleaned_data["last_name"]
                current_user.email = user_profile_form.cleaned_data["email"]
                # Sauvegarde dans la base de données
                current_user.save()
                # Changement de la valeur booléenne
                envoi = True

            # Sinon change la valeur booléenne permettant un affichage dynamique de l'erreur d'adresse mail
            else:
                erreur_email = True
    else:
        # Affiche le formulaire pré-rempli
        user_profile_form = UserProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": user_profile_form, "envoi":envoi, "erreur_email":erreur_email})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def new_simu(request):
    """
    Construire le formulaire, soit avec les données postées, soit vide si l'utilisateur accède pour la première fois
    à la page.
    """
    form = SimuForm(request.POST, request.FILES)

    # Si le formulaire est valide
    if form.is_valid():
        params = form.cleaned_data
        print(params)
        # Création de la simulation
        newsim = Simulation.objects.create(
            user_creator=request.user,
            alpha=params["alpha"],
            beta=params["beta"],
            gamma=params["gamma"],
            delta=params["delta"],
            epsilon=params["epsilon"],
        )
        # Sauvegarde dans la base de données
        newsim.save()
        # Lance la simulation en appelant la fonction run_sim
        return run_sim(request, newsim.id)
    return render(request, "newsimu.html", locals())


@require_http_methods(["GET", "POST"])
def run_sim(request, object_id):
    """
    Effectue la simulation puis la retourne vers le template
    """
    # Récupération des informations de la simulation
    params = model_to_dict(get_object_or_404(Simulation, pk=object_id))

    # Suppression des paramètres inutiles pour le calcul
    # A savoir : username (user_creator), id de la simulation et is_favorite
    params.pop("user_creator")
    params.pop("id")
    params.pop("is_favorite")

    # Récupération des dernières informations : alpha, beta, delta, gamma, epsilon
    res = run_fhn_base(params)

    # Mise en page de la simulation
    f = plt.figure()
    plt.title("FHN Simulation")
    plt.xlabel("Time")
    plt.ylabel("Outputs")
    plot = plt.plot(res["t"], res["y"][0], res["t"], res["y"][1])
    plt.legend(["v", "w"])
    imgdata = StringIO()
    f.savefig(imgdata, format="svg")
    imgdata.seek(0)

    # data contenant le graphique
    data = imgdata.getvalue()
    return render(request, "graphic.html", {"graphic": data})


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def simulation_delete(request, object_id):
    """
    Lié à la vue de sim_list, nous pouvons supprimer une simulation de la liste de l'utilisateur
    """
    # Récupération de la simulation
    sim = get_object_or_404(Simulation, pk=object_id)

    # La suppression de la simulation va dépendre de son auteur
    if request.user == sim.user_creator:
        # Si l'utilisateur est à l'origine de cette simulation, elle va être totalement supprimé
        sim.delete()
    else:
        # Sinon la simulation lui a été partagé et nous ne la supprimons que de la table de simulation
        # Ainsi elle sera toujours présente pour son auteur ou les autres personnes l'ayant reçu
        share_sim = Partage_Simulation.objects.filter(destinataire=request.user, simulation=object_id)
        share_sim.delete()
    return HttpResponseRedirect(reverse_lazy("sim_list"))


@require_http_methods(["GET", "POST"])
def add_user(request):
    """
    Fonction permettant de créer un nouvel utilisateur
    """
    # Valeurs booléennes pour le template
    email_not_available = False
    erreur = False

    # Gestion du formulaire
    if request.method == "POST":
        # Initialisation du formulaire
        form = Creation_Profil(request.POST)

        # Test si le formulaire est correctement rempli et que l'email est de format correct
        if form.is_valid() and form.cleaned_data["email"]:

            # Test si l'email est disponible (méthode créé dans le forms.py)
            if form.email_disponible(request.POST["email"]):
                # Si tout est correct enregistre le formulaire dans la BDD
                form.save()
                # Et redirige l'utilisateur vers l'accueil
                return redirect("/")
            else:
                # Sinon changement de la valeur booléenne, modifiant l'affichage
                email_not_available = True
        else:
            # Sinon changement de la valeur booléenne, modifiant l'affichage
            erreur = True
    else:
        # Affiche le formulaire
        form = Creation_Profil()
    return render(request, "new_profile.html", {"form": form, "email_not_available": email_not_available, "erreur": erreur})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def change_password(request):
    """
    Fonction permettant de changer le mdp de l'utilisateur
    """
    # Valeur booléenne pour le template
    erreur_password = False

    # Gestion du formulaire
    if request.method == "POST":
        form = Changer_MDP(request.user, data=request.POST)

        # Test si le formulaire est valide
        if form.is_valid():
            # Si c'est le cas enregistre les modifications
            form.save()
            # Permet de garder l'utilisateur connecté
            update_session_auth_hash(request, form.user)
            # Redirige vers l'accueil
            return redirect("/")
    else:
        # Affiche le formulaire
        form = Changer_MDP(request.user)
    return render(request, "change_password.html", {"form": form, "erreur_mdp": erreur_password})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def del_user(request):
    """
    Fonction permettant de changer le mdp de l'utilisateur
    """
    # Valeur booléenne pour le template
    erreur_saisie = False

    # Gestion du formulaire
    if request.method == "POST":
        form = Supprimer_Profil(request.POST)

        # Permet de tester si le formulaire est correct et que le texte entré est bien : CONFIRMER
        if form.is_valid() and request.POST["texte_confirmation"] == "CONFIRMER":
            # Récupère l'utilisateur courant
            current_user = User.objects.get(username=request.user.username)
            # Le supprime de la BDD
            current_user.delete()
            # Redirige vers l'accueil
            return redirect("/")
        else:
            erreur_saisie = True
    else:
        # Affiche le formulaire
        form = Supprimer_Profil()
    return render(request, "del_user.html", {"form": form, "erreur_saisie": erreur_saisie})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def simulation_share(request, object_id):
    # Valeur booléenne pour le template
    impossible_send = False

    # Gestion du formulaire
    if request.method == "POST":
        form = Shared_Simulation(request.POST)

        # Test si le formulaire est valide
        if form.is_valid() and form.cleaned_data['destinataire']:
            expediteur = request.user
            destinataire = form.cleaned_data['destinataire']

            # Test si le destinataire a déjà reçu la simulation ou si l'utilisateur partage la simulation a lui-même
            if Partage_Simulation.objects.filter(destinataire=destinataire).exists() or expediteur == destinataire:
                # Change la valeur du booléen
                impossible_send = True
            else:
                # Récupère la simulation
                sim = Simulation.objects.get(pk=object_id)
                # L'ajoute à la BDD : Partage_Simulation et l'enregistre (.save())
                Partage_Simulation(expediteur=expediteur, destinataire=destinataire, simulation=sim).save()
                # Redirige vers la liste des simulations
                return redirect("sim_list")
    else:
        # Affiche le formulaire
        form = Shared_Simulation()
    return render(request, "simulation_share.html", {"form": form, "impossible_send": impossible_send})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def simulation_fav(request, object_id):
    """
    Vue permettant de modifier la valeur du booléen : is_favorite
    """
    # Récupération de la simulation
    sim = get_object_or_404(Simulation, pk=object_id)

    # La modification va dépendre de son état actuel
    if sim.is_favorite:
        # Si la valeur est True nous la mettons à False
        sim.is_favorite = False
        # Puis nous enregistrons la modification
        sim.save()
    else:
        # Si la valeur est False nous la mettons à True
        sim.is_favorite = True
        # Puis nous enregistrons la modification
        sim.save()
    return redirect("sim_list")
