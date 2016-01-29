'''
  Pile holds cards that have been used already,
  you should never have to take a card from pile
  only read the cards from there.
'''


class Pile(object):


  def __init__(self):
    '''
      Initialize a new pile
    '''
    self._cards = []

  def topCard(self):
    '''
      returns the card at the top of the pile
    '''
    return self._cards[-1]

  def put(self,card):
    '''
      Puts card at the top of the pile
    '''
    self._cards.append(card)

  def takeLastCard(self):
    ''' 
      Take last card from pile
    '''
    return self._cards.pop()

  def isEmpty(self):
    '''
      Is pile empty?
    '''
    return bool(self._cards)

  def __iter__(self):
    '''
      returns a iterator of a copy of the pile
    '''
    return iter(copy(self._cards))
