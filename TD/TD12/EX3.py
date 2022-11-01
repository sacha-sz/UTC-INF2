import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def main():
    # image couleur
    face_c= misc.face()
    plt.imshow(face_c)
    plt.show()

    print(type(face_c), face_c.shape)  # tableau 3D
    face = misc.face(gray=True)  # niveau de gris
    plt.imshow(face, cmap=plt.cm.gray)  # affiche en niveau de gris
    plt.show()
    print(type(face), face.shape)  # tableau 2D

    # # Cropping méthode 1
    # hauteur_crop = face_c.shape[0] // 2
    # largeur_crop = face_c.shape[1] // 2
    #
    # pos_x = face_c.shape[0] // 4
    # pos_y = face_c.shape[1] // 4
    #
    # positionnement_x_min = largeur_crop - pos_y
    # positionnement_x_max = largeur_crop + pos_y
    # positionnement_y_min = hauteur_crop - pos_x
    # positionnement_y_max = hauteur_crop + pos_x
    #
    # img_crop = face_c[positionnement_y_min:positionnement_y_max, positionnement_x_min:positionnement_x_max]
    # plt.imshow(img_crop)
    # plt.show()

    # Cropping méthode 2
    h_4 = face_c.shape[0] // 4
    l_4 = face_c.shape[1] // 4

    img_crop = face_c[h_4:-h_4, l_4:-l_4]
    plt.imshow(img_crop)
    plt.show()

    # Contrastes
    img_nb_contraste = np.array(img_crop)
    img_nb_contraste[img_nb_contraste >= 200] = 255
    img_nb_contraste[img_nb_contraste < 55] = 0
    plt.imshow(img_nb_contraste)
    plt.show()

    # Histogramme
    plt.hist(img_nb_contraste.ravel(), bins=256)
    plt.show()


if __name__ == '__main__':
    main()