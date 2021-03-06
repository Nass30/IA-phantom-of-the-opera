from Character import Character
from Room import Room

GHOST = 1
INSPECTOR = 0

class PartyInformations:
    def __init__(self, number):
        self.number = number
        self.tourNumber = 1
        self.rooms = []
        self.salleOmbre = None
        self.roomBloque1 = None
        self.roomBloque2 = None
        self.createRoom()
        self.characters = []
        self.carlota = 4
        self.maxCarlota = 22
        self.fantome = None
        self.taro = []

    def copyTaro(self, taro):
        res = []
        for char in self.characters:
            for t in taro:
                if t.color == char.color:
                    res.append(char)
        return res

    def getRoom(self, name):
        for room in self.rooms:
            if room.name == name:
                return room
        return None

    def createDeepCopy(self):
        new = PartyInformations(self.number)
        new.update(self.tourNumber, self.carlota, self.maxCarlota, self.salleOmbre, self.roomBloque1, self.roomBloque2)
        new.fantome = self.fantome
        for character in self.characters:
            for room in new.rooms:
                if room.name == character.room.name:
                    newChar = Character(character.color, character.suspect, room)
                    new.characters.append(newChar)
                    break
        new.taro = []
        for t in self.taro:
            char = new.getPersoFromColor(t.color)
            new.taro.append(char)
        return new

    def createRoom(self):
        self.rooms = [Room(0), Room(1), Room(2), Room(3), Room(4), Room(5), Room(6), Room(7), Room(8), Room(9)]

        passages = [{1,4},{0,2},    {1,3},  {2,7},{0,5,8},  {4,6},      {5,7},      {3,6,9},    {4,9},  {7,8}]
        pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},  {5,7,2,9},  {3,6,9,1},  {4,9,5},{7,8,4,6}]

        for index, room in enumerate(self.rooms):
            for otherRoom in passages[index]:
                room.addRoom(self.rooms[otherRoom])
            for otherRoom in pass_ext[index]:
                room.addExtendedRoom(self.rooms[otherRoom])

    def obscurcirRoom(self, numero):
        self.salleOmbre = numero
        for room in self.rooms:
            if room.name == numero:
                room.light = False
            else:
                room.light = True

    def update(self, tourNumber, carlota, maxCarlota, salleOmbre, room1, room2):
        self.tourNumber = tourNumber
        self.carlota = carlota
        self.maxCarlota = maxCarlota
        self.obscurcirRoom(salleOmbre)
        self.bloquePassage(room1, room2)

    def updateCharacter(self, color, numberRoom, suspect):
        for character in self.characters:
            if character.color == color:
                character.suspect = suspect
                room = self.rooms[numberRoom]
                character.moveToRoom(room)
                return
        self.characters.append(Character(color, suspect, self.rooms[numberRoom]))

    def bloquePassage(self, room1, room2):
        self.roomBloque1 = room1
        self.roomBloque2 = room2
        for room in self.rooms:
            room.roomBloque = None
        self.rooms[room1].roomBloque = room2
        self.rooms[room2].roomBloque = room1

    def getPersoFromColor(self, color):
        for char in self.characters:
            if char.color == color:
                return char
        return None

    def getFantome(self):
        for char in self.characters:
            if char.color == self.fantome:
                return char
        return None

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        result = ""
        if self.fantome != None:
            result += "fantome = " + self.fantome + '\n'
        result += "Tour number : " + str(self.tourNumber) + "\n"
        result += "Carlota : " + str(self.carlota) + "/" + str(self.maxCarlota) + "\n"
        for c in self.characters:
            result += str(c) + "\n"
        for r in self.rooms:
            result += str(r) + "\n"

        return result
