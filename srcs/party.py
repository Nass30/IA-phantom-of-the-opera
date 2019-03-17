#!/usr/bin/env python
from Character import Character
from Room import Room
from parsing import Parser
import IA
from partyInformations import PartyInformations
from timeit import default_timer as timer

class Party:
	def __init__(self, number):
		self.partyInfos = PartyInformations(number)
		self.parser = Parser(self.partyInfos)
		while self.parser.tryRead() == False:
			continue
		while True:
			start = timer()
			self.parser.updateInfos()
			if number == 1:
				self.parser.getGhost()
			self.parser.parseTourInfos()
			if self.parser.readQuestion() == False:
				continue
			if self.parser.questionType == self.parser.tileQuestion:
				IA.compute(self.partyInfos)
				end = timer()
				print("time elapsed = " + str(end - start))
			self.parser.sendResponse()
