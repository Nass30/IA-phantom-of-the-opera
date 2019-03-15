#!/usr/bin/env python

import copy 

WEIGHT = 0
GHOST = 1
INSPECTOR = 0
WHO = GHOST
RESULT = {"perso":None, "move":None}

def computeTaros(taros, rooms, who):
        global WHO
        WHO = who
	for taro in taros:
                computeCharacter(taro, rooms)
        return RESULT

def computeCharacter(char, rooms):
        global RESULT
        global WEIGHT
        origin_room = char.room
        for character_room in char.room.rooms:
                char.moveToRoom(character_room)
                t_weight = computeWeight(rooms)
                if t_weight > WEIGHT:
                        RESULT["perso"] = char
                        RESULT["move"] = char.room
                        WEIGHT = t_weight
                char.moveToRoom(origin_room)

def computeWeight(rooms):
        nb_inocent = 0
        nb_unknown = 0
        for room in rooms:
                if len(room.characters) == 1:
                        nb_inocent += 1 if room.characters[0].suspect else 0
                else:
                        nb_unknown += len([char for char in room.characters if char.suspect])
        weight = abs(nb_inocent-nb_unknown)
        return weight if WHO == GHOST else (8 - weight)
                
