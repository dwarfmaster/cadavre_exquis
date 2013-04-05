#!/usr/bin/python3

from tkinter import *
import client_mod as lce

class Interface(Frame):
	def __init__(self, screen, **kwargs):
		Frame.__init__(self, screen, **kwargs)
		self.pack(fill=BOTH)
		self.screen = screen
		
		# Le label
		self.lab = Label(screen, text="Hostame :")
		self.lab.pack(side=TOP, fill=X)

		# L'entrée
		self.entry = StringVar()
		self.entryw = Entry(screen, textvariable = self.entry)
		self.entryw.pack(fill=X)

		# Le bouton
		self.but = Button(self, text="Valider", command=self.connect)
		self.but.pack(side=BOTTOM)

	def connect(self):
		lce.connect(self.entry.get())
		part = lce.getPart()
		self.but["command"] = self.send;
		self.entryw.delete(0, len(self.entry.get()))
		self.lab["text"] = part

	def send(self):
		lce.sendPart(self.entry.get())
		self.lab["text"] = "Veuillez patienter ..."
		self.but.pack_forget()
		self.entryw.pack_forget()
		self.screen.after(100, self.receive)

	def receive(self):
		phr = lce.end()
		self.lab["text"] = "Phrase : \"" + phr + "\"."
		self.but["text"] = "Quitter"
		self.but["command"] = self.screen.quit
		self.but.pack(side=BOTTOM)

screen = Tk()
interface = Interface(screen)

interface.mainloop()
interface.destroy()

