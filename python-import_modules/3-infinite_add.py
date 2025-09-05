#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0")  # Affiche '0' si aucun argument n'est passé
    else:
        total = 0
        for i in argv[1:]:  # Parcourt tous les arguments à partir de argv[1]
            total += int(i)
        print(total)  # Affiche le total de la somme
