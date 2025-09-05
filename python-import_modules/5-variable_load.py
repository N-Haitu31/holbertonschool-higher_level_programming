#!/usr/bin/python3

from variable_load_5 import a
    # importe la variable 'a' qui est définie dans un autre fichier appelé 'variable_load_5.py'

def main():
    # C'est la définition d'une fonction nommée 'main'
    # On met souvent le code principal d'un programme dans une fonction 'main' pour une meilleure organisation
    print(a)
        # Cette ligne affiche la valeur de la variable 'a' qui a été importée.

if __name__ == "__main__":
    # Cette condition vérifie si le script est exécuté directement.
    # Le code à l'intérieur de ce bloc ne s'exécutera que si le fichier est le programme principal,
    # et non s'il est importé par un autre fichier. C'est une bonne pratique de programmation.
    main()
        # Cette ligne appelle la fonction 'main' pour démarrer l'exécution du programme.
