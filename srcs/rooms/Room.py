#!/usr/bin/env python

class Room:
	def __init__(self, name):
		self.name = name
		self.rooms = []
		self.light = True
		self.characters = []

	def addRoom(self, room):
		self.rooms.append(room)

	def addCharacter(self, character):
		self.characters.append(character)

	def getCharacters(self):
		return self.characters
