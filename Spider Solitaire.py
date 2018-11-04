#Harvey Sidebottom
#PyGame
#Card Size is 100*146*24
# 6 decks

#__Imports Pygame Functions__
import pygame, sys 
from pygame.locals import *
import random
import pickle

pygame.init()
#FPS = 15
#fpsClock = pygame.time.Clock()
#¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class StartGame():
    def __init__(self):

        #_____Creates colours_____
        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)
        self.RED   = (128,  0,  0)
        self.GREEN = (35, 108, 35)
        self.BLUE  = (  0,  0,255)
        #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        #_______________Imports the cards to be used_______________
        self.AceofClubs = pygame.image.load('Ace of Clubs.JPG')
        self.TwoofClubs = pygame.image.load('Two of Clubs.JPG')
        self.ThreeofClubs = pygame.image.load('Three of Clubs.JPG')
        self.FourofClubs = pygame.image.load('Four of Clubs.JPG')
        self.FiveofClubs = pygame.image.load('Five of Clubs.JPG')
        self.SixofClubs = pygame.image.load('Six of Clubs.JPG')
        self.SevenofClubs = pygame.image.load('Seven of Clubs.JPG')
        self.EightofClubs = pygame.image.load('Eight of Clubs.JPG')
        self.NineofClubs = pygame.image.load('Nine of Clubs.JPG')
        self.TenofClubs = pygame.image.load('Ten of Clubs.JPG')
        self.JackofClubs = pygame.image.load('Jack of Clubs.JPG')
        self.QueenofClubs = pygame.image.load('Queen of Clubs.JPG')
        self.KingofClubs = pygame.image.load('King of Clubs.JPG')
        self.BlankCard = pygame.image.load('Blank Card.JPG')
        
        self.BackofCard = pygame.image.load('Back of Card.JPG')
        self.BackofCard2 = pygame.image.load('Back of Card2.JPG')
        self.BackofCard3 = pygame.image.load('Back of Card3.JPG')
        self.BackofCard4 = pygame.image.load('Back of Card4.JPG')
        self.BackofCard2 = pygame.transform.scale(self.BackofCard2, (100, 146))
        self.BackofCard3 = pygame.transform.scale(self.BackofCard3, (100, 146))
        self.BackofCard4 = pygame.transform.scale(self.BackofCard4, (100, 146))
        
        self.back3 = pygame.image.load('back3.JPG')
        self.back3 = pygame.transform.scale(self.back3, (1300, 700))
        self.ximage = pygame.image.load('x.JPG')
        self.ximage = pygame.transform.scale(self.ximage, (100, 160))
        self.ximage = pygame.transform.rotate(self.ximage,-10)
        #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        #_________________________________Creates Variables_________________________________________________________________________
        self.Printing_Card_x = 10#These are used for the intital printing process
        self.Printing_Card_y = 40
        self.CardList = []#The main CardList used throughout the program
        self.CardCounter = 0#Used when reprinting cards
        self.OnTop = False#This is used when checking if two cards are on top of each other
        self.ColumnNumber = 0#Which column the card is in
        self.ColumnSize = 1#How large each column is
        self.BlankSpaceList = [10,140,270,400,530,660,790,920,1050,1180]#Creates a list that cards positions can be compared against
        self.BlankSpaceList2 = [10,140,270,400,530,660,790,920,1050,1180]#Used to detect which columns are blank
        self.x = 0#MouseUp x
        self.y = 0#MouseUp y
        self.mx = 0#MouseDown x
        self.my = 0#MouseDown y
        self.CheckBlank = False#A check to see if a card is already in a slot
        self.CardValue = 0#Allows for correct card placing
        self.CounterForMultipleCardTransition = 0#A counter for how many cards are transitioning at once

        #The full list of cards in the game
        self.FullCardList = ['AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs']
        self.UnturnedCount = [3,3,3,3,3,3,3,3,2,2]#This is used to measure how many cards are in each column at the start
        self.UnturnedFinalCount = 8#Used for the printing process to ensure each column has the correct amount of unturned cards
        self.CardBackList = []#A list used to store the unturned cards
        self.DisplayOrNot = 'False'#Used when printing the unturned cards
        self.CurrentCard = ''#The current card being used
        self.CurrentList = []#A temporary list created and wiped later
        self.PrintingCardList = []#A list used when displaying the intial 10 cards
        self.b2b = 0#Used when calculating how many cards are unturned in each row
        self.MoveCounter = 0#Counter of how many moves are made
        self.RandomChoiceList = [['AceofClubs',self.AceofClubs,1],['TwoofClubs',self.TwoofClubs,2],['ThreeofClubs',self.ThreeofClubs,3],['FourofClubs',self.FourofClubs,4],['FiveofClubs',self.FiveofClubs,5],['SixofClubs',self.SixofClubs,6],['SevenofClubs',self.SevenofClubs,7],['EightofClubs',self.EightofClubs,8],['NineofClubs',self.NineofClubs,9],['TenofClubs',self.TenofClubs,10],['JackofClubs',self.JackofClubs,11],['QueenofClubs',self.QueenofClubs,12],['KingofClubs',self.KingofClubs,13]]
        self.CardBackUsed = self.BackofCard
        self.CardBackUsedNumber = 1
        self.SkinSelectX = 290
        self.SkinSelectY = 290

        #Stock
        self.StockDrawCount = 4#How many times the stock can be clicked
        self.TheX = 10#Used for printing the cards the stock uses
        self.TheY = 10

        #Full Stacks
        self.CardClear = True#Used for determining whether a full stack has been made
        self.CheckWinAmount = 6#The amount of completed stacks needed to win

        self.CheckSave = True#Used to see if the user has chosen to save their game
        self.IsLoaded = False#A boolean check to see if the user is playing a new game or an existing one
        #Used for converting numbers back to images (Pickle does not let you save images/surface objects)
        self.LoadFixCardList = [[1,self.AceofClubs],[2,self.TwoofClubs],[3,self.ThreeofClubs],[4,self.FourofClubs],[5,self.FiveofClubs],[6,self.SixofClubs],[7,self.SevenofClubs],[8,self.EightofClubs],[9,self.NineofClubs],[10,self.TenofClubs],[11,self.JackofClubs],[12,self.QueenofClubs],[13,self.KingofClubs]]

        self.HelpMidGame = False#Checks if the help is midgame or not
        #Coordinates used for displaying the ace that indicates a full stack has been made
        self.ShowMadeStackx = 400
        self.ShowMadeStacky = 660
        
        self.HelpUser = True#Called to show the help screen
        self.PageNumber = 1#The page the help screen is on
        self.CheckUnder = 0#Used to ensure card cannot be place on cards that are obstructed even it they are in the right order
        
        #Font Sizes
        self.FontSize=48
        self.FontBig=100
        self.FontHuge=140

        #Fonts
        self.Font = pygame.font.SysFont(None, self.FontSize)
        self.FontBig = pygame.font.SysFont(None, self.FontBig)
        self.FontHuge = pygame.font.SysFont(None, self.FontHuge)
        
        #Text that is displayed
        self.Stock = self.Font.render('Stock', True, (self.WHITE))
        self.NewGame = self.Font.render('New Game', True, (self.BLACK))
        self.LoadGame = self.Font.render('Load Game', True, (self.BLACK))
        self.QuitGame = self.Font.render('Quit Game', True, (self.BLACK))
        self.Title = self.FontBig.render('Spider Solitaire', True, (self.WHITE))
        self.Winner = self.FontHuge.render('Congratulations! You win', True, (self.WHITE))
        self.Continue = self.FontBig.render('Press Enter to Quit', True, (self.WHITE))
        self.Menu = self.FontBig.render('Press Space to go back to the menu', True, (self.WHITE))
        self.ReturnMenu = self.Font.render('Menu', True, (self.BLACK))
        self.MovesMade = self.Font.render(('Moves: '+str(self.MoveCounter)), True, (self.WHITE))
        self.SaveCheck = self.FontBig.render('Do you want to save your game?', True, (self.WHITE))
        self.Yes = self.FontBig.render('Yes', True, (self.BLACK))#Colour
        self.No = self.FontBig.render('No', True, (self.BLACK))#Colour
        self.Help = self.Font.render('Help', True, (self.BLACK))
        self.Page1 = self.Font.render('Page 1', True, (self.BLACK))
        self.Page2 = self.Font.render('Page 2', True, (self.BLACK))
        self.QuestionHelp = self.Font.render('?', True, (self.BLACK))
        self.BackGame = self.Font.render('Back', True, (self.BLACK))
        self.ChangeSkin = self.Font.render('Change Skin', True, (self.BLACK))
        self.Pick = self.FontBig.render('Pick a Skin for your cards', True, (self.WHITE))
        
        #Messages on the help screen__________________________________________________________________________________________________________
        self.HelpLine1 = self.Font.render('To win the game, all cards must be arranged in eight sequences of same-', True, (self.WHITE))
        self.HelpLine2 = self.Font.render('suit from King-to-Ace (e.g. K-Q-J-10-9-8-7-6-5-4-3-2-A, all clubs). Once a', True, (self.WHITE))
        self.HelpLine3 = self.Font.render('sequence is completed, the game automatically moves it to a foundation pile.', True, (self.WHITE))
        
        #Page 1
        self.HelpLine4 = self.Font.render('Cards can be moved as either top card alone or as a same suit sequence', True, (self.WHITE))
        self.HelpLine5 = self.Font.render('(e.g. J-10-9), card can be attached to another pile only if they are in the', True, (self.WHITE))
        self.HelpLine6 = self.Font.render('correct sequence. If a column is blank and card of group of cards can be', True, (self.WHITE))
        self.HelpLine7 = self.Font.render('moved there. The game completes when you have made 6 full stacks of cards', True, (self.WHITE))
        self.HelpLine8 = self.Font.render('in the correct sequence. Upon making a stack it will be removed from play', True, (self.WHITE))
         #Page 2
        self.HelpLine9 = self.Font.render('When you move a card from a column if there are any unturned cards beneath it', True, (self.WHITE))
        self.HelpLine10 = self.Font.render('they will turn around and be allowed to be used in play, one card is turned', True, (self.WHITE))
        self.HelpLine11 = self.Font.render('at a time. There is also a stock pile which upon use will draw a full random', True, (self.WHITE))
        self.HelpLine12 = self.Font.render('row of cards placing one on each column. You may click the stock 4 times', True, (self.WHITE))
        self.HelpLine13 = self.Font.render('throughout the game. You will need to use all cards, in the stock and', True, (self.WHITE))
        self.HelpLine14 = self.Font.render('and all unturned cards to win and complete the full six stacks.', True, (self.WHITE))

        self.HelpLine15 = self.Font.render('You move cards by holding down the mousebutton and releasing in the', True, (self.WHITE))
        self.HelpLine16 = self.Font.render('which you wish to place the card, if it is a valid move it will move the', True, (self.WHITE))
        self.HelpLine17 = self.Font.render('card there.', True, (self.WHITE))

        self.MoveMade = False#Used for invalid moves
        self.OnlyForMoves = False
        self.InvalidMove = self.Font.render('Invalid Move!', True, (self.WHITE))
        #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    def Restart(self):
        #Used for resetting important values when you restart
        self.CardList = []
        self.BlankSpaceList = [10,140,270,400,530,660,790,920,1050,1180]
        self.FullCardList = ['AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs','AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs']
        self.UnturnedCount = [3,3,3,3,3,3,3,3,2,2]#
        self.UnturnedFinalCount = 8
        self.CardBackList = []
        self.CurrentList = []
        self.StockDrawCount = 4
        self.CheckWinAmount = 6
        self.ColumnNumber = 0
        self.MoveCounter = 0
        self.MovesMade = self.Font.render(('Moves: '+str(self.MoveCounter)), True, (self.WHITE))#Redefines so it will display correctly
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #_____________________________________________________________________________________________
    def SaveGameCheck(self):
        #Used to check if the game is going to be saved

        DISPLAYSURF.blit( self.back3,(0,0))#Background
        DISPLAYSURF.blit(self.SaveCheck,(130,150))#SaveCheck

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,300,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,310,180,80))
        DISPLAYSURF.blit(self.Yes,(590,320))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,450,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,460,180,80))
        DISPLAYSURF.blit(self.No,(605,470))
        
        pygame.display.update()#Refreshes the screen

        keys = pygame.key.get_pressed()
        
        #User Chooses if they want to save
        while True:
            for event in pygame.event.get():#Checks if a key/mouse has been pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (self.mx,self.my) = self.MouseDown()#Gets the MouseDown coordinates
                    if self.mx >= 550 and self.my >= 300 and  self.mx <= 750 and self.my <= 400:
                        self.CheckSave = True
                    elif self.mx >= 550 and self.my >= 450 and  self.mx <= 750 and self.my <= 550:
                        self.CheckSave = False
                    return self.CheckSave
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    def Save(self):
        #Saves the game to a pickle file
        Hello1 = SaveGame(Hello.CardList,Hello.BlankSpaceList,Hello.FullCardList,Hello.UnturnedCount,Hello.UnturnedFinalCount,Hello.CardBackList,Hello.CurrentList,Hello.StockDrawCount,Hello.CheckWinAmount,Hello.ColumnNumber,Hello.MoveCounter,Hello.CardBackUsedNumber)
        for x in range (len(self.CardList)):
            self.CardList[x][0] = self.CardList[x][6]#Make the images number values so they can be pickled
        pickle.dump(Hello1, open( "save.p", "wb" ) )#Saving
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        


    #___________________________________________________________________________________________
    def Load(self):
        #Loads and existing game
        Hello2 = pickle.load( open( "save.p", "rb" ) )#Loads the file
        
        self.CardList = Hello2.CardList#Returns the images to the cardlist
        self.ReturnCardList()
        
        #Resets the variables to the saved values
        self.BlankSpaceList = Hello2.BlankSpaceList
        self.FullCardList = Hello2.FullCardList
        self.UnturnedCount = Hello2.UnturnedCount
        self.UnturnedFinalCount = Hello2.UnturnedFinalCount
        self.CardBackList = Hello2.CardBackList
        self.CurrentList = Hello2.CurrentList
        self.StockDrawCount = Hello2.StockDrawCount
        self.CheckWinAmount = Hello2.CheckWinAmount
        self.ColumnNumber = Hello2.ColumnNumber
        self.MoveCounter = Hello2.MoveCounter
        self.MovesMade = self.Font.render(('Moves: '+str(self.MoveCounter)), True, (self.WHITE))
        self.CardBackUsedNumber = Hello2.CardBackUsedNumber

        if self.CardBackUsedNumber == 1:
            self.CardBackUsed = self.BackofCard
        elif self.CardBackUsedNumber == 2:
            self.CardBackUsed = self.BackofCard2
        elif self.CardBackUsedNumber == 3:
            self.CardBackUsed = self.BackofCard3
        elif self.CardBackUsedNumber == 4:
            self.CardBackUsed = self.BackofCard4
        self.IsLoaded = True
        self.StartGame()
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #________________________________________________________________
    def ReturnCardList(self):
        #Returns the images to the cardlist
        for x in range (len(self.CardList)):
            for v in range (len(self.LoadFixCardList)):
                if self.CardList[x][0] == self.LoadFixCardList[v][0]:
                    print(self.LoadFixCardList[v])
                    self.CardList[x][0] = self.LoadFixCardList[v][1]
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    def HelpShow(self):
        
        while True:
            if self.PageNumber == 1:

                DISPLAYSURF.blit( self.back3,(0,0))#Menu
                DISPLAYSURF.blit(self.Title,(385,30))#Title

                pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,540,200,100))
                pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,550,180,80))
                DISPLAYSURF.blit(self.Page2,(595,575))
                
                DISPLAYSURF.blit(self.HelpLine1,(50,110))
                DISPLAYSURF.blit(self.HelpLine2,(50,150))
                DISPLAYSURF.blit(self.HelpLine3,(50,190))

                DISPLAYSURF.blit(self.HelpLine4,(50,270))
                DISPLAYSURF.blit(self.HelpLine5,(50,310))
                DISPLAYSURF.blit(self.HelpLine6,(50,350))
                DISPLAYSURF.blit(self.HelpLine7,(50,390))
                DISPLAYSURF.blit(self.HelpLine8,(50,430))

                if self.HelpMidGame == False:
                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
                    pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
                    DISPLAYSURF.blit(self.ReturnMenu,(23,645))
                

                elif self.HelpMidGame == True:
                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
                    pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
                    DISPLAYSURF.blit(self.BackGame,(23,645))

                pygame.display.update()

                keys = pygame.key.get_pressed()

                while self.PageNumber == 1:
                    for event in pygame.event.get():#Checks if a key/mouse has been pressed
                        if event.type == pygame.MOUSEBUTTONUP:
                            (self.x,self.y) = self.MouseDown()#Gets the MouseDown coordinates
                            if self.x >= 10 and self.y >= 625 and  self.x <= 130 and self.y <= 695 and self.HelpMidGame == False:
                                self.PageNumber = 1
                                self.DisplayMenu()
                            elif self.x >= 10 and self.y >= 625 and  self.x <= 130 and self.y <= 695 and self.HelpMidGame == True:
                                self.HelpMidGame = False
                                self.PageNumber = 1
                                return self.HelpUser
                            elif self.x >= 550 and self.y >= 540 and  self.x <= 750 and self.y <= 640:
                                self.PageNumber = 2
                            

            elif self.PageNumber == 2:

                DISPLAYSURF.blit( self.back3,(0,0))#Menu
                DISPLAYSURF.blit(self.Title,(385,30))#Title

                pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,540,200,100))
                pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,550,180,80))
                DISPLAYSURF.blit(self.Page1,(595,575))

                DISPLAYSURF.blit(self.HelpLine9,(50,110))
                DISPLAYSURF.blit(self.HelpLine10,(50,150))
                DISPLAYSURF.blit(self.HelpLine11,(50,190))
                DISPLAYSURF.blit(self.HelpLine12,(50,230))
                DISPLAYSURF.blit(self.HelpLine13,(50,270))
                DISPLAYSURF.blit(self.HelpLine14,(50,310))

                DISPLAYSURF.blit(self.HelpLine15,(50,390))
                DISPLAYSURF.blit(self.HelpLine16,(50,430))
                DISPLAYSURF.blit(self.HelpLine17,(50,470))

                if self.HelpMidGame == False:
                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
                    pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
                    DISPLAYSURF.blit(self.ReturnMenu,(23,645))
                

                elif self.HelpMidGame == True:
                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
                    pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
                    DISPLAYSURF.blit(self.BackGame,(23,645))

                pygame.display.update()

                keys = pygame.key.get_pressed()

                while self.PageNumber == 2:
                    for event in pygame.event.get():#Checks if a key/mouse has been pressed
                        if event.type == pygame.MOUSEBUTTONUP:
                            (self.x,self.y) = self.MouseDown()#Gets the MouseDown coordinates
                            if self.x >= 10 and self.my >= 625 and  self.x <= 130 and self.my <= 695 and self.HelpMidGame == False:
                                self.PageNumber = 1
                                self.DisplayMenu()
                            elif self.x >= 10 and self.y >= 625 and  self.x <= 130 and self.y <= 695 and self.HelpMidGame == True:
                                self.HelpMidGame = False
                                self.PageNumber = 1
                                return self.HelpUser
                            elif self.x >= 550 and self.y >= 540 and  self.x <= 750 and self.y <= 640:
                                self.PageNumber = 1


    def SkinChange(self):
        
        DISPLAYSURF.blit( self.back3,(0,0))#Menu
        DISPLAYSURF.blit(self.Title,(385,30))#Title
        DISPLAYSURF.blit(self.Pick,(220,130))
        pygame.draw.rect(DISPLAYSURF, self.GREEN, (self.SkinSelectX,self.SkinSelectY,120,166))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
        DISPLAYSURF.blit(self.ReturnMenu,(23,645))

        DISPLAYSURF.blit(self.BackofCard,(300,300))
        DISPLAYSURF.blit(self.BackofCard2,(500,300))
        DISPLAYSURF.blit(self.BackofCard3,(700,300))
        DISPLAYSURF.blit(self.BackofCard4,(900,300))

        pygame.display.update()

        keys = pygame.key.get_pressed()

        while True:
            for event in pygame.event.get():#Checks if a key/mouse has been pressed
                if event.type == pygame.MOUSEBUTTONUP:
                    (self.x,self.y) = self.MouseDown()#Gets the MouseDown coordinates
                    if self.x >= 10 and self.my >= 625 and  self.x <= 130 and self.my <= 695:
                        self.DisplayMenu()
                        
                    elif self.mx >= 300 and self.my >= 300 and  self.mx <= 400 and self.my <= 446:
                        self.CardBackUsed = self.BackofCard
                        self.SkinSelectX = 290
                        self.CardBackUsedNumber = 1

                    elif self.mx >= 500 and self.my >= 300 and  self.mx <= 600 and self.my <= 446:
                        self.CardBackUsed = self.BackofCard2
                        self.SkinSelectX = 490
                        self.CardBackUsedNumber = 2
                    elif self.mx >= 700 and self.my >= 300 and  self.mx <= 800 and self.my <= 446:
                        self.CardBackUsed = self.BackofCard3
                        self.SkinSelectX = 690
                        self.CardBackUsedNumber = 3
                    elif self.mx >= 900 and self.my >= 300 and  self.mx <= 1000 and self.my <= 446:
                        self.CardBackUsed = self.BackofCard4
                        self.SkinSelectX = 890
                        self.CardBackUsedNumber = 4

                    DISPLAYSURF.blit( self.back3,(0,0))#Menu
                    DISPLAYSURF.blit(self.Title,(385,30))#Title
                    DISPLAYSURF.blit(self.Pick,(220,130))
                    
                    pygame.draw.rect(DISPLAYSURF, self.GREEN, (self.SkinSelectX,self.SkinSelectY,120,166))

                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
                    pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
                    DISPLAYSURF.blit(self.ReturnMenu,(23,645))

                    DISPLAYSURF.blit(self.BackofCard,(300,300))
                    DISPLAYSURF.blit(self.BackofCard2,(500,300))
                    DISPLAYSURF.blit(self.BackofCard3,(700,300))
                    DISPLAYSURF.blit(self.BackofCard4,(900,300))

                    pygame.display.update()

    #_____________________________________________________________________________________________
    def DisplayMenu(self):
        #Displays the Menu
        
        DISPLAYSURF.blit( self.back3,(0,0))#Menu
        DISPLAYSURF.blit(self.Title,(385,150))#Title

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,300,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,310,180,80))
        DISPLAYSURF.blit(self.NewGame,(562,335))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,420,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,430,180,80))
        DISPLAYSURF.blit(self.LoadGame,(558,455))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (550,540,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (560,550,180,80))
        DISPLAYSURF.blit(self.QuitGame,(562,575))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,540,200,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,550,180,80))
        DISPLAYSURF.blit(self.Help,(70,575))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (1040,540,250,100))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (1050,550,230,80))
        DISPLAYSURF.blit(self.ChangeSkin,(1060,575))

        
        pygame.display.update()#Refreshes the screen

        keys = pygame.key.get_pressed()
        
        #User Chooses what to do on the menu
        while True:
            for event in pygame.event.get():#Checks if a key/mouse has been pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (self.mx,self.my) = self.MouseDown()#Gets the MouseDown coordinates
                    if self.mx >= 550 and self.my >= 300 and  self.mx <= 750 and self.my <= 400:
                        self.Restart()
                        self.StartGame()
                    elif self.mx >= 550 and self.my >= 420 and  self.mx <= 750 and self.my <= 520:
                        self.Load()
                    elif self.mx >= 550 and self.my >= 540 and  self.mx <= 750 and self.my <= 640:
                        self.QuitTheGame()
                    elif self.mx >= 10 and self.my >= 540 and  self.mx <= 210 and self.my <= 640:
                        self.HelpShow()
                    elif self.mx >= 1040 and self.my >= 540 and  self.mx <= 1290 and self.my <= 640:
                        self.SkinChange()
                        
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    def StartGame(self):
        CardShow = True
        DISPLAYSURF.fill(self.WHITE)#Creates the screens background colour

        #__________________________________________________________________________________________________________________________________________________________________________________________________________________
        while CardShow == True and self.IsLoaded == False:
            DISPLAYSURF.blit( self.back3,(0,0))
            DISPLAYSURF.blit(self.Stock,(1195,515))
            #Makes a list of Cards which can be removed when displayed
            self.PrintingCardList = ['AceofClubs','TwoofClubs','ThreeofClubs','FourofClubs','FiveofClubs','SixofClubs','SevenofClubs','EightofClubs','NineofClubs','TenofClubs','JackofClubs','QueenofClubs','KingofClubs']

            while len(self.PrintingCardList) > 3:#Checks if the list is empty
                self.CurrentList = self.PrintingCardList#temporary assignment
                (self.CurrentCard,self.CardValue,self.randomchoice) = self.GetRandomChoice()#Calls a subroutine to find the details of the chosen card
                self.PrintingCardList = self.CurrentList

                self.ColumnNumber +=1#move to the next column
                removecard = self.PrintingCardList.index(self.randomchoice) #get the index of the card to be removed
                self.PrintingCardList.pop(removecard)#removes the card from the printing list
                self.FullCardList.pop(removecard)#Remove the card from the full list to ensure it wont be duplicated

                DISPLAYSURF.blit(self.BlankCard,(self.Printing_Card_x,self.Printing_Card_y-30))#prints the blank card

                DISPLAYSURF.blit(self.CardBackUsed,(self.Printing_Card_x,self.Printing_Card_y-30))#Prints the unturned cards row 1
                CardBack = [self.Printing_Card_x,self.Printing_Card_y-30,self.ColumnNumber,self.DisplayOrNot]
                self.CardBackList.append(CardBack)
                
                DISPLAYSURF.blit(self.CardBackUsed,(self.Printing_Card_x,self.Printing_Card_y-20))#row 2
                CardBack = [self.Printing_Card_x,self.Printing_Card_y-20,self.ColumnNumber,self.DisplayOrNot]
                self.CardBackList.append(CardBack)

                if self.UnturnedFinalCount > 0:#prints the third row checking if it requires a third card or not (last to columns in the row do not)
                    DISPLAYSURF.blit(self.CardBackUsed,(self.Printing_Card_x,self.Printing_Card_y-10,))#row 3
                    CardBack = [self.Printing_Card_x,self.Printing_Card_y-10,self.ColumnNumber,self.DisplayOrNot]
                    self.CardBackList.append(CardBack)
                self.UnturnedFinalCount -=1#Reduces the count so it is only done 8 times

                if len(self.PrintingCardList) <= 4:#This prints the unturned cards in the right positions
                    DISPLAYSURF.blit(self.CurrentCard,(self.Printing_Card_x,self.Printing_Card_y-10))#prints the chosen card on screen
                    Card = [self.CurrentCard,self.Printing_Card_x,self.Printing_Card_y-10,self.randomchoice,self.ColumnNumber,self.ColumnSize,self.CardValue]#prints it 10 lower for the last two columns
                else:
                    DISPLAYSURF.blit(self.CurrentCard,(self.Printing_Card_x,self.Printing_Card_y))#prints the chosen card on screen
                    Card = [self.CurrentCard,self.Printing_Card_x,self.Printing_Card_y,self.randomchoice,self.ColumnNumber,self.ColumnSize,self.CardValue]

                #Makes 1 element with multiple parts
                #Card holds info about each card:
                #image of card, xpos, ypos, name, position in stack, col number, size of stack)
                #SBK changed card from a tuple to a list

                self.CardList.append(Card)#Adds the Card and its x/y coordinate to a list
                self.Printing_Card_x += 130#Moves the x coordinate along for next card

            DISPLAYSURF.blit(self.CardBackUsed,(1190,550))#prints the stock pile

            pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
            pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
            DISPLAYSURF.blit(self.ReturnMenu,(23,645))
            #DISPLAYSURF.blit(self.MovesMade,(200,645))

            pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,545,70,70))
            pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,555,50,50))
            DISPLAYSURF.blit(self.QuestionHelp,(35,565))

            DISPLAYSURF.blit(self.MovesMade,(200,645))

            for ju in range (6 - self.CheckWinAmount):#Will display the complete stacks bottom most card
                DISPLAYSURF.blit(self.AceofClubs,(self.ShowMadeStackx,self.ShowMadeStacky))
                self.ShowMadeStackx +=20#Increments the card
   
            self.Printing_Card_x = 10 #Resets the Printing Card coordinates so they may be used again
            self.Printing_Card_y = 40
    
            if len(self.PrintingCardList) <= 3:#Checks if the list is empty
                CardShow = False


            DISPLAYSURF.blit(self.CardBackUsed,(1190,550))#prints the stock pile
            
            pygame.display.update()#Refreshes the screen
        self.IsLoaded = False#Resets the variable so if a new game is started it wont effect the startgame function
        #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        
        keys = pygame.key.get_pressed()
        
        #_______________Allows for user interaction________________________________
        while True:
            for event in pygame.event.get():#Checks if a key/mouse has been pressed
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.ReprintScreen()#Right mouse button refreshes screen
        #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                #______________________________________
                if event.type == QUIT:#Quits the window
                    pygame.quit()
                    sys.exit()
                #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                #______________________________________________________________________
                if event.type == pygame.MOUSEBUTTONDOWN:#Gets the MouseDown coordinates
                    (self.mx,self.my) = self.MouseDown()
                #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                #______________________________________________________________________________________________________________________________________________________________________________________________________
                if event.type == pygame.MOUSEBUTTONUP:#Gets the MouseUp coordinates
                    (self.x,self.y) = self.MouseUp()
                    UnturnCheck = True#For unturning cards and changing the unturnedcardlist

                    #__________________________________________________________________________Stock__________________________________________________________________________

                    #Checks if the stock button is pressed
                    if self.mx >= 1190 and self.mx <= 1190+90 and self.my >= 550 and self.my <=550+145 and self.StockDrawCount > 0:

                        #Gets the card values from GetRandomChoice
                        for stockboi in range (10):
                            self.CurrentList = self.FullCardList
                            (self.CurrentCard,self.CardValue,self.randomchoice) = self.GetRandomChoice()
                            self.FullCardList = self.CurrentList

                            #Updates the column Xpos and Ypos
                            StockFound = False
                            for ini in range (len(self.CardList)):
                                if self.CardList[ini][4] == stockboi+1:
                                    self.TheX = self.CardList[ini][1]
                                    self.TheY = self.CardList[ini][2]+30
                                    StockFound = True
                            if StockFound == False:
                                self.TheX = 10+(130*(stockboi))
                                self.TheY = 10

                            Card = [self.CurrentCard,self.TheX,self.TheY,self.randomchoice,stockboi+1,1,self.CardValue]#prints it 10 lower for the last two columns
                            #Makes the new unturned card
                            DISPLAYSURF.blit(self.CurrentCard,(self.TheX,self.TheY))#prints the chosen card on screen

                            self.CardList.append(Card)#Adds the new card to the CardList

                            removecard = self.FullCardList.index(self.randomchoice)#Removes the newly added card from the full list of all cards that can be added to the game
                            self.FullCardList.pop(removecard)

                            self.BlankSpaceList.append(self.TheX)
                            self.BlankSpaceList.sort()

                        #self.CardList.sort(key=lambda x: (x[1],x[2]))#Sort the cardlist by x coordinate first and then by y coordinate
                        GetMergeSort = Sort(self.CardList)
                        self.CardList = GetMergeSort
                        
                        self.StockDrawCount -=1
                        self.ReprintScreen()#Refreshes the screen
                        pygame.display.update()#Shows the changes
                    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                    #_________________________Checks if the menu button is pressed________________________
                    elif self.mx >= 10 and self.my >= 625 and  self.mx <= 130 and self.my <= 695:
                        self.CheckSave = self.SaveGameCheck()#Checks if the user wishes to save their game
                        if self.CheckSave == True:
                            self.Save()
                            self.Restart()
                            self.DisplayMenu()
                        else:
                            self.Restart()
                            self.DisplayMenu()

                    elif self.mx >= 10 and self.my >= 545 and  self.mx <= 80 and self.my <= 615:
                        self.HelpMidGame = True
                        self.PageNumber = 1
                        self.HelpUser = self.HelpShow()
                        self.ReprintScreen()#Refreshes the screen
                        pygame.display.update()#Shows the changes

