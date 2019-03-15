from characters import Character
from rooms import Room

class Parser:
	def __init__(self):
		self.linesRead = 0
		self.number = 0
		self.lines = []

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
		questionFile = open('./' + self.number + '/questions.txt', 'r')
		questionLine = questionFile.read()
		questionFile.close()
		return questionLine

	def sendResponse(self, str):
            rf = open('./' + self.number + '/reponses.txt','w')
	    rf.write(str)
            rf.close()