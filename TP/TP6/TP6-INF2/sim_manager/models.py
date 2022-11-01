from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Simulation(models.Model):
    user_creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_id")  # Changement du nom
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    alpha = models.FloatField(validators=[MinValueValidator(0.08), MaxValueValidator(0.12)],)
    beta = models.FloatField(validators=[MinValueValidator(0.4), MaxValueValidator(0.6)],)
    gamma = models.FloatField(validators=[MinValueValidator(0.04), MaxValueValidator(0.06)],)
    delta = models.FloatField(validators=[MinValueValidator(0.008), MaxValueValidator(0.012)],)
    epsilon = models.FloatField(validators=[MinValueValidator(0.08), MaxValueValidator(0.12)],)
    is_favorite = models.BooleanField(default=False) # Ajout d'une valeur booléenne


class Partage_Simulation(models.Model):
    # Création de la table

    # Stocke les clés primaires de l'expéditeur, du destinataire et de la simulation
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="expediteur", null=True)
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinataire", null=True)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name="simulation_shared_id", null=True)