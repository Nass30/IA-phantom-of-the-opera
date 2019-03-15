from Character import Character
from Room import Room
from partyInformations import PartyInformations

class Parser:
	def __init__(self, partyInfos):
		self.linesRead = 0
		self.number = partyInfos.number
		self.lines = []
		self.partyInfos = partyInfos

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
		while i > 0:
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
				return
			i -= 1
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
		questionLine = questionFile.read()
		questionFile.close()
		return questionLine

	def sendResponse(self, str):
		rf = open('./' + str(self.number) + '/reponses.txt','w')
		rf.write(str)
		rf.close()
		
