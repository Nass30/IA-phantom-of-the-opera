#!/usr/bin/env python

import copy 
import partyInformations
from random import randrange

class IA:
    def __init__(self, info):
        self.info = info
        self.deep = 1

    def compute(self):
        result = {"tile":0, "perso":None, "move":None, "power":0, "weight":-1, "lock":0, "light":0, "powerResult":0}
        print ("taro:", self.info.taro)
        for i in range(len(self.info.taro)):
            result = self.computeCharacter(self.info.taro, i, self.info.rooms, result)
        self.computePower(result)
        self.info.result = result

    def computeCharacter(self, taro, tile, rooms, last_result):
        char = taro[tile]
        origin_room = char.room
        result = copy.copy(last_result)
        for character_room in char.room.rooms:
            char.moveToRoom(character_room)
            t_weight = self.computeWeight(rooms)
            print ("t_weight ", t_weight)
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
        if self.info.number == partyInformations.GHOST:
            return nb_alone if len(self.info.getPersoFromColor(self.info.fantome).room.characters) == 1 else nb_grp
        return (10 - abs(nb_alone-nb_grp))

    def computePower(self, result):
        arr = {
            "grey": self.computeGrey(result),
            "blue": self.computeBlue(result),
            "purple": self.computePurple(result),
            "red": self.computeRed(result),
            "pink": self.computePink(result),
        }
        func = arr.get(result['perso'].color, None)
        if func:
            func(result)

    def computeGrey(self, result):
        result["power"] = 1
        result["light"] = randrange(10)

    def computeBlue(self, result):
        result["power"] = 1
        room = self.info.rooms[randrange(len(self.info.rooms))]
        result["lock"] = [room, room.rooms[randrange(len(room.rooms))]]

    def computePurple(self, result):
        result["power"] = 1
        result["powerResult"] = self.info.characters[randrange(len(self.info.characters))]
    
    def computeRed(self, result):
        result["power"] = 1

    def computePink(self, result):
        result["power"] = 1

    
