'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

class Stack:

	stack = []

	def __init__(self):
		self.initializeStack()

	def initializeStack(self):
		self.stack = []

	def addToStack(self, card):
		self.stack.append(card)

	def getTopStackCard(self):
		count = len(self.stack)
		return self.stack[count-1]

	def listTopStackCard(self):
		card = self.getTopStackCard()
		return "Top card is: " + card.getCard();
