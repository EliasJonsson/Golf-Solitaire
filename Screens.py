
#encoding: utf-8
import sys, pygame
from score import Score
from deck import Deck
from highscore import Highscore
from sound import Sound
from random import randint
import time
import eztext


IMG = 0     # Img position in createGraphics object
RECT = 1    # Rect position in createGraphics object

# Screens 
STARTSCREEN = 0
TOPSCREEN = 1
PLAYSCREEN = 2
RULESSCREEN = 3
ABOUTSCREEN = 4
INTROSCREEN = 5

NUMBEROFMINID = 7
CARDSINMINIDECK = 5

def createGraphics(url, left, top):
    '''
        Loads graphic from file and positions it on screen
    '''
    img = pygame.image.load(url)
    rect = img.get_rect()
    rect = rect.move(left,top)
    return [img,rect]

def collides(rect):
    '''
        Checks if mouse pointer is inside rect
    '''
    return rect.collidepoint(pygame.mouse.get_pos())

class IntroScreen(object):
    def __init__(self):
        '''
        START SCREEN INIT
        '''
        # Load all graphics for this screen
        self.bg = createGraphics("img/intro1.png", 0, 0)    # Load the background

    def display(self, screen, currentScreenIndex): 
        # if more than 4 seconds since start
        if pygame.time.get_ticks() > 4000 and pygame.time.get_ticks() < 8000:
            # display second intro screen
            self.bg[IMG] = pygame.image.load("img/intro2.png")

        # if more than 8 seconds since start
        elif pygame.time.get_ticks() > 4000 and pygame.time.get_ticks() < 14000:
            # display third intro screen
            self.bg[IMG] = pygame.image.load("img/intro3.png")

        # if more than 14 seconds since start
        elif pygame.time.get_ticks() > 4000 and pygame.time.get_ticks() > 14000:
            # display startscreen
            return STARTSCREEN

        # draw screen
        screen.blit(self.bg[IMG], self.bg[RECT])
        return INTROSCREEN

class StartScreen(object):
    def __init__(self):
        '''
        START SCREEN INIT
        '''
        # Load all graphics for this screen
        self.bg = createGraphics("img/start_bg.png", 0, 0)    # Load the background
        self.logo = createGraphics("img/logo.png", 349,68)    # Load the logo
        self.play = createGraphics("img/play.png", 262,301)   # Load the play button
        self.rules = createGraphics("img/rules.png", 159,533) # Load the rules button
        self.top = createGraphics("img/top10.png", 331,533)   # Load the top button
        self.about = createGraphics("img/about.png", 503,533) # Load the about button

    def display(self, screen, currentScreenIndex):
        play = Sound() 
        # Check if left mouse button is pressed
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))

        # is mouse pointer over the play button
        if collides(self.play[RECT]):
            self.play[IMG] = pygame.image.load("img/play_hover.png")
            if isPressed:
                play.select() 
                currentScreenIndex = PLAYSCREEN
                
        # is mouse pointer over the rules button
        elif collides(self.rules[RECT]):
            self.rules[IMG] = pygame.image.load("img/rules_hover.png")
            if isPressed:
                play.select() 
                currentScreenIndex = RULESSCREEN
                
        # is mouse pointer over the top 10 button
        elif collides(self.top[RECT]):
            self.top[IMG] = pygame.image.load("img/top10_hover.png")
            if isPressed:
                play.select() 
                currentScreenIndex = TOPSCREEN         

        # is mouse pointer over the about button
        elif collides(self.about[RECT]):
            self.about[IMG] = pygame.image.load("img/about_hover.png")
            if isPressed:
                play.select() 
                currentScreenIndex = ABOUTSCREEN
                
        # nothing of above, set all buttons to start position
        else:
            self.play[IMG] = pygame.image.load("img/play.png")
            self.rules[IMG] = pygame.image.load("img/rules.png")
            self.top[IMG] = pygame.image.load("img/top10.png")
            self.about[IMG] = pygame.image.load("img/about.png")

        # Draw all screen elements
        screen.blit(self.bg[IMG], self.bg[RECT])
        screen.blit(self.logo[IMG], self.logo[RECT])
        screen.blit(self.play[IMG], self.play[RECT])
        screen.blit(self.rules[IMG], self.rules[RECT])
        screen.blit(self.top[IMG], self.top[RECT])
        screen.blit(self.about[IMG], self.about[RECT])
        
        # Send report to controller about current position
        return currentScreenIndex