##                    pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,545,70,70))
##        pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,555,50,50))
##        DISPLAYSURF.blit(self.QuestionHelp,(35,565))
                    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                    else:
                        self.CardList.reverse()
                        self.CheckBlank =  self.CheckIfRowIsBlank()#Checks if the column chosen to moves to is blank
                        self.CounterForMultipleCardTransition = self.CheckCardMoveAmount()#Checks how many cards need moving at once

                        for i in range (len(self.CardList)):#Checks the boundaries of cards
                            
                            # this detects which card was in the mx/my coordinates when the mouse was clicked down
                            if self.mx >=self.CardList[i][1] and self.mx <= self.CardList[i][1]+90 and self.my >=self.CardList[i][2] and self.my <= self.CardList[i][2]+135:
                                self.OnlyForMoves = True

                                for j in range (len(self.CardList)):

                                    if self.my >= self.y and self.my <= self.y+145 and self.mx>= self.x and self.mx <= self.x+90:#Checks if the card is being attempted to be moved to the same spot it is currently in
                                        self.OnTop = True

                                    #__________________________________________________________________________Move onto another card_________________________________________________________________________

                                    #Checks if a valid move to place a card on top of another is possible
                                    elif self.x > self.CardList[j][1] and self.x < self.CardList[j][1]+90 and self.y >= self.CardList[j][2] and self.OnTop == False and self.CheckBlank == False:

                                        for tc in range (len(self.CardList)):#Checks cards cannot be place on cards that are obstructed even it they are in the right order
                                            if self.CardList[j][4] == self.CardList[tc][4] and self.CardList[tc][2] >= self.CardList[j][2]:#Checks the column and if its x coordinate is less than the card being placed on
                                                self.CheckUnder+=1

                                        if self.CardList[i][6] < self.CardList[j][6] and self.CardList[i][6] > self.CardList[j][6]-2 and self.CheckUnder<=1:#Check if the cards may be placed upon each other based upon their values

                                            self.b2b = self.CardList[i][4]-1
                                            self.MoveMade = True

                                            for o in range (self.CounterForMultipleCardTransition):#Runs through the amount of cards thats need to be moved at once
                                    
                                                #records the col number of the col the card was put down on
                                                self.ColumnCheck = self.CardList[j][4]

                                                #SBK when you move a card you need to
                                                #update the col number
                                                #update the xpos
                                                #update the ypos
                                                #update the number of cards in the stack (this must be done for all cards in the stack)
                                                
                                                self.BlankSpaceList.append(self.CardList[j][1])#Adds the cards x position to the BlankSpaceList
                                                self.BlankSpaceList.remove(self.CardList[i][1])#Removes its previous x position from the BlankSpaceList
     
                                                #update the column of the new card
                                                self.CardList[i][4] = self.CardList[j][4]
                                                #update the xpos                                  
                                                self.CardList[i][1] = self.CardList[j][1]
                                                #update the ypos
                                                self.CardList[i][2] = self.CardList[j][2]+(o+1)*30
                                                #+(o+1)*30 basically means increment by 30 each times based upon the amount of cards being moved at once

                                                i-=1#Decreases the i value so the next card if mutliple transitions are done can be moved aswell

                                            if self.CounterForMultipleCardTransition >0:
                                                self.MoveCounter +=1#Used for a move counter
                                                self.MovesMade = self.Font.render(('Moves: '+str(self.MoveCounter)), True, (self.WHITE))#Colour

                                        for jopp in range (len(self.CardList)):
                                            if self.CardList[jopp][4] == self.CardList[i][4]-1:
                                                    UnturnCheck = False


                                        if self.UnturnedCount[self.b2b] >0 and UnturnCheck == True:#Checks that the value in the list position is greater than 1
                                            self.UnturnedCount[self.b2b]-=1#Subtracts 1

                                        self.OnTop = True#Resets the variables
                                        self.CheckUnder = 0
                                    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                                    #___________________________________________________________Move into a blank column___________________________________________________________
                                    
                                    #Checks if a card is being moved into a blank column   
                                    elif self.y >= 10 and self.y <= 145:#Checks the y
                                        for ep in range (len(self.BlankSpaceList2)):
                                            if self.x >= self.BlankSpaceList2[ep] and self.x <= self.BlankSpaceList2[ep]+90:#Checks x
                                                for ed in range (len(self.BlankSpaceList)):
                                                    if self.BlankSpaceList2[ep] == self.BlankSpaceList[ed]:#references the x against the other BlankSpaceList
                                                        CheckingTehBlankSpace = False#If set to false the loop wont be engaged
                                                if CheckingTehBlankSpace == True and self.OnTop == False and self.CheckBlank == True:

                                                    self.b2b = self.CardList[i][4]-1

                                                    #print('Position is blank')#Tells the user that it will be moved to a blank space
                                                    for k in range (len(self.CardList)):
                                                        if self.CardList[k][4] ==  j+1 and self.OnTop == False:
                         
                                                            print ('Move unable to be completed')
                                                        #Checks the move can actually be completed
                                                        elif self.CardList[k][4] !=  j+1 and self.OnTop == False:
                                                            self.MoveMade = True
                                                            for o in range (self.CounterForMultipleCardTransition):#Runs through the amount of cards thats need to be moved at once

                                                                #update the colum of the new card

                                                                self.CardList[i][4] = int((self.BlankSpaceList2[ep]-10)/130)+1#Updates the Column
                                                                #Has been changed from j+1 to k+1 slightly unsure if their is a consequence

                                                                Tempstore = self.CardList[i][1]#Used so when the old x value is overwritten i isn't lost

                                                                #Update the xpos
                                                                self.CardList[i][1] = self.BlankSpaceList2[ep]
                                                                
                                                                self.BlankSpaceList.append(self.CardList[i][1])#Adds the cards x position to the BlankSpaceList
                                                                self.BlankSpaceList.remove(Tempstore)#Removes its previous x position from the BlankSpaceList
                                                                
                                                                #update the ypos
                                                                if o ==0:#First card needs to be printed at 20
                                                                    self.CardList[i][2] = 10
                                                                else:#Every other card is +30 from that original 20
                                                                    self.CardList[i][2] = 10+(o)*30

                                                                #print('Move complete')
                                                                    
                                                                if i >=0:
                                                                    i-=1#Decreases the i value so the next card if mutliple transitions are done can be moved aswell

                                                            self.MoveCounter +=1
                                                            self.MovesMade = self.Font.render(('Moves: '+str(self.MoveCounter)), True, (self.WHITE))#Colour

                                                        self.OnTop = True#Resets the variable

                                                    for jopp in range (len(self.CardList)):
                                                        if self.CardList[jopp][4] == self.CardList[i][4]-1:
                                                            UnturnCheck = False
                                                            
                                                    if self.UnturnedCount[self.b2b] >0 and UnturnCheck == True:#Checks that the value in the list position is greater than 1
                                                        self.UnturnedCount[self.b2b]-=1#Subtracts 1

                                                    
                                    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

                                            #SBK sort the list (good opportunity to use a personalised bubble sort here

                                #s = sorted(s, key = lambda x: (x[1], x[2]))
 
                       
                        #self.CardList.sort(key=lambda x: (x[1],x[2]))#Sort the cardlist by x coordinate first and then by y coordinate
                        GetMergeSort = Sort(self.CardList)
                        self.CardList = GetMergeSort
                        self.CardClear = self.CheckWin()
                        
                        
                        if self.CheckWinAmount <=0:#Checks if the game has been won
                            self.Win()
                            
                        self.ReprintScreen()#Refreshes the screen
                        pygame.display.update()#Shows the changes

                    self.BlankSpaceList.sort()
                    self.OnTop = False#Resets the variable
                    self.CheckBlank = False#Resets the variable
                    CheckingTehBlankSpace = True#Resets the variable
                #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

