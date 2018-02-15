'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

class Player:

	name = ""
	hand = []

	def __init__(self, name):
		self.setName(name)
		self.initializeHand()

	def initializeHand(self):
		self.hand = []

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def addToHand(self, card):
		self.hand.append(card)

	def removeFromHand(self, index):
		self.hand.pop(index)

	def countHand(self):
		return len(self.hand)

	def getHand(self):
		return self.hand