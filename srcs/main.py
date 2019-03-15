#!/usr/bin/env python
from Character import Character
from Room import Room
import IA

class MainIA:
	def __init__(self):
		self.rooms = []
		self.characters = []
		self.createRooms()
		self.createCharacters()

	def mainLoop(self):
		turn = [IA.GHOST, IA.INSPECTOR, IA.INSPECTOR, IA.GHOST]
		taro = self.characters[4:]
		for i in range(len(taro)):
			result = IA.computeTaros(taro, self.rooms, turn[i])
			print "\t", turn[i] ,"MOVE::", result["perso"].color," from ", result["perso"].room.name, " to ", result["move"].name
			result["perso"].moveToRoom(result["move"])
			taro.remove(result["perso"])
		return

	def createRooms(self):
		self.rooms = [Room(0), Room(1), Room(2), Room(3), Room(4), Room(5), Room(6), Room(7), Room(8), Room(9)]

		passages = [{1,4},{0,2},    {1,3},  {2,7},{0,5,8},  {4,6},      {5,7},      {3,6,9},    {4,9},  {7,8}]
		pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},  {5,7,2,9},  {3,6,9,1},  {4,9,5},{7,8,4,6}]

		for index, room in enumerate(self.rooms):
			for otherRoom in passages[index]:
				room.addRoom(self.rooms[otherRoom])
			for otherRoom in pass_ext[index]:
				room.addExtendedRoom(self.rooms[otherRoom])

	def createCharacters(self):
		characters_name = ["Lufi", "Naruto", "Gintama", "Gon", "Yusuke", "Hippo", "Elric", "Nassim"]
		for i, character_name in enumerate(characters_name):
			self.characters.append(Character(character_name, True, self.rooms[i]))

	def displayGame(self):
		for room in self.rooms:
			print room


def main():
	game = MainIA()
	game.mainLoop()

if __name__ == "__main__":
    main()