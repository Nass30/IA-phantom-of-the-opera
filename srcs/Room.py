#!/usr/bin/env python

class Room:
	def __init__(self, name):
		self.name = name
		self.rooms = []
		self.roomBloque = None
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

	def __str__(self):
		result = "Room " + str(self.name)
		result += " : nbCharacters = " + str(len(self.characters))
		result += " ; light = " + str(self.light)
		result += " ; room bloqued = " + ("None" if self.roomBloque == None else str(self.roomBloque)) + " [ "
		for char in self.characters:
			result += char.color + " "
		result += "]"
		return  result
