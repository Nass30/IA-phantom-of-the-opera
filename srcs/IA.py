#!/usr/bin/env python

import partyInformations
from random import randrange

GHOST = 1
INSPECTOR = 0
BEST_MOVE = None
NUM = 0

def print_taro(taro):
    res = '\ttaro :[ '
    for t in taro:
        res += t.color + " "
    print (res, "] ")

def print_rooms(room):
    res = '\trooms :[\n'
    for r in room:
        res += "\t\t" + str(r.name) + " :"
        for c in r.characters:
            res += " " + c.color
        res += "\n"
    print (res, "\t]")

def compute(info):
    global BEST_MOVE
    result = {"tile":0, "perso":None, "move":None, "power":-1, "weight":-1}
    BEST_MOVE = dict(result)
    ghost = info.getFantome()
    check_taro(result, info.taro, info.rooms, info.number, ghost)
    print ("res:::", result["perso"].color, " from ", result["perso"].room.name, " to ", result["move"].name)
    info.result = result

def check_taro(result, taro, rooms, who, ghost):
    print ("****check_taro::",NUM)
    print_taro(taro)
    print_rooms(rooms)
    print ("who:",who, " ghost:", ghost.color if ghost else " NO")
    for i in range(len(taro)):
        character = taro[i]
        print ("************sub_taro::",NUM, " char:",character.color)
        if result["perso"] == None:
            result["perso"] = character
            result["tile"] = character
        copy = list(taro)
        copy.remove(character)
        check_move(character, result, copy, rooms, who, ghost)

def check_move(character, result, taro, rooms, who, ghost):
    origine = character.room
    for room in character.room.rooms:
        if room.name == character.room.roomBloque:
            continue
        character.moveToRoom(room)
        if result['move'] == None:
            result['move'] = room
        check_power(character, result, taro, rooms, who, ghost)
        character.moveToRoom(origine)

def check_power(character, result, taro, rooms, who, ghost):
    global BEST_MOVE
    global NUM
    if result['power'] == -1:
        result['power'] = 0
    #computePower(character)
    if len(taro) > 0:
        if len(taro) != 2:
            who = GHOST if who == INSPECTOR else INSPECTOR
        NUM += 1
        check_taro(result, taro, rooms, who, ghost)
    else:
        NUM = 0
        result["weight"] = compute_weight(rooms, who, ghost)
        if result["weight"] > BEST_MOVE["weight"]:
            BEST_MOVE = result

def compute_weight(rooms, who, ghost):
    nb_alone = 0
    nb_grp = 0
    for room in rooms:
        if len(room.characters) == 1:
            nb_alone += 1 if room.characters[0].suspect else 0
        else:
            nb_grp += len([char for char in room.characters if char.suspect])
    if who == GHOST:
        if ghost:
            return nb_alone if len(ghost.room.characters) == 1 else nb_grp
        else:
            return abs(nb_alone-nb_grp)
    return (10 - abs(nb_alone-nb_grp))

def computePower(result):
    arr = {
        "grey": computeGrey(result),
        "blue": computeBlue(result),
        "purple": computePurple(result),
        "red": computeRed(result),
        "pink": computePink(result),
    }
    func = arr.get(result['perso'].color, None)
    if func:
        func(result)

def computeGrey(result):
    result["power"] = 1
    result["light"] = randrange(10)

def computeBlue(result):
    result["power"] = 1
    #room = self.info.rooms[randrange(len(self.info.rooms))]
    #result["lock"] = [room, room.rooms[randrange(len(room.rooms))]]

def computePurple(result):
    result["power"] = 1
    #result["powerResult"] = self.info.characters[randrange(len(self.info.characters))]
    
def computeRed(result):
    result["power"] = 1

def computePink(result):
    result["power"] = 1

    
