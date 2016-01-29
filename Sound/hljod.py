import pygame

import time

class Sound:
	def __init__(self):
		pygame.init()
	def intro(self):
		pygame.mixer.music.load("introGameOfThrones.wav")
		pygame.mixer.music.play(1)
		time.sleep(27)
	def drawCard(self):
		pygame.mixer.music.load("cardSlide.wav")
		pygame.mixer.music.play(1)
		time.sleep(0.5)
	def select(self):
		pygame.mixer.music.load("select1.wav")
		pygame.mixer.music.play(1)
		time.sleep(0.5)
	def placeCard(self):
		pygame.mixer.music.load("cardPlace.wav")
		pygame.mixer.music.play(1)
		time.sleep(0.5)
	def shuffling(self):
		pygame.mixer.music.load("cardShuffle2.wav")
		pygame.mixer.music.play(1)
		time.sleep(3)
	def gameOver(self):
		pygame.mixer.music.load("gameOver1.wav")
		pygame.mixer.music.play(1)
		time.sleep(4)
	def wrongPlayed(self):
		pygame.mixer.music.load("wrongPlayed.wav")
		pygame.mixer.music.play(1)
		time.sleep(0.5)
	def bonus(self):
		pygame.mixer.music.load("bonus.wav")
		pygame.mixer.music.play(1)
		time.sleep(0.8)
	def winning(self):
		pygame.mixer.music.load("winningFireworks.wav")
		pygame.mixer.music.play(1)
		time.sleep(10)
	def pause(self):
		pygame.mixer.music.load("pause.wav")
		pygame.mixer.music.play(1)
		time.sleep(2)
def main():
	play = Sound()
	play.intro()
	time.sleep(2)
	play.pause()
	time.sleep(2)
	play.bonus()
	time.sleep(2)
	play.select()
	time.sleep(2)
	play.drawCard()
	time.sleep(2)
	play.placeCard()
	time.sleep(2)
	play.wrongPlayed()
	time.sleep(2)
	play.gameOver()
	time.sleep(2)
	play.shuffling()
	time.sleep(2)
	play.winning()
	
main()



#while pygame.mixer.music.get_busy:
		#	continue