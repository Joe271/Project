## Poker

import random
import pygame
import sys
import time
import statistics
from pygame.locals import *

pygame.init()
pygame.font.init()

class Colours():
    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    blue = pygame.Color(0, 75, 255)
    grey = pygame.Color(83, 83, 83)
    lightGrey = pygame.Color(200, 200, 200)

class Cards():
    def __init__(self):
        self.getCardList()

    def getCardList(self):
        self.backOfCard = pygame.image.load("BackOfCard.JPG")
        self.backOfCard = pygame.transform.scale(self.backOfCard, (71, 108))
        self.number = 0
        self.cardList = []
        for number in range(13):
            if number == 0:
                self.cardList.append([13, "C", "C"+str(number+1)+".JPG"]) # Changed order from F, S, V to V, S, F
            else:
                self.cardList.append([number, "C" , "C"+str(number+1)+".JPG"])
        for number in range(13):
            if number == 0:
                self.cardList.append([13, "D", "D"+str(number+1)+".JPG"])
            else:
                self.cardList.append([number, "D", "D"+str(number+1)+".JPG"])
        for number in range(13):
            if number == 0:
                self.cardList.append([13, "H", "H"+str(number+1)+".JPG"])
            else:
                self.cardList.append([number, "H", "H"+str(number+1)+".JPG"])
        for number in range(13):
            if number == 0:
                self.cardList.append([13, "S", "S"+str(number+1)+".JPG"])
            else:
                self.cardList.append([number, "S", "S"+str(number+1)+".JPG"])

class Dealer():
    def __init__(self):
        self.getDealerCards()

    def getDealerCards(self):
        self.dealerCards = cards.cardList
        self.pot = 0

class Player():
    def __init__(self):
        self.Cards = ["", ""]
        self.Chips = 5000
        self.bet = 0
        self.score = 0
        self.handValue = 0

class User(Player):
    def __init__(self):
        super().__init__()

    def getUserCards(self):
        for i in range (2):
            pick = random.randint(0, game.cardCounter)
            user.Cards[i] = dealer.dealerCards[pick]
            dealer.dealerCards.pop(pick)
            game.cardCounter = game.cardCounter - 1

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.openingBet = 0
        self.maxBet = 0

    def getComputerCards(self):
        for i in range (2):
            pick = random.randint(0, game.cardCounter)
            self.Cards[i] = dealer.dealerCards[pick]
            dealer.dealerCards.pop(pick)
            game.cardCounter = game.cardCounter - 1

    def getOpeningBet(self):
        game.isPair(2)

        if self.Cards[0][0] <= 7 and self.Cards[1][0] <=7:
            self.openingBet = 200

        elif self.Cards[0][0] >= 7 and self.Cards[1][0] >= 7:
            self.openingBet = 300

        elif self.Cards[0][0] <=7 and self.Cards[1][0] >=7 or self.Cards[0][0] >= 7 and self.Cards[1][0] <= 7:
            self.openingBet = 250

        elif game.pair == True and self.Cards[0][0] >= 7:
            self.openingBet = 1500

        elif game.pair == True and self.Cards[0][0] < 6:
            self.openingBet = 750

        elif self.Cards[0][1] == self.Cards[1][1]:
            self.openingBet = 600

        else:
            self.openingBet = 200

        print("computer open",self.openingBet)

    def increaseBet(self):
        pass

    def fold(self):
        pass

    def callandcheck(self):
        pass

    def getMaxBets(self):
        game.getHandValue(self.Cards, 1)

        if game.playerValue[1] < 2:
            self.maxBet1 = 150
        elif game.playerValue[1] < 4:
            self.maxBet1 = 1000
        elif game.playerValue[1] < 6:
            self.maxBet1 = 2000
        elif game.playerValue[1] < 8:
            self.maxBet1 = 3000
        elif game.playerValue[1] < 10:
            self.maxBet1 = 5000

class River():
    def __init__(self):
        self.riverCards = ["", "", "", "", ""]

    def getRiverCards(self):
        for q in range (5):
            pick = random.randint(0, game.cardCounter)
            river.riverCards[q] = dealer.dealerCards[pick]
            game.cardCounter = game.cardCounter - 1
            dealer.dealerCards.pop(pick)

