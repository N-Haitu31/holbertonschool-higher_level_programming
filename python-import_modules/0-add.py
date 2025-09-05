#!/usr/bin/python3

from add_0 import add # Importe la fonction 'add' du module 'add_0'
a = 1
b = 2
if __name__ == "__main__": # Vérifie si le script est exécuté directement
    add(a, b) # Appelle la fonction 'add' avec 'a' et 'b' comme arguments
    print("{} + {} = {}".format(a, b, add(a, b))) # Affiche le résultat de l'addition dans un format lisible
