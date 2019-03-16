#!/usr/bin/env python
from Character import Character
from Room import Room
from parsing import Parser
from partyInformations import PartyInformations

import time

class Party:
	def __init__(self, number):
		self.partyInfos = PartyInformations(number)
		self.parser = Parser(self.partyInfos)
		while self.parser.tryRead() == False:
			continue
		while True:
			self.parser.updateInfos()
			if number == 1:
				self.parser.getGhost()
			self.parser.parseTourInfos()
			if self.parser.readQuestion() == False:
				continue
			# IA HERE
			self.parser.sendResponse()
