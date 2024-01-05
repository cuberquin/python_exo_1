import math
import tkinter as tk
from tkinter import *
import pprint
import sys

def saisir_le_nom_du_prof() :
    possible_nom_du_prof = input("Entrez le nom du prof :")
    for chiffre in range(0,9):
        if str (chiffre) in possible_nom_du_prof:
            sys.exit("nom incorrect")
    return possible_nom_du_prof

def saisir_notes() :
    list = []
    len(list)
    max_notes=5
    while len(list) < max_notes:
        possible_note = input(f"Entrez la valeur de la note {len(list)+1}/{max_notes}:")
        try:
            note = float(possible_note)
        except ValueError:
            print("Saisie incorrecte")
            continue

        if note < 0 or note > 20 :
            print("note incorrect")
            continue
        list.append(note)
    return list

#debut du programme
list_des_profs = {}
prof = saisir_le_nom_du_prof()
classe = input("entrer le nom de la classe")
list_des_profs [prof] =  {classe:saisir_notes()}
pprint.pprint(list_des_profs)

for prof in list_des_profs :
    for classe in list_des_profs [prof] :
        listes_des_notes =  list_des_profs [prof][classe]
        moyenne = sum(listes_des_notes) / len(listes_des_notes)
        print(f"La moyenne des notes de la {classe} du prof {prof} est de : {moyenne}")
        message = f"La moyenne de la classe {classe} est "
        if  moyenne < 10 :
            message += " decevante"
        else :
            message += "bonne"
        print(message)