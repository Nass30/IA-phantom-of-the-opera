#!/usr/bin/env python

class Character:
	def __init__(self, color, suspect, room):
		self.color = color
		self.room = None
		self.moveToRoom(room)
		self.suspect = suspect

	def moveToRoom(self, room):
		if self.room != None:
			self.room.removeCharacter(self)
		self.room = room
		room.addCharacter(self)

	def __str__(self):
		return "Character " + self.color + " in Room " + str(self.room.name) + (" is suspect" if self.suspect == True else " is clear")