#!/usr/bin/env python

import copy 

GHOST = 1
INSPECTOR = 0
WHO = GHOST

def computeTaros(taros, rooms, who):
        global WHO
        WHO = who
        result = {"perso":None, "move":None, "weight":-1}
	for taro in taros:
                result = computeCharacter(taro, rooms, result)
        return result

def computeCharacter(char, rooms, last_result):
        origin_room = char.room
        result = copy.copy(last_result)
        for character_room in char.room.rooms:
                #print char.color, " from ", char.room.name, " to ", character_room.name
                char.moveToRoom(character_room)
                t_weight = computeWeight(rooms)
                #print " weight ", t_weight
                if t_weight > result["weight"]:
                        result["perso"] = char
                        result["move"] = char.room
                        result["weight"] = t_weight
                char.moveToRoom(origin_room)
        return result

def computeWeight(rooms):
        nb_alone = 0
        nb_grp = 0
        for room in rooms:
                if len(room.characters) == 1:
                        nb_alone += 1 if room.characters[0].suspect else 0
                else:
                        nb_grp += len([char for char in room.characters if char.suspect])
        weight = abs(nb_alone-nb_grp)
        return weight if WHO == GHOST else (10 - weight)
                
