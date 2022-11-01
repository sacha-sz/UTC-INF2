import numpy as np
import matplotlib.pyplot as plt


def affiche_camenbert(lab, valeurs, titre):
    plt.figure(figsize=(8, 8))  # image de 800 x 800
    plt.title(titre)
    plt.pie(valeurs, labels= lab, autopct = "%0.2f%%")  # pourcentage avec 2 chiffres apres la virgule
    plt.show()
 #   plt.savefig('figures/camembert.png')


def affiche_histo(list_x, list_y, titre, xlab, ylab):
    x = np.array(list_x)
    y = np.array(list_y)
    plt.title(titre)
    x_pos = np.linspace(1, len(x), len(x))
    bc = plt.bar(x_pos, y, color='blue')
    plt.xticks(x_pos, x)
    plt.ylabel(ylab)
    plt.xlabel(xlab)
 #   plt.savefig('figures/programming_langages.png')
    plt.show()


def affiche_courbe(list_x, list_y, titre, xlab, ylab):
    '''
    affichage d'une courbe simple
    :param list_x: liste contenant les valeurs en abscisse
    :param list_y: liste contenant les valeurs en ordonnée
    :param titre: titre de la figure
    :param xlab: x label
    :param ylab: y label
    :return: None
    '''
    plt.plot(list_x, list_y)
    plt.title(titre)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
 #   plt.savefig('figures/courbe.png')
    plt.show()