class Assets(): # All assets but cards
    def __init__(self):

        ## Loading all images

        self.back = pygame.image.load("background (2).JPG")
        self.table = pygame.image.load("table (2).fw.PNG")
        self.titleBack = pygame.image.load("titleBack.fw.PNG")
        self.upBet = pygame.image.load("upBet.fw.PNG")
        self.downBet = pygame.image.load("downBet.fw.PNG")
        self.upBetPress = pygame.image.load("upBetPress.fw.PNG")
        self.downBetPress = pygame.image.load("downBetPress.fw.PNG")
        self.menuButton = pygame.image.load("menuButton.fw.PNG")
        self.menuButtonPress = pygame.image.load("menuButtonPress.fw.PNG")
        self.dealerButton = pygame.image.load("dealerButton.PNG")

        ## Defining fonts

        self.compChips = 25
        self.inGameSize = 30
        self.helpSize = 44
        self.menuSize = 50
        self.titleSize = 100

        self.compChipsFont = pygame.font.SysFont("script", self.compChips)
        self.helpFont = pygame.font.Font("freesansbold.ttf", self.helpSize)
        self.inGameFont = pygame.font.SysFont("script", self.inGameSize)
        self.menuFont = pygame.font.SysFont("script", self.menuSize)
        self.titleFont = pygame.font.SysFont("script", self.titleSize)

        ## Creates all text

        self.titleText = self.titleFont.render("Poker", True, (Colours.lightGrey)) # 285 x 101
        self.playText = self.menuFont.render("Play", True, (Colours.black)) # 106 x 51
        self.saveText = self.menuFont.render("Save", True, (Colours.black)) # 121 x 51
        self.loadText = self.menuFont.render("Load", True, (Colours.black)) # 121 x 51
        self.helpText = self.menuFont.render("Help", True, (Colours.black)) # 115 x 51
        self.exitText = self.menuFont.render("Exit", True, (Colours.black)) # 99 x 51
        self.betButtonText = self.inGameFont.render("Bet", True, Colours.black)
        self.callButtonText = self.inGameFont.render("Call", True, Colours.black)
        self.foldButtonText = self.inGameFont.render("Fold", True, Colours.black)
        self.userIncreaseText = self.inGameFont.render("0", True, Colours.black)
        self.userChipsText = self.inGameFont.render(str(user.Chips), True, Colours.black)
        self.computerChipsText = self.inGameFont.render(str(computer.Chips), True, Colours.black)
        self.chipsText = self.inGameFont.render("Chips:", True, Colours.black)
        self.potText = self.inGameFont.render("Pot: 0", True, (Colours.black))
        self.betText = self.inGameFont.render("Bet: 0", True, (Colours.black))
        self.nextButtonText = self.menuFont.render("Next", True, (Colours.black))
        self.backButtonText = self.menuFont.render("Back", True, (Colours.black))
        self.compchipstext = self.compChipsFont.render("Chips: 5000", True, (Colours.black))

