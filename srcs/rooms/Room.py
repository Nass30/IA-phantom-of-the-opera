#!/usr/bin/env python

class Room:
	def __init__(self, name):
		self.name = name
		self.rooms = []
		self.extendedRooms = []
		self.light = True
		self.characters = []

	def addRoom(self, room):
		self.rooms.append(room)

	def addExtendedRoom(self, room):
		self.extendedRooms.append(room)

	def addCharacter(self, character):
		self.characters.append(character)

	def removeCharacter(self, character):
		self.characters.remove(character)

	def display(self):
		print "Room ", self.name, " :"
		for i, c in enumerate(self.characters):
			print "\t", c.name, "suspect" if c.suspect else "inocent"
