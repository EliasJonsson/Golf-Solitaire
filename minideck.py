from random import shuffle
from deck import Deck


class Minideck(object):
	'''
		Minideck holds 5 diffrent cards from a Deck
	'''

	def __init__(self,five_cards):

		self._minideck = five_cards			#Create a empty minideck

	def get(self):
		'''
			Returns the minideck
		'''

		return self._minideck

	def peek(self):
		'''
			Checks the value of the card on the top of the minideck
		'''

		return self._minideck[-1]

	def pop(self):
		'''
			Pops the value of the card witch is on the top of the minideck
		'''

		return self._minideck.pop()

	def isEmpty(self):
		'''
			Checks if the minideck is empty
		'''
		return self._minideck == []

	def __iter__(self):
		''' 
			Returns an iterator over te cards in the minideck
		'''
		
		return iter(self._minideck)




