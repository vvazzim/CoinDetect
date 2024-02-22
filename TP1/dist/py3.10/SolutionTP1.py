import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def blackout(width, height):
    return np.zeros((height, width))

def see_points(width, height, points):
    # Créer une image noire
    img = blackout(width, height)

    # Parcourir la liste des points et mettre la valeur de ces points à 1
    for point in points:
        img[point[0], point[1]] = 1

    return img

def see_quadrant(image_name, quadrant):
    # Ouvrir l'image et la convertir en tableau numpy
    img = np.array(Image.open(image_name))

    # Obtenir les dimensions de l'image
    height, width = img.shape

    # Déterminer le centre du quadrant spécifié
    if quadrant == 'top_left':
        center = (height // 4, width // 4)
    elif quadrant == 'top_right':
        center = (height // 4, 3 * width // 4)
    elif quadrant == 'bottom_left':
        center = (3 * height // 4, width // 4)
    elif quadrant == 'bottom_right':
        center = (3 * height // 4, 3 * width // 4)

    # Normaliser l'image entre 0 et 255 et retourner la valeur du pixel au centre du quadrant
    img = (img / img.max()) * 255
    return int(img[center])

# fonction renvoie une image de taille width x height, cette image est noir sauf pour les lignes de la liste lines
def see_lines(width, height, lines):
    blackImage = blackout(width, height)
    for line in lines:
        if line[0] == line[2]:  # ligne horizontale
            blackImage[line[0], line[1]:line[3]] = 1
        else:
            blackImage[line[0]:line[2], line[1]] = 1

    return blackImage

#La fonction doit renvoyer l'image produite (en float, avec des valeurs entre 0 et 1).
def see_quadrant_complete(image_name, quadrant):
    # Chargement de l'image en mémoire
    import matplotlib.image as mplimg

    img = mplimg.imread(image_name).copy()

    # Calcul des coordonnées du centre du quadrant
    i = int(img.shape[0] / 4)
    if quadrant.startswith('bottom'):
        i = int(img.shape[0] * 3 / 4)
    j = int(img.shape[1] / 4)
    if quadrant.endswith('right'):
        j = int(img.shape[1] * 3 / 4)

    # Création d'une nouvelle image pour la modification
    img2 = np.empty(img.shape + (3,))

    # Copie de l'image d'origine dans la nouvelle image
    for c in range(3):
        img2[:, :, c] = img

    # Dessin d'une ligne rouge verticale au centre de l'image
    for i2 in range(img2.shape[0]):
        img2[i2, int(img2.shape[1] / 2)] = [1, 0, 0]

    # Dessin d'une ligne rouge horizontale au centre de l'image
    for i2 in range(img2.shape[1]):
        img2[int(img2.shape[0] / 2), i2] = [1, 0, 0]

    # Dessin d'un carré bleu de 7x7 centré sur le pixel à lire
    for i2 in range(-3, 4):
        for j2 in range(-3, 4):
            img2[int(i + i2), int(j + j2)] = [0, 0, 1]

    # Dessin des lignes rouges qui séparent les quadrants
    for i2 in range(img2.shape[0]):
        img2[i2, int(img2.shape[1] / 2)] = [1, 0, 0]
    for i2 in range(img2.shape[1]):
        img2[int(img2.shape[0] / 2), i2] = [1, 0, 0]

    return img2