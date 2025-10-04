#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            liste_dicts = []

            for ligne in reader:
                liste_dicts.append(ligne)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(liste_dicts, json_file, indent=4)

        return True
    except Exception:
        return False
