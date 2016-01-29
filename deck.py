#encoding: utf-8
from random import shuffle

class Deck(object):
    '''
        Holds a deck of cards
    '''


    _suits = 'hsdc' #Hjarta, spaði, tígull, lauf
    _ranks = '23456789TJQKA'

    def __init__(self):
        '''
            Initialize a standard shuffled 52 card deck.
            The last card in self._card is at the top of the deck.
        '''

        self._deck = [rank + suit for rank in Deck._ranks for suit in Deck._suits]
        self._shuffle()

    def draw_card(self):
        '''
            Returns the card from the top (end of list) of the deck and removes it. Assumes deck is not empty!!
        '''

        return self._deck.pop()


    def draw_cards(self, len):
        '''
            Draws len cards.
        '''

        return [self.draw_card() for _ in range(len)]

    def _shuffle(self):
        '''
            Permutes the ordering of the cards in the deck.
        '''
        shuffle(self._deck)


    def isEmpty(self):
        '''
            Checks if the deck is empty
        '''

        return self._deck == []

    def card_count(self):
        '''
            Returns the cards left
        '''
        
        return len(self._deck)

    @staticmethod
    def isMatch(deckCard, pileCard):
        '''
            Returns true if the cards match according to the golf solitaire
        '''
        rankcard = int(Deck._ranks.index(deckCard[0]))
        rankpile = int(Deck._ranks.index(pileCard[0]))

        #Found a  match between card from minideck and pile
        if abs((rankcard-rankpile)) == 1 or abs((rankcard-rankpile)) == 12:
            return True

        return False

    def __iter__(self):
        return iter(self._deck)
