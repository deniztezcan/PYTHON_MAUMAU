'''
 PYTHON_MAUMAU - A non-interactive PYTHON version of the game mau mau (pesten)

 @package 	PYTHON_MAUMAU
 @author    Deniz Tezcan <howdy@deniztezcan.me>
 @link      https://github.com/deniztezcan/PYTHON_MAUMAU
'''

class Application:

	deck 			= []
	players 		= []
	stack 			= []
	losers 			= []
	gameFinished 	= None

	def __init__(self):
		self.initializeDeck()
		self.initializePlayers()a
		self.initializeStack()
		self.initializeLosers()
		self.initializeStatus()


	def startGame(self):
		print('Hello world')