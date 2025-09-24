
# Le code ci-dessous est requis pour lire le fichier CSV
# Ne modifier qu'avec un accord collégial

import csv

données = "isbn_fantasy.csv"
livres = []

# Lis le fichier csv puis stock chaque ligne comme un dictionnaire dans la liste "livres"
with open(données, mode="r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=",", quotechar='"') 
    for ligne in lecteur:
        livres.append(ligne)

# Clés des dictionnaires:
# "isbn", "title", "editeur", "nb_page", "classification_decitre_1", "classification_decitre_2", "classification_decitre_3"
# Tous les champs sont des chaînes de caractères.
# Ajouter les fonctionnalitées en dessous.

for i in range(3):
    print(livres[i])
