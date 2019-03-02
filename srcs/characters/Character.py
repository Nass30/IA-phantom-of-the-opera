#!/usr/bin/env python

class Character:
	def __init__(self, name):
		self.name = name
		self.room = None

	def moveToRoom(self, room):
		self.room = room
		room.addCharacter(self)

	def describe(self):
		print "Name : " + self.name
		print "Room : " + self.room.name
