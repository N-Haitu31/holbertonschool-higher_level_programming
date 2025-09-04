#!/usr/bin/python3
def uppercase(str):
    for c in str:

        # Cette condition vérifie si le caractère 'c' est une lettre minuscule
        if 'a' <= c <= 'z':

            # ord(c) convertit la lettre minuscule en son code (ASCII)
            # En soustrayant 32, on obtient le code de sa version majuscule
            # chr(...) reconvertit ce code numérique en un car. majuscule
            c = chr(ord(c) - 32)

        print("{:s}".format(c), end="")
        # {:s} est un format pour les chaînes
        # end="" empêche l'impression d'un saut de ligne par défaut
        # ce qui permet d'afficher tous les caractères sur une seule ligne

    print()
