#encoding: utf-8
import os
class Highscore(object):
	def __init__(self):
		self.CurrentHighscorelist = []

	"""
	How to use:

	Call parseHighscores(newscore),

	it will check if the the newscore is in the current highscore list
	after either puting it in the highscore or not it will

	from number 1 score to number 10

	"""

	def handleHighScores(self,currentscore):
		"""
		Call this when a player has finished his game returns
		if he is on the highscore list or not
		"""

		#Check if the current highscore is larger than the least highscore
		if int(currentscore) > int(self.CurrentHighscorelist[-1][1]):
			return True

		#If not do nothing
		else:
			return False


	def addHighscore(self,currentscore,username):
		"""
		Called when a highscore is in the highscore list,
		and puts the current score and username
		onto the highscore list
		"""

		newhighscores = []

		#Put the current score into the highscore list
		for name,score in self.CurrentHighscorelist:
			if currentscore > int(score):
				newhighscores.append((username,str(currentscore)))
				currentscore = 0
				newhighscores.append((name,score))
			else:
				newhighscores.append((name,score))

		newscores = newhighscores [0:10]
		
		self.CurrentHighscorelist = newscores

		#Now write it to the .txt file

		highscorefile = 'highscores.txt'
		f = open(highscorefile, 'w')

		for name,score in self.CurrentHighscorelist:
			f.write("%s:%s\n" % (name, score))
		f.close()


	def parseHighscores(self,currentscore):
		"""
		Check if we have created a highscore file
		If not create one with random value
		"""
		highscorefile ="highscores.txt"
		path = os.path.abspath("highscores.txt")
		if os.path.isfile(highscorefile):
			#read the file
			f = open(highscorefile,'r')
			lines = f.readlines()
			#put it into 2 lists

			scores = []
			for line in lines:
				scores.append(line.strip().split(':'))

			self.CurrentHighscorelist = scores
			f.close()
			
			return self.handleHighScores(currentscore)
		else:
			#create a new table of random scores
			f = open(highscorefile, 'w')
			f.write("""kalli:10
						palli:9
						sölvi:8
						helga:7
						gummi:6
						dori:5
						elli:4
						halli:3
						oli:2
						bjarki:1""")
			f.close()

			#call the method again to load the scores
			return self.parseHighscores(currentscore)

	def showHighscores(self):
		"""
		Takes in a highscore list with two lists
		returns a tuple with name and score
		"""

		for i in range(len(self.CurrentHighscorelist)):
			name,score = self.CurrentHighscorelist[i]

		return name,score