class Game():
    def __init__(self):

        self.restart()

    def getCards(self):

        ## Gets cards for each player
        user.getUserCards()
        computer.getComputerCards()
        computer2.getComputerCards()
        computer3.getComputerCards()
        river.getRiverCards()

    def startingAssets(self):

        ## Displays all starting assets
        #The back, table
        self.back = pygame.transform.scale(assets.back, (1280, 720))
        self.table = pygame.transform.scale(assets.table, (980, 420))
        screen.blit(self.back, (0, 0))
        screen.blit(self.table, (150, 150))

        #The 3 user buttons
        self.menuButton = pygame.transform.scale(assets.menuButton, (100, 50))
        screen.blit(self.menuButton, (723, 600)) # Bet button image
        screen.blit(self.menuButton, (723, 660)) # Call button image
        screen.blit(self.menuButton, (833, 600)) # Fold button image
        #pygame.draw.rect(screen, Colours.blue, (723, 600, 100, 50), 0) # Bet button rect
        #pygame.draw.rect(screen, Colours.blue, (723, 660, 100, 50), 0) # Call button rect
        #pygame.draw.rect(screen, Colours.blue, (833, 600, 100, 50), 0) # Fold button rect
        screen.blit(assets.betButtonText,(726, 610)) # Bet button text
        screen.blit(assets.callButtonText,(726, 670)) # Call button text
        screen.blit(assets.foldButtonText,(838, 610)) # Fold button text

        #The 2 bet buttons
        self.upBet = pygame.transform.scale(assets.upBet, self.betButtonScale) # Grey increase bet button
        self.downBet = pygame.transform.scale(assets.downBet, self.betButtonScale) # Grey decrease bet button
        screen.blit(self.upBet, (950, 600))
        screen.blit(self.downBet, (950, 660))

        #The chips
        pygame.draw.rect(screen, Colours.lightGrey, (445, 600, 105, 80), 0) # User chips background
        pygame.draw.rect(screen, Colours.lightGrey, (1015, 635, 80, 40), 0) # User bet increase background

        screen.blit(assets.userIncreaseText, (1020, 640)) # User bet text
        screen.blit(assets.chipsText, (450, 610)) # "Chips:" user
        screen.blit(assets.userChipsText, (450, 640)) # User chips text

        self.computerBetBox = pygame.transform.scale(assets.menuButton, (165, 40))
        #self.potBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 246, 165, 40)) # Pot background
        screen.blit(self.computerBetBox, (557.5, 246)) # "Pot:" Box
        screen.blit(assets.potText, (562.5, 251))

        screen.blit(self.computerBetBox, (557.5, 485)) # "Bet:" Box
        #self.betBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 485, 165, 40)) # Bet background
        screen.blit(assets.betText, (562.5, 490)) # The amount of the bet

        screen.blit(self.computerBetBox, (310.5, 178))
        screen.blit(self.computerBetBox, (557, 178))
        screen.blit(self.computerBetBox, (803.5, 178))
        screen.blit(assets.betText, (315.5, 183))
        screen.blit(assets.betText, (562, 183))
        screen.blit(assets.betText, (808.5, 183))

        screen.blit(help.backPage, (30, 620))
        screen.blit(assets.backButtonText, (65, 625))

        self.blinds()

        pygame.draw.rect(screen, Colours.blue, (0, 359.5, 1280, 1))
        pygame.draw.rect(screen, Colours.blue, (639.5, 0, 1, 720))

        # 3 ai chips
        self.chipsBack = pygame.transform.scale(assets.menuButton, self.chipsScale)
        screen.blit(self.chipsBack, (self.comp1X, 123))
        screen.blit(self.chipsBack, (self.playerCardsX, 123))
        screen.blit(self.chipsBack, (self.comp3X, 123))
        # pygame.draw.rect(screen, Colours.lightGrey, (self.comp1X, 123, 147, 22))
        # pygame.draw.rect(screen, Colours.lightGrey, (self.playerCardsX, 123, 147, 22))
        # pygame.draw.rect(screen, Colours.lightGrey, (self.comp3X, 123, 147, 22))
        screen.blit(assets.compchipstext, (334, 119))
        screen.blit(assets.compchipstext, (581, 119))
        screen.blit(assets.compchipstext, (824, 119))

        pygame.display.update()

    def playGame(self):

        #Gets starting variables and cards for all
        self.restart()
        self.getCards()
        self.startingAssets()

        #Gets the value of the hand of each player, and determines how much AI starts their bet
        self.getHandValue(user.Cards, 0)
        computer.getOpeningBet()
        computer2.getOpeningBet()
        computer3.getOpeningBet()

        print("User cards", user.Cards)
        print("C1 cards  ", computer.Cards)
        print("C2 cards  ", computer2.Cards)
        print("C3 cards  ", computer3.Cards)
        print("River     ", river.riverCards)
        print("Player val", self.playerValue)

        #time.sleep(1)

        for z in range (2): #Displays all 4 player cards
            self.Card = pygame.image.load(user.Cards[z][2])
            self.Card = pygame.transform.scale(self.Card, self.cardScale)
            screen.blit(self.Card, (self.playerCardsX, 600))
            screen.blit(cards.backOfCard, (self.playerCardsX, 10))
            screen.blit(cards.backOfCard, (self.comp1X, 10))
            screen.blit(cards.backOfCard, (self.comp3X, 10))
            self.playerCardsX = self.playerCardsX + 75
            self.comp1X = self.comp1X + 75
            self.comp3X = self.comp3X + 75
            #time.sleep(0.75)
            pygame.display.update()

        self.playerCardsX = 567

        while True:
            self.playerGo()

    def playerGo(self):
        if user.Chips >= 0:
            self.gamePress = pygame.transform.scale(assets.menuButtonPress, (100 ,50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 650:
                            screen.blit(self.gamePress, (723, 600))
                            screen.blit(assets.betButtonText, (726, 610))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(self.menuButton, (723, 600))
                            screen.blit(assets.betButtonText, (726, 610))
                            pygame.display.update()
                            self.makeBet()

                    if pygame.mouse.get_pos()[0] >=723 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710 and self.bet == 0:
                            self.round = self.round + 1
                            if self.round == 3:
                                self.restart()
                            elif self.round <= 2:
                                self.pot = self.pot + user.bet
                                user.bet = 0
                                screen.blit(self.computerBetBox, (557.5, 246))
                                #self.potBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 246, 165, 40)) # Pot background
                                self.potText = assets.inGameFont.render("Pot: " + str(self.pot), True, Colours.black)
                                screen.blit(self.potText, (562.5, 251))
                                screen.blit(self.gamePress, (723, 660))
                                screen.blit(assets.callButtonText, (726, 670))
                                screen.blit(self.computerBetBox, (557.5, 485))
                                #self.betBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 485, 165, 40))
                                screen.blit(assets.betText, (562.5, 490))
                                pygame.display.update()
                                time.sleep(0.2)
                                screen.blit(self.menuButton, (723, 660))
                                screen.blit(assets.callButtonText, (726, 670))
                                pygame.display.update()
                                if self.round <= 0:
                                    self.displayFlop()
                                elif self.round == 1:
                                    self.displayTurn()
                                elif self.round == 2:
                                    self.displayRiver()

                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            user.bet = 0
                            computer.Chips = computer.Chips + self.pot
                            screen.blit(self.gamePress, (833, 600))
                            screen.blit(assets.foldButtonText, (838, 610))
                            screen.blit(self.computerBetBox, (557.5, 485))
                            #self.betBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 485, 165, 40))
                            self.computerChipsText = assets.inGameFont.render(str(computer.Chips), True, Colours.black)
                            screen.blit(assets.betText, (562.5, 490))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(self.menuButton, (833, 600))
                            screen.blit(assets.foldButtonText, (838, 610))
                            pygame.display.update()
                            computer.Chips = computer.Chips + self.pot
                            if user.Chips == 0:
                                user.Chips = -1
                            self.restart()
                            self.playGame()

                    if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(help.backPagePress, (30, 620))
                            screen.blit(assets.backButtonText, (65, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            self.round = -1
                            menu.displayMenu()

        elif user.Chips < 0:
            self.lose()

    def lose(self):
        screen.blit(self.back, (0, 0))

        pygame.display.update()

    def displayFlop(self):
        while self.flopX > 600:
            for i in range(3):
                self.flopCards = pygame.image.load(river.riverCards[i][2])
                self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
                screen.blit(self.flopCards, (self.flopX, 306))
                self.flopX = self.flopX - 125
                time.sleep(0.5)
                pygame.display.update()

    def displayTurn(self):
        self.turnCard = pygame.image.load(river.riverCards[3][2])
        self.turnCard = pygame.transform.scale(self.turnCard, self.cardScale)
        screen.blit(self.turnCard, (475, 306))
        time.sleep(0.5)
        pygame.display.update()

    def displayRiver(self):
        self.riverCard = pygame.image.load(river.riverCards[4][2])
        self.riverCard = pygame.transform.scale(self.riverCard, self.cardScale)
        screen.blit(self.riverCard, (350, 306))
        time.sleep(0.5)
        pygame.display.update()

    def makeBet(self):
        self.betting = True
        while self.betting:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 650:
                            if user.Chips > 0:
                                pygame.draw.rect(screen, Colours.lightGrey, (1015, 635, 80, 40), 0) # Rect over the top of the increase to cover old text
                                pygame.draw.rect(screen, Colours.lightGrey, (445, 640, 105, 40), 0) # Rect over users chips to update the text
                                self.bet = self.bet + 50
                                user.Chips = user.Chips - 50
                                self.userIncreaseText = assets.inGameFont.render(str(self.bet), True, Colours.black) # The text that goes over increase rect
                                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black) # Text over the new users number of chips
                                screen.blit(self.userIncreaseText, (1020, 640)) # Displays the new increase over the top
                                screen.blit(self.userChipsText, (450, 640)) # Displays the new user chips
                                self.upBetPress = pygame.transform.scale(assets.upBetPress, self.betButtonScale) # The orange increase button
                                screen.blit(self.upBetPress, (950, 600))
                                pygame.display.update()
                                time.sleep(0.12)
                                screen.blit(self.upBet, (950, 600)) # Back to grey button
                                pygame.display.update()

                            else:
                                user.Chips = 0

                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 7100:
                            if user.Chips < 5000:
                                if self.bet > 0:
                                    pygame.draw.rect(screen, Colours.lightGrey, (1015, 635, 80, 40), 0)
                                    pygame.draw.rect(screen, Colours.lightGrey, (445, 640, 105, 40), 0)
                                    self.bet = self.bet - 50
                                    user.Chips = user.Chips + 50
                                    self.userIncreaseText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                    self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                                    screen.blit(self.userIncreaseText,(1020, 640))
                                    screen.blit(self.userChipsText,(450, 640))
                                    self.downBetPress = pygame.transform.scale(assets.downBetPress, self.betButtonScale)
                                    screen.blit(self.downBetPress, (950, 660))
                                    pygame.display.update()
                                    time.sleep(0.12)
                                    screen.blit(self.downBet,(950, 660))
                                    pygame.display.update()

                    if pygame.mouse.get_pos()[0] >=1015 and pygame.mouse.get_pos()[1] >= 635:
                        if pygame.mouse.get_pos()[0] <= 1095 and pygame.mouse.get_pos()[1] <= 670:
                            if self.bet >= 0:
                                user.bet = user.bet + self.bet
                                self.bet = 0
                                screen.blit(self.computerBetBox, (557.5, 485))
                                #self.betBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 485, 165, 40))
                                self.betText = assets.inGameFont.render("Bet: "+str(user.bet), True, (Colours.black))
                                screen.blit(self.betText,(562.5, 490))
                                pygame.draw.rect(screen, Colours.lightGrey, (1015, 635, 80, 40), 0)
                                self.userIncreaseText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                screen.blit(self.userIncreaseText,(1020, 640))
                                pygame.display.update()
                                self.betting = False
                                return self.bet

                            else:
                                pass

    def blinds(self):
        if user.Chips > 0:
            if self.userDealerButton == True:
                user.bet = user.bet + self.smallBlind
                user.Chips = user.Chips - self.smallBlind
                pygame.draw.rect(screen, Colours.lightGrey, (595, 485, 80, 40), 0)
                pygame.draw.rect(screen, Colours.lightGrey, (445, 640, 105, 40), 0)
                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                self.userBlindText = assets.inGameFont.render("Bet: "+str(user.bet), True, (Colours.black))
                screen.blit(self.userChipsText, (450, 640))
                screen.blit(self.userBlindText, (562.5, 490))
                self.userDealerButton = False
                return user.bet

            elif self.userDealerButton == False:
                user.bet = user.bet + self.bigBlind
                user.Chips = user.Chips - self.bigBlind
                pygame.draw.rect(screen, Colours.lightGrey, (595, 485, 80, 40), 0)
                pygame.draw.rect(screen, Colours.lightGrey, (445, 640, 105, 40), 0)
                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                self.userBlindText = assets.inGameFont.render("Bet: "+str(user.bet), True, (Colours.black))
                screen.blit(self.userChipsText, (450, 640))
                screen.blit(self.userBlindText, (562.5, 490))
                self.userDealerButton = True
                return user.bet

    def restart(self):

        ## Variables
        self.playerTurn = True
        self.userDealerButton = True
        self.dealerButtonLocation = 0
        self.ThreeOak = False
        self.Straight = False
        self.Flush = False
        self.pair = False
        self.suitList = []
        self.valueList = []
        self.userHand = []
        self.cardCounter = 51
        self.bet = 0
        self.playerCardsX = 567
        self.comp1X = 320
        self.comp3X = 810
        self.flopX = 850
        self.chipsScale = (147, 22)
        self.cardScale = (71, 108)
        self.betButtonScale = (50, 50)
        self.bigBlind = 100
        self.smallBlind = 50
        self.pot = 0
        self.round = -1
        self.hands = 0
        self.totalValue = 0
        self.noOfPair = 0
        self.playerValue = [0, 0, 0, 0]

        cards.getCardList()
        dealer.getDealerCards()

    def getHandValue(self, playerCards, playerValPos):
        self.userHand.extend(playerCards)
        self.riverCards = river.riverCards
        self.userHand.extend(river.riverCards)

        for x in range(7):
            self.suitList.append(self.userHand[x][1])
            self.valueList.append(self.userHand[x][0])

        self.valueList.sort()
        self.userHand.sort()
        self.bestHandValues = self.valueList[2:]
        self.totBestHand = sum(self.bestHandValues)

        self.isPair(playerValPos)
        self.isTwoPair(playerValPos)
        self.isThreeOak(playerValPos)
        self.isStraight(playerValPos)
        self.isFlush(playerValPos)
        self.isFullHouse(playerValPos)
        self.isFourOak(playerValPos)
        self.isStraightFlush(playerValPos)
        self.isRoyalFlush(playerValPos)

        if self.playerValue[playerValPos] == 0:
            self.highCard = self.valueList[-1]
            self.playerValue[playerValPos] = 1

        self.ThreeOak = False
        self.Straight = False
        self.Flush = False
        self.pair = False
        self.suitList = []
        self.valueList = []
        self.userHand = []
        self.totalValue = 0
        self.noOfPair = 0

    def isRoyalFlush(self, playerValPos):
        if self.suitList.count("C") == 5 and self.totBestHand == 55 or self.suitList.count("D") == 5 and self.totBestHand == 55 or self.suitList.count("H") == 5 and self.totBestHand == 55 or self.suitList.count("S") == 5 and self.totBestHand == 55:
            self.playerValue[playerValPos] = 10
            return

    def isStraightFlush(self, playerValPos):
        if self.Straight == True and self.Flush == True:
            self.playerValue[playerValPos] = 9
            return

    def isFourOak(self, playerValPos):
        for x in range (1, 14):
            if self.valueList.count(x) == 4:
                self.playerValue[playerValPos] = 8
                return

    def isFullHouse(self, playerValPos):
        if self.ThreeOak == True and self.pair == True:
            self.playerValue[playerValPos] = 7
            return

    def isFlush(self, playerValPos):
        if self.suitList.count("C") >= 5 or self.suitList.count("D") >= 5 or self.suitList.count("H") >= 5 or self.suitList.count("S") >= 5:
            self.playerValue[playerValPos] = 6
            self.Flush = True
            return

    def isStraight(self, playerValPos):
        for i in range (len(self.valueList)):
            if self.valueList[i] - self.valueList[i-1] == 1 and self.valueList[i-1] - self.valueList[i-2] == 1 and self.valueList[i-2] - self.valueList[i-3] == 1 and self.valueList[i-3] - self.valueList[i-4] == 1:
                self.playerValue[playerValPos] = 5
                self.Straight = True
                return

    def isThreeOak(self, playerValPos):
        for x in range (1, 14):
            if self.valueList.count(x) == 3:
                self.playerValue[playerValPos] = 4
                for y in range(3):
                    self.valueList.remove(x)
                self.ThreeOak = True
                return

    def isTwoPair(self, playerValPos):
        if self.pair == True:
            for x in range(1, 14):
                if self.valueList.count(x) == 2:
                    self.playerValue[playerValPos] = 3
                    self.valueList.remove(x)
                    return

    def isPair(self, playerValPos):
        for x in range(1, 14):
            if self.valueList.count(x) == 2:
                self.playerValue[playerValPos] = 2
                self.valueList.remove(x)
                self.pair = True
                return

class Help():
    def __init__(self):
        self.back = pygame.transform.scale(assets.back, (1280, 720))

        self.helpPage1 = assets.helpFont.render("How to play", True, Colours.white) # 249 x 45
        self.helpPage2 = assets.helpFont.render("How to win", True, Colours.white) # 235 x 45
        self.helpPage3 = assets.helpFont.render("Possible hands", True, Colours.white) # 332 x 45

        self.help1 = assets.helpFont.render("To make a bet click the bet button, then use the arrows to", True, Colours.white)
        self.help2 = assets.helpFont.render("increase or decrease your bet, when you want to make the", True, Colours.white)
        self.help3 = assets.helpFont.render("bet click the box that your bet is in, if you do not wish", True, Colours.white)
        self.help4 = assets.helpFont.render("to make a bet and the opponent has not  made a bet click", True, Colours.white)
        self.help5 = assets.helpFont.render("the check/call button and the next cards in the river will", True, Colours.white)
        self.help6 = assets.helpFont.render("be displayed. At the start of each hand there are blinds", True, Colours.white)
        self.help7 = assets.helpFont.render("which is a forced bet that both players have to bet, this", True, Colours.white)
        self.help8 = assets.helpFont.render("is default to 100 chips however you can change this to be", True, Colours.white)
        self.help9 = assets.helpFont.render("higher or lower in multiples of 50.", True, Colours.white)

        self.help12 = assets.helpFont.render("To win get all of your opponents chips by betting your", True, Colours.white)
        self.help13 = assets.helpFont.render("own chips with theirs when you think you have a better", True, Colours.white)
        self.help14 = assets.helpFont.render("hand. E.g. if you only have one pair you may not want to", True, Colours.white)
        self.help15 = assets.helpFont.render("bet as much as if you had a flush or straight.", True, Colours.white)

        self.help16 = assets.inGameFont.render("Pair:", True, Colours.white)
        self.help17 = assets.inGameFont.render("Two Pair:", True, Colours.white)
        self.help18 = assets.inGameFont.render("Three of a kind:", True, Colours.white)
        self.help19 = assets.inGameFont.render("Straight:", True, Colours.white)
        self.help20 = assets.inGameFont.render("Flush:", True, Colours.white)
        self.help21 = assets.inGameFont.render("Full House:", True, Colours.white)
        self.help22 = assets.inGameFont.render("Four of a kind:", True, Colours.white)
        self.help23 = assets.inGameFont.render("Straight Flush:", True, Colours.white)
        self.help24 = assets.inGameFont.render("Royal Flush:", True, Colours.white)

        self.nextPage = pygame.transform.scale(assets.menuButton, (175, 75))
        self.backPage = self.nextPage
        self.nextPagePress = pygame.transform.scale(assets.menuButtonPress, (175, 75))
        self.backPagePress = self.nextPagePress

    def page1(self):
        screen.blit(self.back, (0, 0))
        screen.blit(self.helpPage1, (515.5, 15))
        screen.blit(self.help1, (20, 100))
        screen.blit(self.help2, (20, 150))
        screen.blit(self.help3, (20, 200))
        screen.blit(self.help4, (20, 250))
        screen.blit(self.help5, (20, 300))
        screen.blit(self.help6, (20, 350))
        screen.blit(self.help7, (20, 400))
        screen.blit(self.help8, (20, 450))
        screen.blit(self.help9, (20, 500))
        screen.blit(self.nextPage, (1075, 620))
        screen.blit(assets.nextButtonText, (1110, 625))
        screen.blit(self.backPage, (30, 620))
        screen.blit(assets.backButtonText, (65, 625))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 1075 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 1250 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(self.nextPagePress, (1075, 620))
                            screen.blit(assets.nextButtonText, (1110, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            self.page2()

                    if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(self.backPagePress, (30, 620))
                            screen.blit(assets.backButtonText, (65, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            menu.displayMenu()

    def page2(self):
        screen.blit(self.back, (0, 0))
        screen.blit(self.helpPage2, (522.5, 15))
        screen.blit(self.help12, (20, 100))
        screen.blit(self.help13, (20, 150))
        screen.blit(self.help14, (20, 200))
        screen.blit(self.help15, (20, 250))

        screen.blit(self.nextPage, (1075, 620))
        screen.blit(self.backPage, (30, 620))
        screen.blit(assets.nextButtonText, (1110, 625))
        screen.blit(assets.backButtonText, (65, 625))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 1075 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 1250 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(self.nextPagePress, (1075, 620))
                            screen.blit(assets.nextButtonText, (1110, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            self.page3()

                    if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(self.backPagePress, (30, 620))
                            screen.blit(assets.backButtonText, (65, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            self.page1()

    def page3(self):
        screen.blit(self.back, (0, 0))
        screen.blit(self.helpPage3, (474, 15))

        screen.blit(self.backPage, (30, 620))
        screen.blit(assets.backButtonText, (65, 625))

        screen.blit(self.help16, (10, 80))
        screen.blit(self.help17, (640, 80))
        screen.blit(self.help18, (10, 188))
        screen.blit(self.help19, (640, 188))
        screen.blit(self.help20, (10, 294))
        screen.blit(self.help21, (640, 294))
        screen.blit(self.help22, (10, 400))
        screen.blit(self.help23, (640, 400))
        screen.blit(self.help24, (10, 506))

        self.pair1 = pygame.image.load("C2.JPG")
        self.pair2 = pygame.image.load("D2.JPG")
        self.pair1 = pygame.transform.scale(self.pair1, (67, 103))
        self.pair2 = pygame.transform.scale(self.pair2, (67, 103))
        self.twoPair1 = pygame.image.load("S5.JPG")
        self.twoPair2 = pygame.image.load("H5.JPG")
        self.twoPair1 = pygame.transform.scale(self.twoPair1, (67, 103))
        self.twoPair2 = pygame.transform.scale(self.twoPair2, (67, 103))
        self.threeOAK = pygame.image.load("H2.JPG")
        self.threeOAK = pygame.transform.scale(self.threeOAK, (67,103))
        self.straight1 = pygame.image.load("H3.JPG")
        self.straight2 = pygame.image.load("D4.JPG")
        self.straight3 = pygame.image.load("C6.JPG")
        self.straight1 = pygame.transform.scale(self.straight1, (67, 103))
        self.straight2 = pygame.transform.scale(self.straight2, (67, 103))
        self.straight3 = pygame.transform.scale(self.straight3, (67, 103))
        self.flush1 = pygame.image.load("H8.JPG")
        self.flush2 = pygame.image.load("H13.JPG")
        self.flush1 = pygame.transform.scale(self.flush1, (67, 103))
        self.flush2 = pygame.transform.scale(self.flush2, (67, 103))
        self.fourOAK = pygame.image.load("S2.JPG")
        self.fourOAK = pygame.transform.scale(self.fourOAK, (67, 103))
        self.straightF1 = pygame.image.load("H4.JPG")
        self.straightF2 = pygame.image.load("H6.JPG")
        self.straightF1 = pygame.transform.scale(self.straightF1, (67, 103))
        self.straightF2 = pygame.transform.scale(self.straightF2, (67, 103))
        self.royalF1 = pygame.image.load("H10.JPG")
        self.royalF2 = pygame.image.load("H11.JPG")
        self.royalF3 = pygame.image.load("H12.JPG")
        self.royalF4 = pygame.image.load("H1.JPG")
        self.royalF1 = pygame.transform.scale(self.royalF1, (67, 103))
        self.royalF2 = pygame.transform.scale(self.royalF2, (67, 103))
        self.royalF3 = pygame.transform.scale(self.royalF3, (67, 103))
        self.royalF4 = pygame.transform.scale(self.royalF4, (67, 103))

        screen.blit(self.pair1, (230, 80))
        screen.blit(self.pair2, (300, 80))

        screen.blit(self.pair1, (860, 80))
        screen.blit(self.pair2, (930, 80))
        screen.blit(self.twoPair1, (1000, 80))
        screen.blit(self.twoPair2, (1070, 80))

        screen.blit(self.pair1, (230, 188))
        screen.blit(self.pair2, (300, 188))
        screen.blit(self.threeOAK, (370, 188))

        screen.blit(self.pair1, (860, 188))
        screen.blit(self.straight1, (930, 188))
        screen.blit(self.straight2, (1000, 188))
        screen.blit(self.twoPair1, (1070, 188))
        screen.blit(self.straight3, (1140, 188))

        screen.blit(self.threeOAK, (230, 294))
        screen.blit(self.straight1, (300, 294))
        screen.blit(self.twoPair2, (370, 294))
        screen.blit(self.flush1, (440, 294))
        screen.blit(self.flush2, (510, 294))

        screen.blit(self.pair1, (860, 294))
        screen.blit(self.pair2, (930, 294))
        screen.blit(self.threeOAK, (1000, 294))
        screen.blit(self.twoPair1, (1070, 294))
        screen.blit(self.twoPair2, (1140, 294))

        screen.blit(self.pair1, (230, 400))
        screen.blit(self.pair2, (300, 400))
        screen.blit(self.threeOAK, (370, 400))
        screen.blit(self.fourOAK, (440, 400))

        screen.blit(self.threeOAK, (860, 400))
        screen.blit(self.straight1, (930, 400))
        screen.blit(self.straightF1, (1000, 400))
        screen.blit(self.twoPair2, (1070, 400))
        screen.blit(self.straightF2, (1140, 400))

        screen.blit(self.royalF1, (230, 506))
        screen.blit(self.royalF2, (300, 506))
        screen.blit(self.royalF3, (370, 506))
        screen.blit(self.flush2, (440, 506))
        screen.blit(self.royalF4, (510, 506))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(self.backPagePress, (30, 620))
                            screen.blit(assets.backButtonText, (65, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            self.page2()

class Menu():
    def displayMenu(self):

        self.back = pygame.transform.scale(assets.back, (1280, 720))
        screen.blit(self.back,(0, 0))

        self.titleBack = pygame.transform.scale(assets.titleBack, (750, 120))
        screen.blit(self.titleBack, (265, 10))

        screen.blit(assets.titleText,(543.5, 10)) # 193 x 69

        assets.menuButton = pygame.transform.scale(assets.menuButton, (500, 80))
        assets.menuButtonPress = pygame.transform.scale(assets.menuButtonPress, (500, 80))

        screen.blit(assets.menuButton, (390, 185.5))
        screen.blit(assets.menuButton, (390, 285.5))
        screen.blit(assets.menuButton, (390, 385.5))
        screen.blit(assets.menuButton, (390, 485.5))
        screen.blit(assets.menuButton, (390, 585.5))
        screen.blit(assets.playText, (587, 190))
        screen.blit(assets.saveText, (579.5, 290))
        screen.blit(assets.loadText, (579.5, 390))
        screen.blit(assets.helpText, (582.5, 490))
        screen.blit(assets.exitText, (590.5, 590))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 390 and pygame.mouse.get_pos()[0] <= 890:
                        if pygame.mouse.get_pos()[1] >= 185.5 and pygame.mouse.get_pos()[1] <= 265.5:
                            screen.blit(assets.menuButtonPress, (390, 185.5))
                            screen.blit(assets.playText, (587, 200))
                            pygame.display.update()
                            time.sleep(0.2)
                            game.playGame()

                        if pygame.mouse.get_pos()[1] >= 285.5 and pygame.mouse.get_pos()[1] <= 365.5:
                            print("2")

                        if pygame.mouse.get_pos()[1] >= 385.5 and pygame.mouse.get_pos()[1] <= 465.5:
                            print("3")

                        if pygame.mouse.get_pos()[1] >= 485.5 and pygame.mouse.get_pos()[1] <= 565.5:
                            screen.blit(assets.menuButtonPress, (390, 485.5))
                            screen.blit(assets.helpText, (582.5, 500))
                            pygame.display.update()
                            time.sleep(0.2)
                            help.page1()

                        if pygame.mouse.get_pos()[1] >= 585.5 and pygame.mouse.get_pos()[1] <= 665.5:
                            screen.blit(assets.menuButtonPress, (390, 585.5))
                            screen.blit(assets.exitText, (590.5, 600))
                            pygame.display.update()
                            time.sleep(0.2)
                            pygame.quit()
                            sys.exit()

# Instantiates classes
cards = Cards()
dealer = Dealer()
player = Player()
user = User()
computer = Computer()
computer2 = Computer()
computer3 = Computer()
river = River()
assets = Assets()
game = Game()
help = Help()
menu = Menu()

if __name__ == "__main__":
    screenwidth = 1280
    screenheight = 720
    framerate = 60
    clock = pygame.time.Clock()
    screenSize = ((screenwidth, screenheight))
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Poker")
    menu.displayMenu()
