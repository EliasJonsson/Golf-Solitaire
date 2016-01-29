 #encoding: utf-8
from __future__ import division
class Score(object):

    def __init__(self):
        
        self.score = 0
        self.comboScore = 0
        self.normalScore = 0
        self.timeScore = 0
        self.sumScore = 0
        self.finishScore = 300
        self.secInMin = 60
        self.bonusLimitCombo = [3, 5, 10, 20]
        self.bonusLimitTime = 5

    def getSumScore(self,finish):
        """
        Get the totalscore for the player

        Put the totalTime of the round and total ComboScore
        To get the total score
        """
        #comment
        if finish:
            self.sumScore = self.comboScore + self.timeScore + self.normalScore  + self.finishScore
            self.comboScore =+ self.finishScore
            return int(self.sumScore)
        else:
            self.sumScore = self.comboScore + self.timeScore + self.normalScore
            return int(self.sumScore)

    def getTimeScore(self,getTime,finish):
        """
        Get the time, and if the player finished the game or not

        And updates the timescore and returns it
        """

        if getTime/self.secInMin < self.bonusLimitTime and finish:
            scoreFromTime = 10000/(getTime*getTime)
            self.timeScore = scoreFromTime * 1000
        else:
            self.timeScore = 0

        return int(self.timeScore)

    def getComboScore(self,combo):
        """
        Call this after evry succisfull move from the player
        with the combo value (how many times in a row the player)
        has made a succesfull move.

        you put in the original comboscore, and it is updated
        """
        if combo == self.bonusLimitCombo[3]:
            self.comboScore += 400
            self.score += 400
        elif combo == self.bonusLimitCombo[2]:
            self.comboScore += 100
            self.score += 100
        elif combo == self.bonusLimitCombo[1]:
            self.comboScore += 30
            self.score += 30
        elif combo == self.bonusLimitCombo[0]:
            self.comboScore += 10
            self.score += 10
        

    def normalMove(self):
        """
        Update the normalscore if the player does a succesfull move
        """

        self.normalScore += 1
        self.score += 1

    def returnNormalScore(self):
        """
        Return the normalScore
        """

        return self.normalScore

    def returnScore(self):
        """
        Return the score
        """

        return self.score

    def returnCombo(self):
        """
        Return the comboScore
        """

        return self.comboScore
       








