'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

import sys
from deck import Deck
from player import Player
from stack import Stack

class Application:

	deck 			= []
	players 		= []
	stack 			= []
	losers 			= []
	gameFinished 	= None

	def __init__(self):
		self.initializeDeck()
		self.initializePlayers()
		self.initializeStack()
		self.initializeLosers()
		self.initializeStatus()

	def initializeDeck(self):
		self.deck = Deck()
		self.deck.shuffle()

	def initializePlayers(self):
		self.players = []
		self.players.append(Player('Churchill'))
		self.players.append(Player('Stalin'))
		self.players.append(Player('Roosevelt'))
		self.players.append(Player('de Gaulle'))

	def initializeStack(self):
		self.stack = Stack()

	def initializeLosers(self):
		self.losers = []

	def initializeStatus(self):
		self.gameFinished = False


	def listPlayers(self):
		returnString = "Starting game with"

		for player in self.players:
			returnString += " " + player.getName() + ","

		returnString = returnString.rstrip(",")
		return returnString

	def initialDealing(self):
		for player in self.players:
			for cardIndex in range(0, 7):
				player.addToHand(self.deck.dealCard())

	def listInitialDealings(self):
		returnString = ""

		for player in self.players:
			returnString += player.getName() + " has been dealt:"
			for card in player.getHand():
				returnString += " " + card.getCard() + ","
			returnString = returnString.rstrip(",") + "\n"

		returnString = returnString.rstrip("\n")
		return returnString

	def listWinner(self, name):
		print( name + " has won." )
 
	def setGameFinished(self, status):
		self.gameFinished = status

	def setLoser(self, player):
		if self.countLosers() == 0:
			self.losers.append(player)
		else:
			foundPlayer = False
			for losingPlayer in self.losers:
				if losingPlayer == player:
					foundPlayer = True
			
			if foundPlayer == True:
				return
			else:
				self.losers.append(player)
				return

	def removeLosers(self):
		self.initializeLosers()

	def countLosers(self):
		return len(self.losers)

	def countPlayers(self):
		return len(self.players)

	def canPlay(self, card, hand, player):
		for idx, handCard in enumerate(hand):
			if handCard.getSuit() == card.getSuit():
				return [idx, handCard]
			elif handCard.getValue() == card.getValue():
				return [idx, handCard]
		return False

	def play(self, player):
		stackCard 	= self.stack.getTopStackCard()
		canPlay 	= self.canPlay(stackCard, player.getHand(), player)

		if canPlay == False:
			if self.deck.isEmpty == False:
				newCard = self.deck.dealCard()
				player.addToHand(newCard)
				print(player.getName() + " does not have a suitable card. taking from deck " + newCard.getCard())
			else:
				if self.countLosers() == self.countPlayers():
					print("No cards left in deck. There is no winner :(")
					self.setGameFinished(True)
					sys.exit()

				else:
					print(player.getName() + " does not have a suitable card. Deck is empty - skipping turn")
					self.setLoser(player)
		else:
			print(player.getName() + " plays " + canPlay[1].getCard())
			self.stack.addToStack(canPlay[1])
			player.removeFromHand(canPlay[0])
			self.removeLosers()

	def restOfGame(self):
		while self.gameFinished == False:
			for player in self.players:
				if player.countHand() > 0:
					self.play(player)
					if player.countHand() == 0:
						self.listWinner(player.getName())
						self.setGameFinished(True)
						sys.exit()

	def startGame(self):
		print(self.listPlayers())
		self.initialDealing()
		print(self.listInitialDealings())
		self.stack.addToStack(self.deck.dealCard())
		print(self.stack.listTopStackCard())
		self.restOfGame()