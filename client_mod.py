#!/usr/bin/python3

import socket

cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnx.connect(("localhost", 7777))

part = cnx.recv(1024).decode("UTF-8")
print("Veuillez entrer le \"", part, "\" :", sep="", end=" ")
phr = input()
cnx.send(bytes(phr, "UTF-8"))

phr = cnx.recv(1024).decode("UTF-8")
print("La phrase est : \"", phr, "\".", sep="")

cnx.close()


