#!/usr/bin/python3

import socket
from select import select
import random as rd

cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnx.bind(('', 7777))
cnx.listen(5)

parts = [u"Sujet", u"Adjectif", u"Verbe", u"Adverbe", u"Complément d'objet", u"Complément circonstanciel"]

class Client:
	cnx # Connection
	part = 0 # Partie dont il s'occupe

clients = []
nb = 0
selecteds = []

def connect_one():
	global nb, selected, clients

	cnx_cli, infos_cli = cnx.accept()
	print("Connection accepted :", infos_cli)
	nb += 1
	client = Client()
	client.cnx = cnx_cli

	valid = False
	while not valid:
		valid = True
		part = rd.randint(0,5)
		for i in selecteds:
			if i == part:
				valid = False
	client.part = part
	selecteds.append(part)

	client.cnx.send(bytes(parts[client.part], "UTF-8"))

	clients.append(client)

def readSelect():
	ret = [cnx]
	for i in clients:
		ret.append(i.cnx)
	return ret

def isIn(lst, value):
	for i in lst:
		if i == value:
			return True
	return False

begin = True
recvs = ["", "", "", "", "", ""]
recvnb = 0
print("***** Nouvelle partie *****")
while True:
	rlst = readSelect()
	rlst, wlst, xlst = select(rlst, [], [])

	if isIn(rlst, cnx) and nb < 6:
		connect_one()
	else:
		for client in clients:
			if isIn(rlst, client.cnx):
				buf = client.cnx.recv(1024)
				recvs[client.part] = buf.decode("UTF-8")
				recvnb = recvnb + 1
	
	if recvnb >= 6:
		phr = ""
		for i in range(6):
			phr += recvs[i];
			if i == 5:
				phr += "."
			else:
				phr += " "
		for client in clients:
			client.cnx.send(bytes(phr, "UTF-8"))
			client.cnx.close()
		# Remise à zéro
		clients = []
		nb = 0
		selected = []
		begin = True
		recvs = ["", "", "", "", "", ""]
		recvnb = 0
		print("***** Nouvelle partie *****")

cnx.close()

