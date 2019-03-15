#!/usr/bin/env python

class Character:
	def __init__(self, name):
		self.name = name
		self.room = None
		self.suspect = True

	def moveToRoom(self, room):
		if self.room:
			self.room.removeCharacter(self)
		self.room = room
		room.addCharacter(self)

	def describe(self):
		print "Name : " + self.name
		print "Room : " + self.room.name
