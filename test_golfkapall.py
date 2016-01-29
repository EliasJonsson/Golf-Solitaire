#encoding: utf-8
import unittest
from deck import Deck
from minideck import Minideck
from pile import Pile
from score import Score




class GolfKapallTests(unittest.TestCase):


  def testDeckinit(self):
     '''
         Tests if the deck initializes correctly

     '''

     deck1 = Deck()
     deck2 = ['7c', '2s', '6d', 'Tc', '2d', 'Qs', '5c', 'Kc', 'Kd', 'Ad', '2c', 'Qh', 'Jd', '7d', 'Ah', '8s', '6s', '4d', 'Ts', '3s', '6c', '7h', '4h', 'Jh', '7s', '3h', '8c', 'Td', 'Ac', '9d', 'Ks', 'As', '9h', '4c', '5d', 'Th', '6h', '2h', 'Js', '3d', 'Kh', '8h', 'Qd', '5h', '9c', '9s', '8d', '4s', 'Qc', '5s', 'Jc', '3c']

     self.assertEqual(set(deck1), set(deck2))


  def testDrawCard(self):
     '''
         Does draw_card instance method work correctly, that is have the appropriate side effects on the state of the Deck instance.
     '''

     deck = Deck()

     lastcard = deck._deck[-1]
     previouslength = len(deck._deck)

     self.assertEqual(deck.draw_card(), lastcard)
     self.assertEqual(len(deck._deck), previouslength-1)
     self.assertTrue(lastcard not in deck)
  def testDrawCards(self):
     '''
       Tests drawing multiple cards
     '''

     deck = Deck()
     self.assertEqual(len(deck.draw_cards(5)), 5)
     self.assertEqual(len(deck._deck), 52-5)

  def testPile(self):
     '''
       Tests the pile class
     '''
     pile = Pile()

     pile.put('H5')
     pile.put('H6')

     self.assertEqual(pile.topCard(), 'H6')

  def testpop(self):
      '''
         Check if the minideck pops a card from it and also check if the poped card is the same from 2 minidecks
      '''

      deck = Deck()

      _minideck1 = Minideck(deck.draw_cards(5))
      _minideck2 = Minideck(deck.draw_cards(5))



      self.assertFalse(_minideck1.pop() == _minideck2.pop())
      self.assertEqual(4,len(_minideck1.get()))
      self.assertEqual(4,len(_minideck1.get()))

  def testpeek(self):
      '''
         Check if the minideck peeks on a card and doesnt pop it.
      '''

      deck = Deck()

      _minideck1 = Minideck(deck.draw_cards(5))
      _minideck2 = _minideck1

      self.assertTrue(_minideck1.peek() == _minideck2.peek())
      self.assertEqual(5,len(_minideck1.get()))

  def testisMatch(self):
    '''
      Check if the current card on the pile and the card on the deck are the same
    '''

    deck = Deck()
    #This should be false
    test1 = deck.isMatch("2h","2h")
    #This should be true
    test2 = deck.isMatch("2h","Ac")
    #This should be true
    test3 = deck.isMatch("2h","3h")
    #This should be false
    test4 = deck.isMatch("2h","8s")

    self.assertTrue(test1 == False)
    self.assertTrue(test2 == True)
    self.assertTrue(test3 == True)
    self.assertTrue(test4 == False)

  def testgetSumScore(self):
    'Test if the getSumScore function is correct'
    get1 = Score()
    get2 = Score()
    get1.normalScore = 300
    get1.finishScore = 200
    get1.comboScore = 100
    get1.timeScore = 0
    normalScore = 400
    finishScore = 300
    comboScore = 100
    timeScore = 1000
    get2.normalScore = normalScore
    get2.finishScore = finishScore
    get2.comboScore = comboScore
    get2.timeScore = timeScore
    finish1 = 1
    finish2 = 0
    self.assertEqual(get1.getSumScore(finish2),(get1.normalScore+get1.comboScore))
    self.assertEqual(get2.getSumScore(finish1),(timeScore+normalScore+finishScore+comboScore))
  def testgetComboScore(self): 
    'Test if the getComboScore is correct for five instances'
    get1 = Score()
    combo = 20
    get1.getComboScore(combo)
    comboScore1 = 400
    self.assertEqual(get1.returnCombo(),comboScore1)
    get2 = Score()
    combo = 10
    get2.getComboScore(combo)
    comboScore2 = 100
    self.assertEqual(get2.returnCombo(),comboScore2)
    get3 = Score()
    combo = 5
    get3.getComboScore(combo)
    comboScore3 = 30
    self.assertEqual(get3.returnCombo(),comboScore3)
    get4 = Score()
    combo = 3
    get4.getComboScore(combo)
    comboScore4 = 10
    self.assertEqual(get4.returnCombo(),comboScore4)
    get5 = Score()
    combo = 7
    get5.getComboScore(combo)
    comboScore5 = 0
    self.assertEqual(get5.returnCombo(),comboScore5)
  def testgetTimeScore(self):
    'Test if getTimeScore will return the correct time score for 3 instances'
    get1 = Score()
    finish1 = True
    time1 = 1000
    self.assertEqual(get1.getTimeScore(time1,finish1),0)
    get2 = Score()
    time2 = 290
    self.failIf(get2.getTimeScore(time2,finish1) == 0)
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