class RulesScreen(object):
    def __init__(self):
        '''
        START RULES INIT
        '''
        # Load all graphics for this screen
        self.bg = createGraphics("img/rules_bg.png", 0, 0)    # Load the background
        self.back = createGraphics("img/back.png",20,533)    # Load the logo

    def display(self, screen, currentScreenIndex):
        play = Sound() 
        # Check if left mouse button is pressed
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))

        # is mouse pointer over the play button
        if collides(self.back[RECT]):
            self.back[IMG] = pygame.image.load("img/back_hover.png")
            if isPressed:
                currentScreenIndex = STARTSCREEN
                play.select() 

        # nothing of above, set all buttons to start position
        else:
            self.back[IMG] = pygame.image.load("img/back.png")

        # Draw all screen elements
        screen.blit(self.bg[IMG], self.bg[RECT])
        screen.blit(self.back[IMG], self.back[RECT])
        
        # Send report to controller about current position
        return currentScreenIndex

class AboutScreen(object):
    def __init__(self):
        '''
        START RULES INIT
        '''
        # Load all graphics for this screen
        self.bg = createGraphics("img/about_bg.png", 0, 0)    # Load the background
        self.back = createGraphics("img/back.png",20,533)    # Load the logo


    def display(self, screen, currentScreenIndex):
        play = Sound() 
        # Check if left mouse button is pressed
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))

        # is mouse pointer over the play button
        if collides(self.back[RECT]):
            self.back[IMG] = pygame.image.load("img/back_hover.png")
            if isPressed:
                currentScreenIndex = STARTSCREEN
                play.select() 

        # nothing of above, set all buttons to start position
        else:
            self.back[IMG] = pygame.image.load("img/back.png")

        # Draw all screen elements
        screen.blit(self.bg[IMG], self.bg[RECT])
        screen.blit(self.back[IMG], self.back[RECT])
        
        # Send report to controller about current position
        return currentScreenIndex

class TopScreen(object):
    def __init__(self):
        '''
        TOP10 SCREEN INIT
        '''
        # Init the font
        self.largefont = pygame.font.SysFont("Impact", 20)
        self.smallfont = pygame.font.SysFont("Impact", 15)

        # Load background and back button
        self.topbg = createGraphics("img/top10_bg.png",0,0) # Load the background
        self.back = createGraphics("img/back.png",20,533)  # Load the back button
        
    def display(self, screen, topdata, currentScreenIndex):
        play = Sound() 
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))
        top = pygame.image.load("img/top10.png")

        # if mosue is over back button
        if collides(self.back[RECT]):
            # display hover graphic
            self.back[IMG] = pygame.image.load("img/back_hover.png")
            if isPressed:
                # if mosue is pressed go back
                currentScreenIndex = 0
                play.select()
        else:
            # else display regular back button
            self.back[IMG] = pygame.image.load("img/back.png") 

        # Draw
        screen.blit(self.topbg[IMG], self.topbg[RECT])
        screen.blit(self.back[IMG], self.back[RECT])
        
        # Print out top 10 score
        for number,score in enumerate(topdata):
            number += 1     # display count from 1, not 0
            line = 288 + (number-4)*30  # after line 4 increase line distance from top

            # write rank, points and date to screen
            rank = self.largefont.render(str(number) + '.', 1, (255,255,255))
            points = self.largefont.render(score[1] + ' stig', 1, (255,255,255))
            date = self.smallfont.render(score[0], 1, (255,255,255))    
            '''
            TODO: Display name of player instead of date?
            '''
            # display info for nr 1
            if number == 1:
                screen.blit(points, (366, 130))
                screen.blit(date, (366, 110))

            # display info for nr 2
            elif number == 2:
                screen.blit(points, (278, 148))
                screen.blit(date, (278, 128))

            # display info for nr 3
            elif number == 3:
                screen.blit(points, (455, 160))
                screen.blit(date, (455, 140))

            # display info for nr 4-10
            else:
                screen.blit(rank, (320, line))
                screen.blit(points, (350, line))
                screen.blit(date, (425, line+5))

        # Send report to controller about current position
        return currentScreenIndex