##    def Sort(self):
##        for qw in range(len(self.CardList)-1,0,-1):
##            for qe in range(qw):
##                if self.CardList[qe][1]>self.CardList[qe+1][1]:
##                    temp = self.CardList[qe]
##                    self.CardList[qe] = self.CardList[qe+1]
##                    self.CardList[qe+1] = temp
##                    
##                if self.CardList[qe][1]== self.CardList[qe+1][1]:
##                    if self.CardList[qe][2]>self.CardList[qe+1][2]:
##                        temp = self.CardList[qe]
##                        self.CardList[qe] = self.CardList[qe+1]
##                        self.CardList[qe+1] = temp
##

    #________________________________________________________________________________________________Checks if a stack needs to be removed_________________________________________________________________________________________________
    def CheckWin(self):
        self.CardClear = False
        CheckWinCount = 1
        
        for n in range (len(self.CardList)):
            mn = n
            self.b2b = self.CardList[n][4]-1
            
            for wok in range (len(self.CardList)):
                #Checks how many cards need to be moved at once
                if self.CardList[wok][4] == self.CardList[n][4] and self.CardList[wok][6] < self.CardList[n][6] and self.CardList[wok][6] > self.CardList[n][6]-2 and self.CardList[wok][2] == self.CardList[n][2]+30:
                    CheckWinCount+=1
                    n+=1
                    
                    if CheckWinCount ==13:

                        if self.UnturnedCount[self.b2b] >0:#Checks that the value in the list position is greater than 1
                            self.UnturnedCount[self.b2b]-=1#Subtracts 1


                        for jhh in range (13):
                            self.BlankSpaceList.remove(self.CardList[mn][1])#Removes the x from each card that is no longer in play from the blankspacelist
                            self.CardList.remove(self.CardList[mn])#Removes the card from the CardList
                        
                        CheckWinCount = 1#Resets the values
                        self.CardClear = True
                        self.CheckWinAmount -=1
                        self.ReprintScreen()#Refreshes the screen
                        pygame.display.update()
                        return self.CardClear
                        
                    
                elif self.CardList[wok][4] == self.CardList[n][4] and self.CardList[wok][2] == self.CardList[n][2]+30 or self.CardList[wok][4] != self.CardList[n][4]:#Ensures that a card cannot be moved if it is trapped by another card
                    CheckWinCount = 1
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
               
    #_____________________________Checks if the row is blank_____________________________
    def CheckIfRowIsBlank(self):
        #Detect which column
        #Detect if there are any cards in that column
        #Detect if there are any other cards in said column
        #Detect if a new card was moved in after it was originally made blank
        
        self.CheckBlank = True#Initially sets the variable to true
 
        for l in range (len(self.BlankSpaceList2)):
            #Checks which column
            if self.x  >= self.BlankSpaceList2[l] and self.x <= self.BlankSpaceList2[l]+90:
                
                for lp in range (len(self.CardList)):
                    for lg in range (len(self.UnturnedCount)):
                        #Detects if there are still unturned cards in the column
                        if self.UnturnedCount[l] >=1 or self.CardList[lp][4] == l+1:
                            self.CheckBlank = False

                        #Detects if a new card was moved in after it was originally made blank
                        elif self.x >= self.CardList[lp][1] and self.x <= self.CardList[lp][1]+90 and self.UnturnedCount[self.CardList[lp][4]] > 0:
                            self.CheckBlank = False
                           
        return self.CheckBlank
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #________________________________________________________________Reprints the screen________________________________________________________________        
    def ReprintScreen(self):
        DISPLAYSURF.fill(self.WHITE)#Clears the board so it can be reprinted in the changed state
        DISPLAYSURF.blit( self.back3,(0,0))#Displays the background
        
        DISPLAYSURF.blit(self.Stock,(1195,515))#Displays 'Stock'
        DISPLAYSURF.blit(self.CardBackUsed,(1190,550))#prints the stock pile
        if self.StockDrawCount < 1:
            DISPLAYSURF.blit(self.ximage,(1182,535))
         
        if self.MoveMade == False and self.OnlyForMoves == True:
            self.OnlyForMoves = False
            DISPLAYSURF.blit(self.InvalidMove,(550,535))
            

        elif self.MoveMade == True:
            self.MoveMade = False
        
        pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,625,120,70))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,635,100,50))
        DISPLAYSURF.blit(self.ReturnMenu,(23,645))
        DISPLAYSURF.blit(self.MovesMade,(200,645))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (10,545,70,70))
        pygame.draw.rect(DISPLAYSURF, self.WHITE, (20,555,50,50))
        DISPLAYSURF.blit(self.QuestionHelp,(35,565))

        pygame.draw.rect(DISPLAYSURF, self.BLACK, (385,645,250,100))#Pile for completed stacks
        pygame.draw.rect(DISPLAYSURF, self.RED, (395,655,230,80))
        
        for ju in range (6 - self.CheckWinAmount):#Will display the complete stacks bottom most card
            DISPLAYSURF.blit(self.AceofClubs,(self.ShowMadeStackx,self.ShowMadeStacky))
            self.ShowMadeStackx +=20#Increments the card

        self.ShowMadeStackx = 400#Resets the X value
        

        for z in range (10):
            DISPLAYSURF.blit(self.BlankCard,(10+130*z,10))#prints the blank cards

        #Sets all the boolean values in CardBackList to False
        for jd in range (len(self.CardBackList)):
            self.CardBackList[jd][3] = 'False'

        #sets all cards that dont need turning over to 'True'
        for jf in range (len(self.CardList)):
            for jk in range (len(self.CardBackList)):
                if self.CardBackList[jk][0] == self.CardList[jf][1]:
                    self.CardBackList[jk][3] = 'True'
                    
        Complete = True
        self.CardBackList.reverse()
        for je in range(len(self.CardBackList)):
            #Checks if a card needs unturning
            if self.CardBackList[je][3] == 'False' and Complete == True:
                
                self.CurrentList = self.FullCardList
                (self.CurrentCard,self.CardValue,self.randomchoice) = self.GetRandomChoice()
                self.FullCardList = self.CurrentList

                Card = [self.CurrentCard,self.CardBackList[je][0],self.CardBackList[je][1],self.randomchoice,self.CardBackList[je][2],1,self.CardValue]#prints it 10 lower for the last two columns
                #Makes the new unturned card
                DISPLAYSURF.blit(self.CurrentCard,(self.CardBackList[je][0],self.CardBackList[je][1]))#prints the chosen card on screen

                self.CardList.append(Card)#Adds the new card to the CardList
                #self.CardList.sort(key=lambda x: (x[1],x[2]))#Sort the cardlist by x coordinate first and then by y coordinate
                GetMergeSort = Sort(self.CardList)
                self.Cardlist = GetMergeSort
                
                removecard = self.FullCardList.index(self.randomchoice)#Removes the newly added card from the full list of all cards that can be added to the game
                self.FullCardList.pop(removecard)

                self.BlankSpaceList.append(self.CardBackList[je][0])
                self.BlankSpaceList.sort()

                self.bb = je
                Complete = False

        #Removes the turned Card from the list of unturned cards          
        if Complete == False:
            self.CardBackList.pop(self.bb)

        self.CardBackList.reverse()
           
        #Displays all of the unturned cards
        for oof in range (len(self.CardBackList)):
            DISPLAYSURF.blit(self.CardBackUsed,(self.CardBackList[oof][0],self.CardBackList[oof][1]))
            
        for xd in range (len(self.CardList)):#Will print the full row of cards again
            DISPLAYSURF.blit(self.CardList[xd][0],(self.CardList[xd][1],self.CardList[xd][2]))#Prints the card in that part of the list
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #_______________________________________________________________________________________
    def MouseDown(self):
        (self.mx,self.my) = pygame.mouse.get_pos()
     #   print("mousedown x",self.mx)
     #   print("mousedown y",self.my)
        return (self.mx,self.my)
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #___________________________________________
    def MouseUp(self):
        (self.x,self.y) = pygame.mouse.get_pos()
      #  print("mouseup x",self.x)
      #  print("mouseup y",self.y)
        return (self.x,self.y)
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #__________________________________________________________________________________Checks how many cards need moving at once__________________________________________________________________________________
    def CheckCardMoveAmount(self):
        self.CounterForMultipleCardTransition = 1#Defaults the Counter to 1
        for n in range (len(self.CardList)):#Checks the boundaries of cards
            
            # this detects which card was in the mx/my coordinates when the mouse was clicked down
            if self.mx >=self.CardList[n][1] and self.mx <= self.CardList[n][1]+90 and self.my >=self.CardList[n][2] and self.my <= self.CardList[n][2]+135:
                           
                n = len(self.CardList) - (n+1) #Resets the value the value of i with the list sorted and assings a placeholder so isn't changed
                #self.CardList.sort(key=lambda x: (x[1],x[2]))#Sorts it so the list is read in the right way
                GetMergeSort = Sort(self.CardList)
                self.CardList = GetMergeSort
                
                #Check it's in the correct column
                #Lower card value,
                #In the right order numerically,
                #In the right position within the column
                 
                for m in range (len(self.CardList)):
                    #Checks how many cards need to be moved at once
                    if self.CardList[m][4] == self.CardList[n][4] and self.CardList[m][6] < self.CardList[n][6] and self.CardList[m][6] > self.CardList[n][6]-2 and self.CardList[m][2] == self.CardList[n][2]+30:
                        self.CounterForMultipleCardTransition +=1#Increases the counter by 1
                        n=n+1
                    elif self.CardList[m][4] == self.CardList[n][4] and self.CardList[m][2] == self.CardList[n][2]+30:#Ensures that a card cannot be moved if it is trapped by another card
                        self.CounterForMultipleCardTransition = 0
                        return (self.CounterForMultipleCardTransition)
                        
                self.CardList.reverse()#Puts the list back
                #print('CounterForMultipleCardTransition:',self.CounterForMultipleCardTransition)#Displays how many transitions are needed
                return (self.CounterForMultipleCardTransition)
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #____________________________________________________________________________________________
    def GetRandomChoice(self):
        self.randomchoice = (random.choice(self.CurrentList))#Selects a random card from the list

        for x in range (len(self.CurrentList)):
            for v in range (len(self.RandomChoiceList)):
                if self.randomchoice == self.RandomChoiceList[v][0]:
                    self.CurrentCard = self.RandomChoiceList[v][1]
                    self.CardValue = self.RandomChoiceList[v][2]
                    
        return(self.CurrentCard,self.CardValue,self.randomchoice)
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

    #________________________________________________________________________
    def Win(self):
        #Called if the user wins the game
        DISPLAYSURF.blit( self.back3,(0,0))#Background
        DISPLAYSURF.blit(self.Winner,(50,150))
        DISPLAYSURF.blit(self.Continue,(320,350))
        DISPLAYSURF.blit(self.Menu,(60,500)) 
        pygame.display.update()

        keys = pygame.key.get_pressed()
        
        while True:
            for event in pygame.event.get():#Checks if a key has been pressed
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    self.QuitTheGame()
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.Restart()
                    self.DisplayMenu()           
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        
    #_________Quits the Game____________
    def QuitTheGame(self):#Quits the game
        pygame.quit()
        sys.exit()
    #¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

