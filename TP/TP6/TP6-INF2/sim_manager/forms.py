from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .models import Simulation, Partage_Simulation
from django.contrib.auth.models import User


class SimuForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def email_disponible(self, email):
        liste = User.objects.filter(email=email)  # va lister tous les utilisateurs avec cette adresse mail
        if not liste:  # Si la liste est vide, l'adresse mail n'est pas prise : retourne vrai (email disponible)
            return True
        return False  # Sinon retourne Faux (email non disponible)


class Creation_Profil(UserCreationForm):
    # Hérite de UserCreationForm
    class Meta:
        # Suit le modèle : User
        model = User
        # Choix des champs que nous voulons que l'utilisateur rentre pour son inscription
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

    def email_disponible(self, email):
        """
        Méthode permettant de vérifier que l'email est disponible
        """
        liste = User.objects.filter(email=email)  # va lister tous les utilisateurs avec cette adresse mail
        if not liste:  # Si la liste est vide, l'adresse mail n'est pas prise : retourne vrai (email disponible)
            return True
        return False  # Sinon retourne Faux (email non disponible)


class Changer_MDP(PasswordChangeForm):
    # Hérite de PasswordChangeForm
    class Meta:
        # Suit le modèle PasswordChangeForm
        model = PasswordChangeForm
        # Choix des champs : son ancien mot de passe, son nouveau mot de passe et sa confirmation
        fields = ['password1', 'password2']


class Supprimer_Profil(forms.Form):
    texte_confirmation = forms.CharField(max_length=9,  # permet de fixer un nombre maximum de caractère
                                         widget=forms.TextInput(),  # fixe le <widget
                                         help_text="Si vous voulez supprimer le compte tapez : CONFIRMER")  # permet d'afficher un texte d'aide


class Shared_Simulation(forms.ModelForm):
    class Meta:
        model = Partage_Simulation
        fields = ['destinataire']
