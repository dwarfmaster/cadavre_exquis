#!/usr/bin/python3

import socket
cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(hostname):
	global cnx
	cnx.connect((hostname, 7777))

def getPart():
	global cnx
	return cnx.recv(1024).decode("UTF-8")

def sendPart(string):
	global cnx
	cnx.send(bytes(string, "UTF-8"))

def end():
	global cnx
	phr = cnx.recv(1024).decode("UTF-8")
	cnx.close()
	return phr


