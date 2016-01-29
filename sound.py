#encoding: utf-8
import pygame
import time
import os

class Sound:
	def __init__(self):
		pygame.init()
		pygame.mixer.set_num_channels(30)
		self.soundlist = []
		self.playlist =["Sound/Lagalisti/Allofme.wav","Sound/Lagalisti/AloeBlacc-TheMan.wav","Sound/Lagalisti/DJMuscleBoy-LOUDERftStopWaitGo.wav","Sound/Lagalisti/KatyPerry-IKissedAGirl.wav","Sound/Lagalisti/Letitgo-frozen.wav","Sound/Lagalisti/PokemonFirstThemeSong.wav","Sound/Lagalisti/SebastienTellier-Divine.wav","Sound/Lagalisti/ShakiraCantRemembertoForgetYouftRihanna.wav","Sound/Lagalisti/StandOut-AGoofyMovieLyrics.wav","Sound/Lagalisti/TheLionKing-CircleOfLife.wav","Sound/Lagalisti/Vestfjardaodur.wav"]	
		self.playlist2 = []
		self.currentsong = None
		self.playlistname = ["John Legend - All of me","Aloe Blacc - The Man","DJ MuscleBoy - LOUDER","Katy Perry - I Kissed A Girl","Let it go - Frozen","First Theme Song - Pokemon","Sebastien Tellier - Divine","Shakira - Cant Remember to Forget You ft Rihanna","Stand Out - A Goofy Movie","The Lion King - Circle Of Life","Herbertson - Vestfjardaodur"]
		self.neverPlayed = False
	def stop(self):
		"""
		Stop the all the songs that are playing
		"""
		
		for sound in self.soundlist:
			pygame.mixer.Sound.stop(sound)

	def intro(self):
		"""
		Play the mario intro song
		"""

		s = pygame.mixer.Sound("Sound/introSuperMario.wav")
		s.play(100)
		self.soundlist.append(s)
		
	def drawCard(self):
		"""
		Play the drawcard sound
		"""

		s = pygame.mixer.Sound("Sound/cardSlide.wav")
		s.play()

	def select(self):
		"""
		Play the select sound
		"""

		s = pygame.mixer.Sound("Sound/select1.wav")
		s.play()

	def placeCard(self):
		"""
		Play the placecard sound
		"""

		s = pygame.mixer.Sound("Sound/cardPlace.wav")
		s.play()
		
	def shuffling(self):
		"""
		Play the shuffling sound
		"""

		s = pygame.mixer.Sound("Sound/cardShuffle2.wav")
		s.play()

	def gameOver(self):
		"""
		Play the gameover sound
		"""
		pygame.mixer.music.load("Sound/gameOver1.wav")
		pygame.mixer.music.play(1)
		
	
	def wrongPlayed(self):
		"""
		Play the wrongmove sound
		"""

		pygame.mixer.music.load("Sound/wrongMove.wav")
		pygame.mixer.music.play(1)
		
	def combo(self, number):
		"""
		Play the combo sound
		"""
		s = pygame.mixer.Sound("Sound/combo" + str(number)+ ".wav")
		s.play()
	
	
	def winning(self):
		"""
		Play the wingame sound
		"""

		pygame.mixer.music.load("Sound/winningFireworks.wav")
		pygame.mixer.music.play(1)
		

	def pause(self):
		"""
		Play the pause sound
		"""

		pygame.mixer.music.load("Sound/pause.wav")
		pygame.mixer.music.play(1)
		
	def comboBreaker(self):
		"""
		Play the combobreaker sound
		"""

		s = pygame.mixer.Sound("Sound/comboBreaker.wav")
		s.play()


	#musicplayer

	def playSong(self,song):
		"""
		Play the song that the 'song' refers to
		"""

		s = pygame.mixer.Sound(self.playlist[song])
		c = pygame.mixer.Channel(1)
		c.play(s)

	def getLenPlaylist(self):
		"""
		Return the length of the current playlist running
		"""

		return len(self.playlist)

	def pauseSong(self):
		"""
		Pause the current song that is running on channel 1
		"""

		s = pygame.mixer.Channel(1)
		s.pause()

	def resumeSong(self):
		"""
		Resume the song that is running on channel 1
		"""

		s = pygame.mixer.Channel(1)
		s.unpause()

	def getSongName(self,song):
		"""
		Return the song name of the song that is currently running
		"""

		return self.playlistname[song]
