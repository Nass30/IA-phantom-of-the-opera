#!/usr/bin/env python

import partyInformations
from random import randrange

GHOST = 1
INSPECTOR = 0
BEST_MOVE = None
NUM = 0
C = ["","","","",""]

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
    check_taro(result, info.taro, info.rooms, info.number, ghost, info)
    result = BEST_MOVE
    print ("res:::", result["perso"].color, " from ", result["perso"].room.name, " to ", info.getRoom(result["move"]))
    info.result = result

def check_taro(result, taro, rooms, who, ghost, info):
    global NUM
    NUM += 1
    global C
    #print ("****check_taro::",NUM)
    #print_taro(taro)
    #print_rooms(rooms)
    #print ("who:",who, " ghost:", ghost.color if ghost else " NO")
    for i in range(len(taro)):
        new_info = info.createDeepCopy()
        character = new_info.taro[i]
        C[NUM] = character.color
        #print ("************sub_taro::",NUM, " char:",character.color)
        if NUM == 1:
            new_res = dict(result)
            new_res["perso"] = taro[i]
            new_res["tile"] = i
        else:
            new_res = result
        new_info.taro.remove(new_info.taro[i])
        check_move(character, new_res, new_info.taro, new_info.rooms, who, ghost, new_info)
    NUM -= 1
    
def check_move(character, result, taro, rooms, who, ghost, info):
    origine = character.room
    for i in range(len(character.room.rooms)):
        room = character.room.rooms[i]
        if room.name == character.room.roomBloque:
            i -= 1
            continue
        character.moveToRoom(room)
        if NUM == 1:
            new_res = dict(result)
            new_res['move'] = room.name
        else:
            new_res = result
        check_power(character, new_res, taro, rooms, who, ghost, info)
        character.moveToRoom(origine)

def check_power(character, result, taro, rooms, who, ghost, info):
    arr = {
        "gris": computeGrey,
        "bleu": computeBlue,
        "violet": computePurple,
        "rouge": computeRed,
        "rose": computePink,
        "blanc": computeWhite,
        "noir": computeBlack,
        "marron": computeBrawon
    }
    func = arr.get(character.color, None)
    if func:
        if NUM == 1:
            result['power'] = 0
            check_weight(character, result, taro, rooms, who, ghost, info)
            result['power'] = 1
            func(character, result, taro, rooms, who, ghost, info)
        else :
            check_weight(character, result, taro, rooms, who, ghost, info)
            func(character, result, taro, rooms, who, ghost, info)

def check_weight(character, result, taro, rooms, who, ghost, info):
    global BEST_MOVE
    global NUM
    if len(taro) > 0:
        if len(taro) != 2:
            who = GHOST if who == INSPECTOR else INSPECTOR
        check_taro(result, taro, rooms, who, ghost, info)
    else:
        result["weight"] = compute_weight(rooms, who, ghost)
        if result["weight"] > BEST_MOVE["weight"]:
            BEST_MOVE = result
        #print("END OF CYCLE:", C[1]," ", C[2]," ", C[3], "  cool:",result['perso'].color)
        #input()

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

def computeGrey(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = randrange(10)
    check_weight(character, result, taro, rooms, who, ghost, info)

def computeBlue(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = [0, 1]
    check_weight(character, result, taro, rooms, who, ghost, info)
    #room = self.info.rooms[randrange(len(self.info.rooms))]
    #result["lock"] = [room, room.rooms[randrange(len(room.rooms))]]

def computePurple(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = 0
    check_weight(character, result, taro, rooms, who, ghost, info)
    #result["powerResult"] = self.info.characters[randrange(len(self.info.characters))]
    
def computeRed(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = None
    check_weight(character, result, taro, rooms, who, ghost, info)

def computePink(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = None
    check_weight(character, result, taro, rooms, who, ghost, info)

def computeWhite(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = None
    check_weight(character, result, taro, rooms, who, ghost, info)

def computeBlack(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = None
    check_weight(character, result, taro, rooms, who, ghost, info)

def computeBrawon(character, result, taro, rooms, who, ghost, info):
    if NUM == 1:
        result["power_effect"] = None
    check_weight(character, result, taro, rooms, who, ghost, info)