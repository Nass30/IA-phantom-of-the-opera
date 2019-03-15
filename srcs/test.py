#!/usr/bin/env python
from characters.Character import Character
from rooms.Room import Room
from party import Party
import ia.IA as IA
import time

def displayGame(game):
	for i, room in enumerate(game.rooms):
		room.display()

def main():
	print "#### Iitialisation ####"
	game = Party("Ghost")
	game.createRoom()
	chars = [Character("Nass"), Character("Mad"), Character("JD"), Character("Tony"), Character("Nassim"), Character("Imad"), Character("Jean-David"), Character("Anthony")]
	game.characters = chars
	for i, c in enumerate(chars):
		c.moveToRoom(game.rooms[i])
	print "#### Start ####"
	taro = chars[4:]
	result = IA.computeTaros(taro, game.rooms, IA.GHOST)
	print "\tMOVE::", result["perso"].name," from ", result["perso"].room.name, " to ", result["move"].name

main()
