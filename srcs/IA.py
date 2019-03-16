#!/usr/bin/env python

import copy 
import partyInformations
from random import randrange

class IA:
    def __init__(self, info):
        self.info = info
        self.deep = 1

    def compute(self):
        result = {"tile":0, "perso":None, "move":None, "power":0, "weight":-1, "lock":0, "light":0}
        for i in range(len(self.info.taro)):
            result = self.computeCharacter(self.info.taro, i, self.info.rooms, result)
        self.computeLight(result)
        self.computeLight(result)
        self.info.result = result

    def computeCharacter(self, taro, tile, rooms, last_result):
        char = taro[tile]
        origin_room = char.room
        result = copy.copy(last_result)
        for character_room in char.room.rooms:
            #print char.color, " from ", char.room.name, " to ", character_room.name
            char.moveToRoom(character_room)
            t_weight = self.computeWeight(rooms)
            #print " weight ", t_weight
            if t_weight > result["weight"]:
                result["perso"] = char
                result["tile"] = tile
                result["move"] = char.room
                result["weight"] = t_weight
                char.moveToRoom(origin_room)
        return result

    def computeWeight(self,rooms):
        nb_alone = 0
        nb_grp = 0
        for room in rooms:
            if len(room.characters) == 1:
                nb_alone += 1 if room.characters[0].suspect else 0
            else:
                nb_grp += len([char for char in room.characters if char.suspect])
        weight = abs(nb_alone-nb_grp)
        return weight if self.info.number == partyInformations.GHOST else (10 - weight)
                
    def computeLight(self, result):
        result["light"] = randrange(10)

    def computeLock(self, result):
        room = self.info.rooms[randrange(len(self.info.rooms))]
        result["lock"] = [room, room.rooms[randrange(len(room.rooms))]]

    def computePurple(self, result):
        result["power"] = self.info.characters[randrange(len(self.info.characters))]
