#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1 # Compte les arguments, exclut le nom du script 'argv[0]'

    # Vérifiez le nombre d'arguments
    if count == 0:
        print("0 arguments.") # Affiche si aucun argument n'est passé

    elif count == 1:
        print("1 argument:") # Affiche pour un seul argument
        print("1: {}".format(argv[1])) # Affiche l'argument avec sa position

    else:
        print("{} arguments:".format(count)) # Affiche le nombre d'arguments
        for i in range(1, len(argv)): # Commencez à l'index 1 pour ignorer le nom du script
            print("{}: {}".format(i, argv[i])) # Affiche chaque argument avec sa position
