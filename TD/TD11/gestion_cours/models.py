from django.db import models


# Create your models here.

class Bureau(models.Model):
    """
    Permet de faire le lien avec la BDD - création de la table Bureau
    """
    centre = models.CharField(max_length=2, null=False)
    batiment = models.CharField(max_length=2, null=False)
    salle = models.IntegerField(null=False)

    class Meta: # rajoute des contraintes supplémentaires
        constraints = [
            models.UniqueConstraint(fields=["centre", "batiment", "salle"], name="Contrainte d'unicité du bureau")
        ]

    def __str__(self):
        return f'{self.centre}-{self.batiment}{self.salle}'


class Intervenant(models.Model):
    """
    Permet de faire le lien avec la BDD - création de la table Intervenant
    """
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=25, null=False)
    telephone = models.CharField(max_length=15)
    Bureau = models.ForeignKey(Bureau, on_delete=models.SET_NULL, related_name='personnes', null=True)

    class Meta: # rajoute des contraintes supplémentaires
        constraints = [
            models.UniqueConstraint(fields=["nom", "prenom"], name="Contrainte d'unicité d'une personne")
        ]

    def __str__(self):
        return f'{self.prenom}-{self.nom}'


class Etudiant(models.Model):
    """
    Permet de faire le lien avec la BDD - création de la table Etudiant
    """
    nom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=25, null=False)
    INE = models.IntegerField(null=False)
    niveau = models.IntegerField(max_length=4, null=False)

    class Meta: # rajoute des contraintes supplémentaires
        constraints = [
            models.UniqueConstraint(fields=["INE"], name="Contrainte d'unicité d'un étudiant")
        ]

    def __str__(self):
        return f'{self.prenom}-{self.nom}'


class Est_inscrit(models.Model):
    """
    Permet de faire le lien avec la BDD - création de la table Est_inscrit
    """
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, null=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=False)
    TP = models.ForeignKey(TD, on_delete=models.CASCADE, null=False)
    TD = models.ForeignKey(TP, on_delete=models.CASCADE, null=False)


class Cours(models.Model):
    """
    Permet de faire le lien avec la BDD - création de la table Cours
    """
    ID = models.CharField(max_length=4, null=False)
    nom = models.CharField(null=False)
    description = models.TextField(max_length=500)
    semestre = models.CharField(max_length=1, null=False)

    responsable = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, related_name='aucun', null=True)

    etudiant = models.ManyToManyField(Etudiant, through=Est_inscrit)

    class Meta: # rajoute des contraintes supplémentaires
        constraints = [
            models.UniqueConstraint(fields=["ID"], name="Contrainte d'unicité d'un étudiant")
        ]

    def __str__(self):
        return f"{self.ID}-{self.nom}"