Hello = StartGame()#Initialises class StartGame

#___________________________________________________________________________________________________________________________________________________________________________________________________________________________
class SaveGame():
    def __init__(self,CardList,BlankSpaceList,FullCardList,UnturnedCount,UnturnedFinalCount,CardBackList,CurrentList,StockDrawCount,CheckWinAmount,ColumnNumber,MoveCounter,CardBackUsedNumber): #Passes in variables from the start game class
        self.CardList = CardList
        self.BlankSpaceList = BlankSpaceList
        self.FullCardList = FullCardList
        self.UnturnedCount = UnturnedCount
        self.UnturnedFinalCount = UnturnedFinalCount
        self.CardBackList = CardBackList
        self.CurrentList = CurrentList
        self.StockDrawCount = StockDrawCount
        self.CheckWinAmount = CheckWinAmount
        self.ColumnNumber = ColumnNumber
        self.MoveCounter = MoveCounter
        self.CardBackUsedNumber = CardBackUsedNumber
#¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

def Sort(CardList):
    MergeList = CardList#Assigns the CardList to the MergeList
    if len(MergeList) > 1:
        Mid = len(MergeList) // 2#Splits the list in two until each list sublist has a length of 1 (integer division)
        LeftHalf = MergeList[:Mid]#Left and right halves of mergelist into the halves
        RightHalf = MergeList[Mid:]
        Sort(LeftHalf)#Recursion
        Sort(RightHalf)
        a = 0#Resets values
        b = 0
        c = 0
        while a < len(LeftHalf) and b < len(RightHalf):#Sees if the x coordinate is larger
            if LeftHalf[a][1] < RightHalf[b][1]:
                MergeList[c] = LeftHalf[a]#Adds the left item to the mergelist
                a +=1#read the next value from the leftlist

            elif LeftHalf[a][1] == RightHalf[b][1]:#Checks if the x coordinate is the same
                if LeftHalf[a][2] < RightHalf[b][2]:#Looks at the y coordinate
                    MergeList[c] = LeftHalf[a]#Adds the left item to the mergelist
                    a +=1#read the next value from the leftlist
                else:
                    MergeList[c] = RightHalf[b]#Adds the right item to the mergelist
                    b +=1#read the next value from the rightlist
            else:
                MergeList[c] = RightHalf[b]##Adds the right item to the mergelist
                b +=1#read the next value from the rightlist
            c +=1
        while a < len(LeftHalf):#check if the left half has elements that have not merged
            MergeList[c] = LeftHalf[a]#add to the mergelist
            a +=1
            c +=1
        while b < len(RightHalf):#check if the right half has elements that have not merged
            MergeList[c] = RightHalf[b]#add to the mergelist
            b +=1
            c +=1
    GetMergeList = MergeList
    return(GetMergeList)


Hello1 = SaveGame(Hello.CardList,Hello.BlankSpaceList,Hello.FullCardList,Hello.UnturnedCount,Hello.UnturnedFinalCount,Hello.CardBackList,Hello.CurrentList,Hello.StockDrawCount,Hello.CheckWinAmount,Hello.ColumnNumber,Hello.MoveCounter,Hello.CardBackUsedNumber)

    
#_____________________________________________________________________________________
if __name__ == "__main__":
    DISPLAYSURF = pygame.display.set_mode((1300, 700), 0, 32)#Sets the window size
    pygame.display.set_caption('Harvey Spider Solitaire')
    Hello.DisplayMenu()      
#¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
