#!/usr/bin/env python
from characters.Character import Character
from rooms.Room import Room

class Party:
	def __init__(self, playerType):
		self.playerType = playerType
		self.carlota = 4
		self.endCarlota = 22
		self.rooms = []
		self.createRoom()

	def createRoom(self):
		self.rooms = [Room(0), Room(1), Room(2), Room(3), Room(4), Room(5), Room(6), Room(7), Room(8), Room(9)]

		passages = [{1,4},{0,2},    {1,3},  {2,7},{0,5,8},  {4,6},      {5,7},      {3,6,9},    {4,9},  {7,8}]
		pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},  {5,7,2,9},  {3,6,9,1},  {4,9,5},{7,8,4,6}]

		for index, room in enumerate(self.rooms):
			for otherRoom in passages[index]:
				room.addRoom(self.rooms[otherRoom])
			for otherRoom in pass_ext[index]:
				room.addExtendedRoom(self.rooms[otherRoom])

party = Party("GHOST")

