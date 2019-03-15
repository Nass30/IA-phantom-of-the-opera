#!/usr/bin/env python
from characters import Character
from rooms import Room
import parsing

class MainIA:
	def __init__(self):
		self.parser = parsing.Parser()
		self.createRooms()
		self.createCharacters()
		self.mainLoop()

	def mainLoop(self):
		while (1):
			self.characters[0].describe()
		return

	def createRooms(self):
		self.rooms = [Room("Tech")]

	def createCharacters(self):
		anthony = Character("Anthony")
		anthony.moveToRoom(self.rooms[0])
		self.characters = [anthony]

ia = MainIA()