class PlayScreen(object):
    def __init__(self):
        '''
        PLAY SCREEN INIT
        '''
        # Init the font
        self.largefont = pygame.font.SysFont("Impact", 20)
        self.smallfont = pygame.font.SysFont("Impact", 15)

        # Load all graphics for the screen
        self.playbg = createGraphics("img/play_bg.png", 0,0)            # load the backgorund   
        self.pause = createGraphics("img/pause.png", 745,450)           # load the pause button
        self.mute = createGraphics("img/mute.png", 745,496)             # load the mute button
        self.undo = createGraphics("img/undo.png", 745,542)             # load the undo button
        self.deck = createGraphics("img/deck.png", 21,449)              # load the deck graphic
        self.menubg = createGraphics("img/pause_menu_bg.png", 223,70)   # load the pause menu popup 
        self.playOn = createGraphics("img/halda_afram.png", 242,99)     # load the play on button in menu
        self.playAgain = createGraphics("img/byrja_aftur.png", 242,211) # load the play again button in menu
        self.stopGame = createGraphics("img/haetta_leik.png", 242,323)  # load the stop game button in menu
        self.endscreen = createGraphics("img/lose_bg.png", 0,0)         # load the loose screen 
        self.winscreen = createGraphics("img/win_bg.png", 0,0)          # load the win screen
        self.register_bg = createGraphics("img/register_bg.png", 0,0)       # load the top 10 register screen
        self.view_toplist = createGraphics("img/view_toplist.png", 262,363)     # load the view top list button

        # For music player
        self.last_song = createGraphics("img/last_song.png", 356,7)
        self.play_song = createGraphics("img/pause_song.png", 381,7)
        self.next_song = createGraphics("img/next_song.png", 412,7)

        self.song = 0
        self.initPlayer = True

        # place cards on table in first iteration
        self.initBoardMode = True

        self.sound = True 
        self.i = 0 

        self.j = 0

        play = Sound() 

        #card taken from deck
        self.lastStock = False

        '''
        CARDS INIT
        '''
        self.suits = 'hsdc'     #hearts, spades, diamonds, clubs
        self.ranks = '23456789TJQKA'    # all card types
        cardslist = [rank + suit for suit in self.suits for rank in self.ranks] # create dummy deck
        self.cardsImg = {}  # list that will contain all card graphics

        # create card graphic for every card in cardslist and put into self.cardsImg
        for card in cardslist: 
            self.cardsImg[card] = createGraphics("img/cards/" + card + ".png",0,0)

        '''
        DRAGMODE INIT
        '''
        self.mouseInDeck = False
        self.dragmode = False
        self.selectedCard = None
        self.selectedCardOrigPosL = None
        self.selectedCardOrigPosT = None
        self.displayMenu = False

        '''
        SCORE INIT
        '''
        self.score = Score()
        self.currentScore = self.largefont.render(str(self.score.returnScore()), 1, (255,255,255))
        self.currentScoreRect = self.currentScore.get_rect()
        self.currentScoreRect = self.currentScoreRect.move(20,8)
        
        # count successful moves in a row
        self.combo = 0

        # finalTime is set when game ends and is sent to high score etc
        self.finalTime = 0

        # Controls if to dispaly end screens or not
        self.displayLoseScreen = False
        self.displayWinScreen = False
        self.checkGameStatus = True

        self.gameResults = False

        '''
        TIME INIT
        '''
        # Time since program was executed
        self.startTime = pygame.time.get_ticks()

        # Time in pause mode
        self.pauseTime = 0

        # Object to write time to screen
        self.displayTime = self.smallfont.render('Tími: ' + str(pygame.time.get_ticks() - self.startTime), 1, (255,255,255))
        self.displayTimeRect = self.displayTime.get_rect()
        self.displayTimeRect = self.displayTimeRect.move(100,8)

        self.highscore = Highscore()
        self.displayRegister = False

        '''
        TEXT INPUT INIT
        '''
        self.txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='')

    def gameOver(self, deck, pile, minidecks):
        '''
            Checks if the user has no more moves to make.
        '''
        gameover = True     # assume the game is over
        # If the deck is empty check if card in any minideck can go to pile
        if deck.isEmpty():
            for minideck in minidecks:
                if not minideck.isEmpty():
                    if deck.isMatch(minideck.peek(),pile.topCard()):
                        gameover = False
                        break
        else:
            # deck is not empty so the game is not over
            gameover = False
        return gameover


    def display(self, screen, currentScreenIndex, deck, pile, minidecks):
        play = Sound() 

        # Is left mouse button pressed
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))

        # Do we need to startover
        startover = False

        IMG = 0     # Location of graphic object in card list
        RECT = 1    # Location of rect object in card list

        # Count empty minidecks
        numberofEmpties = 0     # Number of empty minidecks  
        for minideck in minidecks:
            if  minideck.isEmpty():
                numberofEmpties += 1

        # Is mouse over mute button
        if collides(self.mute[RECT]):
            
            if self.i%2==0:
                self.mute[IMG] = pygame.image.load("img/mute_hover.png")
            else:
                self.mute[IMG] = pygame.image.load("img/mute.png")
            if isPressed and self.i%2==0:
                self.mouseInDeck = True
            elif  not isPressed and self.mouseInDeck and self.i%2==0:
                self.mute[IMG] = pygame.image.load("img/mute_press.png")
                self.mouseInDeck = False
                self.sound = False
                self.i += 1
                isPressed = False

                play.pauseSong()

               
            elif isPressed and self.i%2==1 and self.mouseInDeck == False:
                self.mouseInDeck = True
            elif not isPressed and self.mouseInDeck and self.i%2==1:
                self.mute[IMG] = pygame.image.load("img/mute.png")
                self.mouseInDeck = False
                self.sound = True
                self.i += 1
                isPressed = False
                play.resumeSong()
            
        
        # Is mouse over undo button
        elif collides(self.undo[RECT]):
            self.undo[IMG] = pygame.image.load("img/undo_hover.png")
            if isPressed:
                #Undo last action
                if pile.isEmpty():
                    card = pile.topCard()
                    if self.lastStock: 
                        deck._deck.append(card)
                        pile.takeLastCard()
                        self.lastStock = False
                        self.combo = 0
                        
        # Is the deck being clicked
        elif collides(self.deck[RECT]) and isPressed:
            # Wait until mouse is released
            self.mouseInDeck = True

        # Is mouse being released over deck and was it clicked before
        elif collides(self.deck[RECT]) and not isPressed and self.mouseInDeck:
            self.mouseInDeck = False
            # Check if deck is empty
            if not deck.isEmpty():

                if self.sound and self.combo > 2:
                    play.comboBreaker()
                # reset combo counter
                self.combo = 0

                # Draw card and place it on the pile
                drawn_card = deck.draw_card()

                #update that last action was from deck
                self.lastStock = True

                self.cardsImg[drawn_card][RECT] = self.cardsImg[pile.topCard()][RECT]
                pile.put(drawn_card)
                if self.sound == True:
                    play.drawCard() 

        else:
            # No action required, make sure buttons are in original position
            self.pause[IMG] = pygame.image.load("img/pause.png")
            if self.i%2==1 and self.mouseInDeck == False:
                self.mute[IMG] = pygame.image.load("img/mute_press.png")
            elif self.i%2==0 and self.mouseInDeck == False:
                self.mute[IMG] = pygame.image.load("img/mute.png")
            self.undo[IMG] = pygame.image.load("img/undo.png")

        # Draw play, mute and undo button to screen
        screen.blit(self.playbg[IMG], self.playbg[RECT])
        screen.blit(self.mute[IMG], self.mute[RECT])
        screen.blit(self.undo[IMG], self.undo[RECT])


        '''
        MUSIC PLAYER 
        '''
        screen.blit(self.last_song[IMG], self.last_song[RECT])
        screen.blit(self.play_song[IMG], self.play_song[RECT])
        screen.blit(self.next_song[IMG], self.next_song[RECT])

        if abs(self.song) == play.getLenPlaylist():
            self.song = 0

        if self.initPlayer:
            self.song = randint(0,play.getLenPlaylist()-1)
            play.playSong(self.song)
            self.initPlayer = False

        if collides(self.last_song[RECT]):
            self.last_song[IMG] = pygame.image.load("img/last_song_hover.png")
            if isPressed:
                self.song -= 1
                if abs(self.song) == play.getLenPlaylist():
                    self.song = 0
                play.playSong(self.song)

        elif collides(self.play_song[RECT]):
            if self.j%2 == 0:
                self.play_song[IMG] = pygame.image.load("img/pause_song_hover.png")
            else:
                self.play_song[IMG] = pygame.image.load("img/play_song_hover.png")
            if isPressed and self.j%2 == 0:
                self.mouseInDeck = True
            elif not isPressed and self.mouseInDeck and self.j%2 == 0:
                self.play_song[IMG] = pygame.image.load("img/play_song.png")
                self.mouseInDeck = False
                self.j += 1
                play.pauseSong()
            elif isPressed and self.j%2==1 and self.mouseInDeck == False:
                self.mouseInDeck = True
            elif not isPressed and self.mouseInDeck and self.j%2==1:
                self.play_song[IMG] = pygame.image.load("img/pause_song.png")
                self.mouseInDeck = False
                self.j += 1
                isPressed = False
                play.resumeSong()

        elif collides(self.next_song[RECT]):
            self.next_song[IMG] = pygame.image.load("img/next_song_hover.png")
            if isPressed:
                self.song += 1
                if abs(self.song) == play.getLenPlaylist():
                    self.song = 0

                play.playSong(self.song)
        else:
            self.last_song[IMG] = pygame.image.load("img/last_song.png")
            if self.j%2 == 1:
                self.play_song[IMG] = pygame.image.load("img/play_song.png")
            else:
                self.play_song[IMG] = pygame.image.load("img/pause_song.png")
            self.next_song[IMG] = pygame.image.load("img/next_song.png")

        nowplaying = self.largefont.render('i spilun: ' + play.getSongName(self.song), 1, (255,255,255))
        screen.blit(nowplaying, (450,6))

        # Place cards on the board
        if self.initBoardMode:
            # Display the pile
            self.cardsImg[pile.topCard()][RECT] = self.cardsImg[pile.topCard()][RECT].move(131,450)

            # Locate all cards in minidecks 
            xpos = 20
            ypos = 57
            for minideck in minidecks:
                for card in minideck:
                    self.cardsImg[card][RECT] = self.cardsImg[card][RECT].move(xpos,ypos)
                    ypos += 50
                xpos += 110
                ypos = 57
            
            # Only want to run this if loop once
            self.initBoardMode = False

        # Get the mouse position
        mousepos = pygame.mouse.get_pos()

        # If we are in dragmode
        if self.dragmode:
            # and if mouse is pressed
            if isPressed:
                # make selected card follow mouse position, -50 to place cursor in center of card
                self.cardsImg[self.selectedCard][RECT][0] = mousepos[0]-50
                self.cardsImg[self.selectedCard][RECT][1] = mousepos[1]-50

            # Card released over pile, check if card can go to pile
            elif not isPressed and self.cardsImg[self.selectedCard][RECT].colliderect(self.cardsImg[pile.topCard()][RECT]) and Deck.isMatch(self.selectedCard, pile.topCard()):
                # the card can go to pile, move card from minideck to pile

                self.combo += 1

                #Play combo sound if combo
                if self.combo == 3 and self.sound:
                    play.combo(3)

                elif self.combo == 5 and self.sound:
                    play.combo(3)

                elif self.combo == 10 and self.sound:
                    play.combo(3)

                elif self.combo == 20 and self.sound:
                    play.combo(3)

                self.score.getComboScore(self.combo)
                self.score.normalMove()

                # find out in what minideck selected card was
                for minideck in minidecks:
                    # check if the card was in selected minideck
                    if self.selectedCard in minideck:
                        # pop the card from the minideck to the top of the pile
                        self.cardsImg[self.selectedCard][RECT] = self.cardsImg[pile.topCard()][RECT]
                        pile.put(minideck.pop())
                        
                        #update lastStock
                        self.lastStock = False

                        if self.sound:
                            play.placeCard() 
                        
                        # re-init dragmode
                        self.selectedCard = None
                        self.selectedCardOrigPosL = None
                        self.selectedCardOrigPosT = None
                        self.dragmode = False
                        break
            else:
                # card can't go to pile
                if self.sound and self.combo > 2:
                    play.comboBreaker()

                # reset combo counter
                self.combo = 0

                # move it back to its original position in minideck
                self.cardsImg[self.selectedCard][RECT][0] = self.selectedCardOrigPosL
                self.cardsImg[self.selectedCard][RECT][1] = self.selectedCardOrigPosT
                if self.sound:
                    play.wrongPlayed() 
                # re-init dragmode
                self.selectedCard = None
                self.dragmode = False
        else:
            # Check if we need to enable drag mode
            for minideck in minidecks:
                # Start dragmode when user clicks card for first time
                if not minideck.isEmpty() and self.cardsImg[minideck.peek()][RECT].collidepoint(mousepos) and isPressed:
                    # start dragmode and start drag
                    self.dragmode = True
                    self.selectedCard = minideck.peek()
                    self.selectedCardOrigPosL = self.cardsImg[minideck.peek()][RECT][0]
                    self.selectedCardOrigPosT = self.cardsImg[minideck.peek()][RECT][1]
                    break

        # Draw pile
        screen.blit(self.cardsImg[pile.topCard()][IMG], self.cardsImg[pile.topCard()][RECT])

         # Draw deck
        if deck.isEmpty():
            self.deck[IMG] = pygame.image.load("img/deck_empty.png")
        else:
            self.deck[IMG] = pygame.image.load("img/deck.png")
            
        screen.blit(self.deck[IMG], self.deck[RECT])
       
        # Cards in deck counter
        deckCount = self.smallfont.render(str(deck.card_count()) + ' spil eftir', 1, (255,255,255))
        # draw the count
        screen.blit(deckCount, (21,428))

        # Draw all cards in minidecks
        for minideck in minidecks:
                for card in minideck:
                    screen.blit(self.cardsImg[card][IMG], self.cardsImg[card][RECT])

        # If card is selected, draw it
        if self.selectedCard is not None:
            screen.blit(self.cardsImg[self.selectedCard][IMG], self.cardsImg[self.selectedCard][RECT])
        # if mouse hovers over pause button
        if collides(self.pause[RECT]):
            self.pause[IMG] = pygame.image.load("img/pause_hover.png")  # display hover graphic
            if isPressed:
                self.displayMenu = True     # start displaying pause menu
                self.pauseTime = pygame.time.get_ticks()    # start record time in pause mode
                if self.sound == True:
                    play.select() 

        # if we are supposed to display pause menu
        if self.displayMenu:
            # draw pause menu graphic
            self.playOn[IMG] = pygame.image.load("img/halda_afram.png")
            self.playAgain[IMG] = pygame.image.load("img/byrja_aftur.png")
            self.stopGame[IMG] = pygame.image.load("img/haetta_leik.png")

            # if play on button is hovered
            if collides(self.playOn[RECT]):
                self.playOn[IMG] = pygame.image.load("img/halda_afram_hover.png")    # display hover graphic
                # if play button is pressed
                if isPressed:
                    self.displayMenu = False    # Hide menu
                    if self.sound == True:
                        play.select() 
                    self.startTime += pygame.time.get_ticks() - self.pauseTime  # add pause time to total time to subtract
            
            # if play again button is hovered
            elif collides(self.playAgain[RECT]):
                self.playAgain[IMG] = pygame.image.load("img/byrja_aftur_hover.png")     #display hover graphic
                if isPressed:
                    startover = True    # re-init playscreen class to start a new game
                    if self.sound == True:
                        play.select() 

            # if stop game button is hovered
            elif collides(self.stopGame[RECT]):
                self.stopGame[IMG] = pygame.image.load("img/haetta_leik_hover.png")  # display hover graphic
                if isPressed:
                    # end game and go to start screen
                    play.pauseSong()
                    currentScreenIndex = 0
                    startover = True
                    if self.sound == True:
                        play.select() 

            # draw the menu 
            screen.blit(self.menubg[IMG], self.menubg[RECT])
            screen.blit(self.playOn[IMG], self.playOn[RECT])
            screen.blit(self.playAgain[IMG], self.playAgain[RECT])
            screen.blit(self.stopGame[IMG], self.stopGame[RECT])

        # draw pause button
        screen.blit(self.pause[IMG], self.pause[RECT])

        # Update score
        self.currentScore = self.largefont.render('Stig: ' + str(self.score.returnScore()), 1, (255,255,255))
        screen.blit(self.currentScore, self.currentScoreRect)

        # Update time
        if self.displayMenu:
            displayTimeString = str(self.pauseTime - self.startTime)
        else:
            displayTimeString = str(pygame.time.get_ticks() - self.startTime)
        displayTimeString = displayTimeString[:-3]

        # write time to screen
        self.displayTime = self.largefont.render('Klukka: ' + displayTimeString, 1, (255,255,255))
        screen.blit(self.displayTime, self.displayTimeRect)

        # check if we are in 'game finished' mode
        if self.displayLoseScreen or self.displayWinScreen:

            '''
            TODO: Highscore registration screen
            '''
            if isPressed:
                if self.highscore.parseHighscores(self.score.getSumScore(self.gameResults)):
                    self.displayWinScreen = False
                    self.displayLoseScreen = False
                    self.displayRegister = True
                else:
                    currentScreenIndex = STARTSCREEN
                    startover = True

            color = (192, 57, 43)
            if self.displayLoseScreen:
                # if game was lost set color theme to red
                color = (192, 57, 43)
                self.gameResults = False
            elif self.displayWinScreen:
                # if game was won set color theme to green
                color = (49, 182, 144) 
                self.gameResults = True

            # create drawable objects for score and time. Score info is requested from model
            timeLabel = self.smallfont.render(str(self.finalTime) , 1, color)
            pointLabel = self.smallfont.render(str(self.score.returnNormalScore()), 1, color)
            bonuspointLabel = self.smallfont.render(str(self.score.returnCombo()), 1, color)
            timepointLabel = self.smallfont.render(str(self.score.getTimeScore(int(self.finalTime), self.gameResults)), 1, color)
            totalpointLabel = self.largefont.render(str(self.score.getSumScore(self.gameResults)), 1, color)

            # if lose screen draw lose screen
            if self.displayLoseScreen:
                screen.blit(self.endscreen[IMG], self.endscreen[RECT])

            # if win screen draw win screen
            elif self.displayWinScreen:
                screen.blit(self.winscreen[IMG], self.winscreen[RECT]) 

            # draw info to screen
            screen.blit(timeLabel, timeLabel.get_rect().move(369,216))
            screen.blit(pointLabel, pointLabel.get_rect().move(369,280))
            screen.blit(bonuspointLabel, bonuspointLabel.get_rect().move(369,305))
            screen.blit(timepointLabel, timepointLabel.get_rect().move(369,330))
            screen.blit(totalpointLabel, totalpointLabel.get_rect().move(369,353))
        
        # check if game is over
        gameover = PlayScreen.gameOver(self, deck, pile, minidecks)

        # if game is over and game status hasn't been checked
        if gameover and self.checkGameStatus:
            play.pauseSong()
            self.displayLoseScreen = True       # request lose screen
            self.finalTime = displayTimeString  # stop and save timer to variable
            self.checkGameStatus = False        # we only need to check game status once in each game
            if self.sound == True:
                    play.gameOver() 

        # if all minidecks are empty and game status hasn't been checked
        elif numberofEmpties == len(minidecks) and self.checkGameStatus:
            play.pauseSong()
            #play winning sound
            if self.sound:
                    play.winning() 

            self.displayWinScreen = True        # request win screen
            self.finalTime = displayTimeString  # stop and save timer to variable
            self.checkGameStatus = False        # we only need to check game status once in each game
        

        if self.displayRegister:
            screen.blit(self.register_bg[IMG], self.register_bg[RECT]) 
            screen.blit(self.view_toplist[IMG], self.view_toplist[RECT]) 
            if collides(self.view_toplist[RECT]) and isPressed:
                self.highscore.addHighscore(self.score.getSumScore(self.gameResults), self.txtbx.getValue())
                currentScreenIndex = TOPSCREEN
                startover = True

            # events for txtbx
            events = pygame.event.get()
            # process other events
            '''
            for event in events:
                # close it x button si pressed
                if event.type == QUIT: return
            '''
            # update txtbx
            self.txtbx.update(events)
            # blit txtbx on the sceen
            self.txtbx.draw(screen)
            # refresh the display
            #pygame.display.flip()

        # Send report to controller about current position
        return currentScreenIndex, startover