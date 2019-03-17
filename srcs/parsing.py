from Character import Character
from Room import Room
from partyInformations import PartyInformations
import re
from random import randrange
from time import sleep

class Parser:
	def __init__(self, partyInfos):
		self.linesRead = 0
		self.number = partyInfos.number
		self.lines = []
		self.rooms = []
		self.questionType = "None"
		self.moveQuestion = "move"
		self.tileQuestion = "tile"
		self.powerQuestion = "power"
		self.colorChangeQuestion = "colorChange"
		self.roomLightQuestion = "roomLight"
		self.roomToBlockQuestion = "roomToBlock"
		self.withWhichRoomQuestion = "withWhichRoom"
		self.partyInfos = partyInfos

	def tryRead(self):
		ok = False
		try:
			f = open('./' + str(self.number) + '/questions.txt', 'r')
			f.close()
			ok = True
		except IOError:
			ok = False
		return ok
	def updateInfos(self):
		info_file = open('./' + str(self.number) + '/infos.txt', 'r')
		self.lines = info_file.readlines()
		info_file.close()

	def getGhost(self):
		if len(self.lines) != 0:
			line = self.lines[0]
			self.partyInfos.fantome = line.split()[-1]

	def parseTourInfos(self):
		i = len(self.lines) - 1
		if i == -1:
			return
		while i >= 0:
			if "**************************" in (self.lines)[i]:
				i += 1
				tourInfos = self.lines[i].split(',')
				numberTour = int(tourInfos[0][-1])
				carlota = int(tourInfos[1].split(':')[1].split('/')[0])
				maxCarlota = int(tourInfos[1].split(':')[1].split('/')[1])
				salleOmbre = int(tourInfos[2][-1])
				room1Bloque = int(tourInfos[3][-1])
				room2Bloque = int(tourInfos[4][1])
				self.partyInfos.update(numberTour, carlota, maxCarlota, salleOmbre, room1Bloque, room2Bloque)
				i += 1
				charactersInfos = self.lines[i].split()
				for characterInfos in charactersInfos:
					cinfos = characterInfos.split('-')
					color = cinfos[0]
					room = int(cinfos[1])
					suspect = cinfos[2]
					self.partyInfos.updateCharacter(color, room, True if suspect == "suspect" else False)
				break
			i -= 1
		i += 1
		while i < len(self.lines):
			line = (self.lines)[i]
			if "NOUVEAU PLACEMENT" in line:
				move = line.split()[3]
				color = move.split('-')[0]	
				roomNumber = int(move.split('-')[1])
				suspect = move.split('-')[2]
				self.partyInfos.updateCharacter(color, roomNumber, True if suspect == "suspect" else False)
			elif "a été tiré" in line:
				if "fantome" in line:
					self.partyInfos.carlota += -1 if self.partyInfos.number == 0 else 1
				else:
					move = line.split()[0]
					color = move.split('-')[0]
					roomNumber = int(move.split('-')[1])
					suspect = move.split('-')[2]
					self.partyInfos.updateCharacter(color, roomNumber, True if suspect == "suspect" else False)
			elif "Quelle salle obscurcir ? (0-9)" in line:
				i += 2
				if len(self.lines) <= i:
					return
				line = (self.lines)[i]
				room = int(line.split()[3])
				self.partyInfos.obscurcirRoom(room)
			elif "Quelle salle bloquer ? (0-9)" in line:
				i += 4
				if len(self.lines) <= i:
					return
				line = (self.lines)[i]
				passage = line.split()[3]
				room1 = int(line.split()[3][1])
				room2 = int(line.split()[4][0])
				self.partyInfos.bloquePassage(room1, room2)
			elif "Score final" in line:
				score = int(line.split()[3])
				if self.partyInfos.number == 0:
					if score > 0:
						print("Orewa Meitante Conan !!!")
					else:
						print("Orewa Meitante Anthony !!!")
				else:
					if score > 0:
						print("J'ai perdu, c'est Conan en face!")
					else:
						print("J'ai gagné, c'est Anthony en face!")
				print(line)
				exit()

			i += 1

	def readInfos(self):
		info_file = open('./' + self.number + '/infos.txt', 'r')
		self.lines = info_file.readlines()
		returnLine = ""
		if (len(self.lines) > self.linesRead):
			returnLine = self.lines[self.linesRead]
			self.linesRead += 1
		info_file.close()
		return returnLine

	def readQuestion(self):
		questionFile = open('./' + str(self.number) + '/questions.txt', 'r')
		line = questionFile.read()
		if "Tuiles disponibles" in line:
			print("\n\n********New turn********")
		if len(line) > 0:
			print(("Inspecteur" if self.number == 0 else "Fantome") + " : Question :" + line + ":")
		if "Tuiles disponibles" in line:
			self.questionType = self.tileQuestion
			m = re.search('\[(.+?)\]', line).group(1)
			characters = m.split(',')
			self.partyInfos.taro = []
			for character in characters:
				character = character.replace(' ', '')
				color = character.split('-')[0]
				for c in self.partyInfos.characters:
					if color == c.color:
						self.partyInfos.taro.append(c)
						break
			# print ("Taro read:", self.partyInfos.taro)
		elif "Quelle salle obscurcir" in line:
			self.questionType = self.roomLightQuestion
		elif "Voulez-vous activer le pouvoir" in line:
			self.questionType = self.powerQuestion
		elif "positions disponibles : " in line:
			m = re.search('\{(.+?)\}', line).group(1)
			rooms = m.split(',')
			self.finalRooms = []
			for room in rooms:
				room = room.replace(' ','')
				self.finalRooms.append(int(room))
			self.questionType = self.moveQuestion
		elif "Avec quelle couleur échanger (pas violet!) ?" in line:
			self.questionType = self.colorChangeQuestion
		elif "Quelle salle bloquer ? (0-9)" in line:
			self.questionType = self.roomToBlockQuestion
		elif "Quelle sortie ? Chosir parmi" in line:
			self.questionType = self.withWhichRoomQuestion
		else:
			self.questionType = "None"
			questionFile.close()
			return False
		questionFile.close()
		questionFile = open('./' + str(self.number) + '/questions.txt', 'w')
		questionFile.write("")
		questionFile.close()
		return True

	def sendResponse(self):
		rf = open('./' + str(self.number) + '/reponses.txt','w')
		result = ""
		if self.questionType == "None":
			rf.close()
			return
		elif self.questionType == self.tileQuestion:
			print("IA RESULT :")
			print(self.partyInfos.result)
			result = str(self.partyInfos.result["tile"])
		elif self.questionType == self.moveQuestion:
			result = str(self.partyInfos.result["move"])
			# for index, room in enumerate(self.finalRooms):
			# 	if room == self.partyInfos.result["move"]:
			# 		result = str(index)
			# 		break
		elif self.questionType == self.powerQuestion:
	        	result = str(self.partyInfos.result["power"])
		elif self.questionType == self.roomToBlockQuestion:
	        	result = str(self.partyInfos.result["power_effect"][0])
		elif self.questionType == self.withWhichRoomQuestion:
	        	result = str(self.partyInfos.result["power_effect"][1])
		elif self.questionType == self.colorChangeQuestion:
	        	result = str(self.partyInfos.result["power_effect"])
		elif self.questionType == self.roomLightQuestion:
	        	result = str(self.partyInfos.result["power_effect"])
		print("Response : " + result)
		rf.write(result)
		rf.close()
