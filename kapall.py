#encoding: utf-8
import sys, pygame
from Screens import StartScreen, PlayScreen, TopScreen, AboutScreen, RulesScreen, IntroScreen
from pygame import *
from deck import Deck
from minideck import Minideck
from pile import Pile
from sound import Sound
import os

#constants
STARTSCREEN = 0
TOPSCREEN = 1
PLAYSCREEN = 2
NUMBEROFMINID = 7
CARDSINMINIDECK = 5
RULESSCREEN = 3
ABOUTSCREEN = 4
INTROSCREEN = 5

clock = pygame.time.Clock()

def initGame(mastersound):
    '''
        Initialize a new model of the game:

        Starts the intro song

        returns a tuple 
            a deck
            a list of minidecks
            a pile
            a new playscreen
    '''


    deck = Deck()
    pile = Pile()
    minidecks = []

    mastersound.stop()
    mastersound.intro()

    #Initialize a list of slots
    
    for i in range(NUMBEROFMINID):
        minidecks.append(Minideck(deck.draw_cards(CARDSINMINIDECK)))



    pile.put(deck.draw_card())

    return deck, minidecks, pile, PlayScreen()

def getTopscore(highscorefile):
    '''
        returns a score list
    '''
    path = os.path.abspath(highscorefile)
    if os.path.isfile(highscorefile):
        #read the file
        f = open(highscorefile,'r')
        lines = f.readlines()
        #put it into 2 lists

        scores = []
        for line in lines:
            scores.append(line.strip().split(':'))
        f.close()
        return scores
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
        return getTopscore(highscorefile)

def runGame():
   
    
    pygame.init()
    # Set window size
    size = width, height = 800, 600
    # Create the window
    screen = pygame.display.set_mode(size)
    
    #Create the sound of startscreeen
    mastersound = Sound()

    #Initialize all screens
    screens = [None]*6
    screens[STARTSCREEN] = StartScreen()
    screens[TOPSCREEN] = TopScreen()
    screens[PLAYSCREEN] = PlayScreen()
    screens[RULESSCREEN] = RulesScreen()
    screens[ABOUTSCREEN] = AboutScreen()
    screens[INTROSCREEN] = IntroScreen()


    #Current screen
    currentScreenIndex = INTROSCREEN
    
    #starts a new game
    startover = True

    #highscoredata
    topdata = getTopscore("highscores.txt")
   
    #EVENT LOOP
    while 1:
        clock.tick(30)

        #Exit button triggered
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #Is left muse pressed
        isPressed = (pygame.mouse.get_pressed() == (1,0,0))  

        #Initialize a new model of the game
        if startover:
            deck, minidecks, pile, screens[PLAYSCREEN] = initGame(mastersound)
            startover = False

        if currentScreenIndex == INTROSCREEN:
            currentScreenIndex = screens[currentScreenIndex].display(screen,currentScreenIndex)

        elif currentScreenIndex == STARTSCREEN:
            currentScreenIndex = screens[currentScreenIndex].display(screen,currentScreenIndex)

            # init clock
            screens[PLAYSCREEN].startTime = pygame.time.get_ticks()
        elif currentScreenIndex == TOPSCREEN:
            topdata = getTopscore("highscores.txt")
            currentScreenIndex = screens[currentScreenIndex].display(screen, topdata, currentScreenIndex)
              
        elif currentScreenIndex == PLAYSCREEN:
            mastersound.stop()
            currentScreenIndex, startover = screens[currentScreenIndex].display(screen,currentScreenIndex, deck, pile, minidecks)

        elif currentScreenIndex == RULESSCREEN:
            currentScreenIndex = screens[currentScreenIndex].display(screen,currentScreenIndex)
            
        elif currentScreenIndex == ABOUTSCREEN:
            currentScreenIndex = screens[currentScreenIndex].display(screen,currentScreenIndex)

        # Refresh screen
        pygame.display.flip()




if __name__ == '__main__':
    runGame()




