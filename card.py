'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

class Card:

	suit 	= ""
	value 	= ""

	def __init__(self, suit, value):
		self.setSuit(suit)
		self.setValue(value)

	def setSuit(self, suit):
		self.suit = suit

	def getSuit(self):
		return self.suit

	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value

	def getCard(self):
		return self.suit+self.value	