'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

import random
from card import Card

class Deck:

	suits 	= []
	values 	= []
	cards 	= []

	def __init__(self):
		self.initializeSuits()
		self.initializeValues()
		self.initializeCards()
		self.initializeDeck()

	def setCard(self, suit, value):
		self.cards.append(Card(suit, value))

	def initializeSuits(self):
		self.suits.append("♥")
		self.suits.append("♠")
		self.suits.append("♦")
		self.suits.append("♣")

	def initializeValues(self):
		self.values.append("A")
		self.values.append("K")
		self.values.append("Q")
		self.values.append("J")
		self.values.append("10")
		self.values.append("9")
		self.values.append("8")
		self.values.append("7")
		self.values.append("6")
		self.values.append("5")
		self.values.append("4")
		self.values.append("3")
		self.values.append("2")	

	def initializeCards(self):
		self.cards = []

	def initializeDeck(self):
		for suit in self.suits:
			for value in self.values:
				self.setCard(suit, value)	

	def shuffle(self):
		random.shuffle(self.cards)

	def count(self):
		return len(self.cards)

	def addToDeck(self, card):
		self.cards.append(card)

	def removeFromDeck(self, index):
		self.cards.pop(index)

	def dealCard(self):
		cardInHand = self.cards[0]
		self.removeFromDeck(0)
		return cardInHand

	def isEmpty(self):
		if self.count() == 0:
			return True
		else:
			return False
