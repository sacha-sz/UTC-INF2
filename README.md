# UTC-INF2
Contient les codes sources des TD et TP de l'UV INF2 à l'Université de Technologie de Compiègne.
Tous les codes sources sont codés en python.

Les rendus des différents TP ont été codés en jupyter notebook, il est donc recommandé d'utiliser jupyter notebook pour les exécuter.
Si vous n'avez pas jupyter notebook, vous pouvez utiliser le site https://jupyter.org/try pour exécuter les codes sources ou
github qui permet d'afficher les codes sources sans les exécuter.

## :card_index_dividers: - Arborescence du projet

```
.
├── README.md
├── LICENSE
├── TD
.   ├── TD1
.   .   ├── TD 1.pdf
.   .   ├── Autre.py
.   .   ├── TD1-1.py
.   .   ├── TD1-1-Alternatif.py
.   .   ├── TD1-2.py
.   .   ├── TD1-3.py
.   .   ├── TD1-3-Alternatif.py
.   .   ├── TD1-4.py
.   .   ├── TD1-5.py
.   .   ├── TD1-6.py
.   .   ├── TD1-7.py
.   .   ├── TD1-7-Alternatif.py
.   .   ├── TD1-8.py
.   .   └── TD1-8-Final.py
.   ├── TD2
.   .   ├── TD 2.pdf
.   .   ├── TD2-1.py
.   .   ├── TD2-2.py
.   .   ├── TD2-3.py
.   .   ├── TD2-3-Alternatif.py
.   .   └── TD2-3-suite.py
.   ├── TD3
.   .   ├── TD 3.pdf
.   .   ├── TD3-1.py
.   .   ├── TD3-1-correction.py
.   .   ├── TD3-2.py
.   .   └── TD3-2-correction.py
.   ├── TD4
.   .   ├── TD 4.pdf
.   .   ├── TD4-1.py
.   .   ├── TD4-1.1.py
.   .   ├── TD4-2.py
.   .   └── Revision.py
.   ├── TD5
.   .   ├── TD 5.pdf
.   .   ├── MyNotes.py
.   .   └── pingouin.jpg
.   ├── TD6
.   .   ├── TD6.pdf
.   .   ├── TD6-1.py
.   .   ├── TD6-2.py
.   .   └── TD6-3.py
.   ├── TD7
.   .   ├── TD7.pdf
.   .   ├── EX1.py
.   .   ├── EX2.py
.   .   ├── EX3.py
.   .   ├── affichage_graphique.py
.   .   ├── co2-annmean-mlo.csv
.   .   ├── notes.csv
.   .   └── sinus.txt
.   ├── TD8
.   .   ├── TD8.pdf
.   .   ├── EX1.py
.   .   ├── EX2.py
.   .   ├── EX3.py
.   .   ├── EX4.py
.   .   └── france.jpg
.   ├── TD9
.   .   ├── TD9.pdf
.   .   ├── EX1.py
.   .   └── BDD-exo4.sqlite
.   ├── TD11
.   .   ├── TD11.pdf
.   .   ├── gestion_cours
.   .   .   └── ...
.   .   ├── inf2
.   .   .   └── ...
.   .   ├── __init__.py
.   .   ├── manage.py
.   .   └── db_INF2.sqlite3
.   └── TD12
.   .   ├── TD12_calculVisu.pdf
.   .   ├── EX1.py
.   .   ├── EX2.py
.   .   └── EX3.py
└── TP
    ├── TP1 
    .   ├── Correction TP1
    .   .   ├── ex1.py
    .   .   ├── ex2.py
    .   .   ├── ex3.py
    .   .   ├── ex4.py
    .   .   ├── ex5.py
    .   .   └── ex6.py
    .   ├── TP1
    .   .   └── TP1.ipynb
    .   └── TP1.pdf
    ├── TP2
    .   ├── TP2.pdf
    .   └── TP2-INF2.ipynb
    ├── TP3
    .   ├── BF-latitude-longitude.png
    .   ├── PG-latitude-longitude.png
    .   ├── TP3.pdf
    .   └── TP3-INF2.ipynb
    ├── TP4
    .   ├── Image-Rapport
    .   .   ├── cercle_colore_1.png
    .   .   ├── cercle_colore_2.png
    .   .   └── courbe_cosinus.png
    .   ├── admis.txt
    .   ├── concours.txt
    .   ├── math.csv
    .   ├── math2.csv
    .   ├── TP4.pdf
    .   └── TP4-INF2.ipynb
    ├── TP5
    .   ├── Images
    .   .   ├── Ecran_accueil.png
    .   .   ├── Ecran_addition.png
    .   .   ├── Ecran_carre.png
    .   .   ├── Ecran_cos.png
    .   .   ├── Ecran_division.png
    .   .   ├── Ecran_erreur_0.png
    .   .   ├── Ecran_erreur_syntaxe.png
    .   .   ├── Ecran_erreur_syntaxe_corrige.png
    .   .   ├── Ecran_erreur_valeur.png
    .   .   ├── Ecran_multiplication.png
    .   .   ├── Ecran_puissance.png
    .   .   ├── Ecran_sin.png
    .   .   ├── Ecran_sin_pi.png
    .   .   ├── Ecran_soustraction.png
    .   .   ├── Ecran_sqrt.png
    .   .   ├── Ecran_tan.png
    .   .   └── Enonce.png
    .   ├── TP5.pdf
    .   └── TP5-INF2.ipynb
    └── TP6
        ├── TP6-INF2
        .   ├── djangoTP
        .   .   ├── __init__.py
        .   .   ├── settings.py
        .   .   ├── urls.py
        .   .   └── wsgi.py
        .   ├── pyfhn
        .   .   └── ...
        .   ├── sim_manager
        .   .   ├── __init__.py
        .   .   ├── admin.py
        .   .   ├── apps.py
        .   .   ├── migrations
        .   .   .   └── ...
        .   .   ├── models.py
        .   .   ├── tests.py
        .   .   └── views.py
        .   ├── templates
        .   .   ├── registration
        .   .   .   ├── login.html
        .   .   .   └── logout.html
        .   .   ├── base.html
        .   .   ├── change_password.html
        .   .   ├── del_user.html
        .   .   ├── edit_profile.html
        .   .   ├── graphic.html
        .   .   ├── new_profile.html
        .   .   ├── newsimu.html
        .   .   ├── simulation_list.html
        .   .   └── simulation_share.html
        .   ├── manage.py
        .   └── db.sqlite3
        ├── Configuration d environnement TP6.txt
        ├── TP6.pdf
        └── TP6-INF2.ipynb
```
## :technologist: - Langage utilisé
- [Python](https://www.python.org/)
- [HTML](https://www.wikiwand.com/fr/Hypertext_Markup_Language)
- [Jupyter Notebook](https://jupyter.org/)

## :memo: - Licence

[MIT](LICENSE)

## :notebook_with_decorative_cover: - Auteurs et contributeurs

-   **sacha-sz** - Tous les TD et TP - [sacha-sz](https://github.com/sacha-sz/)

## :bookmark_tabs: - Références
- **Lien moodle vers le cours**, (nécessite d'être connecté pour y accéder) : [UTC-INF2](https://moodle.utc.fr/course/view.php?id=2590)
