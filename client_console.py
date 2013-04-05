#!/usr/bin/python3

import client_mod as lce

host = input("Entrez l'adresse du serveur :")
lce.connect(host)

print("Veuillez entrer le \"", lce.getPart(), "\" :", sep="", end=" ")
lce.sendPart(input())
print("La phrase est : \"", lce.end(), "\".", sep="")



