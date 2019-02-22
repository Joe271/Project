# Poker

import random
import pygame
import sys
import time
from pygame.locals import *

pygame.init()
pygame.font.init()


class Colours:
    _white = pygame.Color(255, 255, 255)
    _black = pygame.Color(0, 0, 0)
    _blue = pygame.Color(0, 75, 255)
    _grey = pygame.Color(83, 83, 83)
    _lightGrey = pygame.Color(200, 200, 200)


class Cards():
    def __init__(self):
        self.getCardList() # calls function getCardList

    def getCardList(self): # appends all of the cards with their: value, suit and file name
        self.backOfCard = pygame.image.load("BackOfCard.JPG") # loads the back of the card image
        self.backOfCard = pygame.transform.scale(self.backOfCard, (71, 108)) # changes the size to be 71, 108 the size of the cards on the table
        self.cardList = [] # creates empty list cardList which will store the cards
        for number in range(13): # loops through the cardList construction
            if number == 0: # for the first item (ace) the value is the highest but the number on the card is lowest
                self.cardList.append([13, "C", "C"+str(number+1)+".JPG"]) # Changed order from F, S, V to V, S, F
            else: # adds the rest of the suit (2-K)to the cardList
                self.cardList.append([number, "C" , "C"+str(number+1)+".JPG"])
        for number in range(13): # runs 4 times to add each suit
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

    def getDealerCards(self): # creates a new list so the original list of cards is preserved
        self.dealerCards = cards.cardList
        self.pot = 0

class Player():
    def __init__(self):
        self.Cards = ["", ""] # the standard list for the 2 cards a player has
        self.Chips = 5000 # the starting amount of chips for a player
        self.bet = 0 # all bets start at 0
        self.score = 0 # ?
        self.handValue = 0 # this is the rank of hand i.e. high card = 1 royal flush = 10
        self.locationList = {0: "user", 1: "computer1", 2: "computer2", 3: "computer3"} # dictionary for all of the locations of each player in the hand starting from the user going clockwise

class User(Player):
    def __init__(self):
        super().__init__()
        self.increaseBet = 0 # this is how much the user is going to increase their bet by and is displayed in the bottom left

    def getUserCards(self):
        for i in range (2): # runs twice for 2 cards
            pick = random.randint(0, game.cardCounter) # picks a random number to select the card
            user.Cards[i] = dealer.dealerCards[pick] # the selected card is put in index i in their Cards
            dealer.dealerCards.pop(pick) # removes this selected card from the dealer list so 2 players can not have the same cards
            game.cardCounter = game.cardCounter - 1 # reduces the counter by the number of cards chosen so there are no index errors

    def userTurn(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: # checks if the game is being exited
                    pygame.quit() # closes pygame so the window can be shut
                    sys.exit() # closes the window
                # Bet button
                if event.type == pygame.MOUSEBUTTONDOWN: # if a click is detected
                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 600: # if the mouse x is greater than 723 and the y is greater than 600
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 650: # if the mouse x is less than 823 and y is less than 650
                            screen.blit(assets.gamePress, (723, 600)) # display the pressed button
                            screen.blit(assets.betButtonText, (726, 610)) # display the text over the top of that
                            pygame.display.update() # update the screen for new changes
                            time.sleep(0.2) # wait 0.2s so there is a visible change in the button
                            screen.blit(assets.userButton, (723, 600)) # returns the buttons to its original look
                            screen.blit(assets.betButtonText, (726, 610)) # ^^
                            pygame.display.update()
                            self.makeBet() # calls the function that allows the user to increase their bet

                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 660:  # Call button
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710 and self.bet == 0:
                            screen.blit(assets.gamePress, (723, 660))
                            screen.blit(assets.callButtonText, (726, 670))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(assets.userButton, (723, 660))
                            screen.blit(assets.callButtonText, (726, 670))
                            pygame.display.update()
                            # this button will allow the user to match the previous bet as this is the minimum they have to bet without folding
                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600: # Fold button
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            screen.blit(assets.gamePress, (833, 600))
                            screen.blit(assets.foldButtonText, (838, 610))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(assets.userButton, (833, 600))
                            screen.blit(assets.foldButtonText, (838, 610))
                            pygame.display.update()
                            # this will allow the user to get out of the round if they think that they cannot win
    def makeBet(self): # the function allowing the user to increase their bet
        self.betting = True
        while self.betting:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 600:  # Increase bet button
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 650:
                            if user.Chips > 0: # checks that the user has chips to bet
                                pygame.draw.rect(screen, Colours._lightGrey, (1015, 635, 80, 40), 0)  # Rect over the top of the increase to cover old text
                                pygame.draw.rect(screen, Colours._lightGrey, (445, 640, 105, 40), 0)  # Rect over users chips to update the text
                                self.increaseBet = self.increaseBet + 50 # increases the bet by 50 as this is the increment cause by the button press
                                self.Chips = self.Chips - 50 # takes these chips out of the users bank as they would not gave them
                                self.userIncreaseText = assets.inGameFont.render(str(self.increaseBet), True, Colours._black)  # The text that goes over increase rect
                                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours._black)  # Text over the new users number of chips
                                screen.blit(self.userIncreaseText, (1020, 640))  # Displays the new increase over the top
                                screen.blit(self.userChipsText, (450, 640))  # Displays the new user chips
                                screen.blit(assets.upBetPress, (950, 600))
                                pygame.display.update()
                                time.sleep(0.12)
                                screen.blit(assets.upBet, (950, 600))  # Back to grey button
                                pygame.display.update()

                            else: # if the user does not have enough chips to bet this will stop then getting negative chips
                                user.Chips = 0

                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 660:  # Decrease bet button
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 710:
                            if self.increaseBet > 0:
                                pygame.draw.rect(screen, Colours._lightGrey, (1015, 635, 80, 40), 0)
                                pygame.draw.rect(screen, Colours._lightGrey, (445, 640, 105, 40), 0)
                                self.increaseBet = self.increaseBet - 50 # same as the previous section but reversed
                                user.Chips = user.Chips + 50 # adds the chips taken from the increase and returned to bank
                                self.userIncreaseText = assets.inGameFont.render(str(self.increaseBet), True, Colours._black)
                                self.userChipsText = assets.inGameFont.render(str(self.Chips), True, Colours._black)
                                screen.blit(self.userIncreaseText, (1020, 640))
                                screen.blit(self.userChipsText, (450, 640))
                                screen.blit(assets.downBetPress, (950, 660))
                                pygame.display.update()
                                time.sleep(0.12)
                                screen.blit(assets.downBet, (950, 660))
                                pygame.display.update()

                    if pygame.mouse.get_pos()[0] >= 1015 and pygame.mouse.get_pos()[1] >= 635:  # Add increase to total bet
                        if pygame.mouse.get_pos()[0] <= 1095 and pygame.mouse.get_pos()[1] <= 670:
                            self.bet = self.bet + self.increaseBet
                            self.increaseBet = 0
                            screen.blit(assets.computerBetBox, (557.5, 485))
                            # self.betBox = pygame.draw.rect(screen, Colours.lightGrey, (557.5, 485, 165, 40))
                            self.betText = assets.inGameFont.render("Bet: " + str(user.bet), True, (Colours._black))
                            screen.blit(self.betText, (562.5, 490))
                            pygame.draw.rect(screen, Colours._lightGrey, (1015, 635, 80, 40), 0)
                            self.userIncreaseText = assets.inGameFont.render(str(self.increaseBet), True, Colours._black)
                            screen.blit(self.userIncreaseText, (1020, 640))
                            pygame.display.update()
                            self.betting = False
                            game.previousBet = self.bet
                            # if the user clicks the number to increase this amount will be added to their bet and then the next player will have their turn

class Computer(Player):
    def __init__(self, locPos):
        super().__init__()
        self.openingBet = 0 # how much preflop bet
        self.maxBet = 0 # max bet after river
        self.currentBet = 0 # the amount they currently have in their bet
        self.location = self.locationList[locPos]

    def getComputerCards(self):
        for i in range(2): # picks their 2 cards (see user.getUserCards())
            pick = random.randint(0, game.cardCounter)
            self.Cards[i] = dealer.dealerCards[pick]
            dealer.dealerCards.pop(pick)
            game.cardCounter = game.cardCounter - 1

    def nextTurn(self):
        if game.previousBet <= self.maxBet:
            self.call()
        elif game.previousBet == 0:
            self.check()

    def call(self):
        self.currentBet = game.previousBet
        game.updateComputersChips()

    def check(self):
        pass

    def computerBet(self):
        pass


class River():
    def __init__(self):
        self.riverCards = ["", "", "", "", ""]

    def getRiverCards(self):
        for card in range (5):
            pick = random.randint(0, game.cardCounter)
            river.riverCards[card] = dealer.dealerCards[pick]
            game.cardCounter = game.cardCounter - 1
            dealer.dealerCards.pop(pick)

class Assets(): # All assets but cards
    def __init__(self):

        ## Image scales
        self.chipsScale = (147, 22)
        self.cardScale = (71, 108)
        self.betButtonScale = (50, 50)

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
        self.dealerButton = pygame.image.load("dealerButton.fw.PNG")

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

        self.titleText = self.titleFont.render("Poker", True, (Colours._lightGrey)) # 285 x 101
        self.playText = self.menuFont.render("Play", True, (Colours._black)) # 106 x 51
        self.saveText = self.menuFont.render("Save", True, (Colours._black)) # 121 x 51
        self.loadText = self.menuFont.render("Load", True, (Colours._black)) # 121 x 51
        self.helpText = self.menuFont.render("Help", True, (Colours._black)) # 115 x 51
        self.exitText = self.menuFont.render("Exit", True, (Colours._black)) # 99 x 51
        self.betButtonText = self.inGameFont.render("Bet", True, Colours._black)
        self.callButtonText = self.inGameFont.render("Call", True, Colours._black)
        self.foldButtonText = self.inGameFont.render("Fold", True, Colours._black)
        self.chipsText = self.inGameFont.render("Chips:", True, Colours._black)
        self.nextButtonText = self.menuFont.render("Next", True, (Colours._black))
        self.backButtonText = self.menuFont.render("Back", True, (Colours._black))
        #self.compChipsText = self.compChipsFont.render("Chips:", True, Colours._black)

        self.back = pygame.transform.scale(self.back, (1280, 720))
        self.table = pygame.transform.scale(self.table, (980, 420))
        self.gamePress = pygame.transform.scale(self.menuButtonPress, (100, 50))
        self.userButton = pygame.transform.scale(self.menuButton, (100, 50))
        self.upBetPress = pygame.transform.scale(self.upBetPress, self.betButtonScale)  # The orange increase button
        self.upBet = pygame.transform.scale(self.upBet, self.betButtonScale) # Grey increase bet button
        self.downBet = pygame.transform.scale(self.downBet, self.betButtonScale) # Grey decrease bet button
        self.computerBetBox = pygame.transform.scale(self.menuButton, (165, 40))
        self.chipsBack = pygame.transform.scale(self.menuButton, self.chipsScale)
        self.downBetPress = pygame.transform.scale(self.downBetPress, self.betButtonScale)

    def generateNumber(self):## Creates all text that is a number

        self.userIncreaseText = self.inGameFont.render(str(user.increaseBet), True, Colours._black)
        self.userBetText = self.inGameFont.render(("Bet: "+ str(user.bet)), True, Colours._black)
        self.userChipsText = self.inGameFont.render(str(user.Chips), True, Colours._black)
        self.computer1ChipsText = self.compChipsFont.render(("Chips: " + str(computer1.Chips)), True, Colours._black)
        self.computer2ChipsText = self.compChipsFont.render(("Chips: " + str(computer2.Chips)), True, Colours._black)
        self.computer3ChipsText = self.compChipsFont.render(("Chips: " + str(computer3.Chips)), True, Colours._black)
        self.computer1BetText = self.inGameFont.render(("Bet: " + str(computer1.bet)), True, Colours._black)
        self.computer2BetText = self.inGameFont.render(("Bet: " + str(computer2.bet)), True, Colours._black)
        self.computer3BetText = self.inGameFont.render(("Bet: " + str(computer3.bet)), True, Colours._black)
        self.potText = self.inGameFont.render(("Pot: "+ str(dealer.pot)), True, (Colours._black))

class Game():
    def __init__(self):

        self.restart()

    def getCards(self):

        ## Gets cards for each player
        user.getUserCards()
        computer1.getComputerCards()
        computer2.getComputerCards()
        computer3.getComputerCards()
        river.getRiverCards()

    def startingAssets(self):

        ## Displays all starting assets
        screen.blit(assets.back, (0, 0))
        screen.blit(assets.table, (150, 150))

        screen.blit(assets.userButton, (723, 600)) # Bet button image
        screen.blit(assets.userButton, (723, 660)) # Call button image
        screen.blit(assets.userButton, (833, 600)) # Fold button image
        screen.blit(assets.betButtonText,(726, 610)) # Bet button text
        screen.blit(assets.callButtonText,(726, 670)) # Call button text
        screen.blit(assets.foldButtonText,(838, 610)) # Fold button text
        screen.blit(assets.upBet, (950, 600))
        screen.blit(assets.downBet, (950, 660))

        self.updateUserChips()
        self.updateComputersChips()
        screen.blit(assets.computerBetBox, (557.5, 246)) # "Pot:" Box
        screen.blit(assets.potText, (562.5, 251))

        screen.blit(help.backPage, (30, 620))
        screen.blit(assets.backButtonText, (65, 625))

        pygame.display.update()

    def displayCards(self):
        for z in range(2):  # Displays all 4 player cards
            self.Card = pygame.image.load(user.Cards[z][2])
            self.Card = pygame.transform.scale(self.Card, assets.cardScale)
            screen.blit(self.Card, (self.playerCardsX, 600))
            screen.blit(cards.backOfCard, (self.playerCardsX, 10))
            screen.blit(cards.backOfCard, (self.comp1X, 10))
            screen.blit(cards.backOfCard, (self.comp3X, 10))
            self.playerCardsX = self.playerCardsX + 75
            self.comp1X = self.comp1X + 75
            self.comp3X = self.comp3X + 75
            # time.sleep(0.75)
            pygame.display.update()

        self.comp1X = 320
        self.comp3X = 810

    def playGame(self):

        self.restart()
        self.getCards()
        self.startingAssets()
        self.displayCards()
        self.playerCardsX = 567
        self.getBlinds()

        for count in range(4):
            while user.bet != computer1.bet or computer1.bet != computer2.bet or computer2.bet != computer3.bet:
                if self.playerTurn == 0:
                    user.userTurn()
                    self.playerTurn = self.playerTurn + 1

                elif self.playerTurn == 1:
                    print(1)
                    # computer1.nextTurn()
                    self.playerTurn = self.playerTurn + 1

                elif self.playerTurn == 2:
                    # computer2.nextTurn()
                    self.playerTurn = self.playerTurn + 1
                    print(2)

                elif self.playerTurn == 3:
                    # computer3.nextTurn()
                    self.playerTurn = 0
                    print(3)

            if count == 1:
                self.displayFlop()

            elif count == 2:
                self.displayTurn()

            elif count == 3:
                self.displayRiver()

    def updateComputersChips(self):
        assets.generateNumber()
        screen.blit(assets.computerBetBox, (310.5, 178))
        screen.blit(assets.computerBetBox, (557, 178))
        screen.blit(assets.computerBetBox, (803.5, 178))
        screen.blit(assets.chipsBack, (self.comp1X, 123))
        screen.blit(assets.chipsBack, (self.playerCardsX, 123))
        screen.blit(assets.chipsBack, (self.comp3X, 123))
        screen.blit(assets.computer1ChipsText, (334, 119))
        screen.blit(assets.computer2ChipsText, (581, 119))
        screen.blit(assets.computer3ChipsText, (824, 119))
        screen.blit(assets.computer1BetText, (315.5, 183))
        screen.blit(assets.computer2BetText, (562, 183))
        screen.blit(assets.computer3BetText, (808.5, 183))
        pygame.display.update()

    def updateUserChips(self):
        assets.generateNumber()
        pygame.draw.rect(screen, Colours._lightGrey, (445, 600, 105, 80), 0) # User total chips background (left)
        pygame.draw.rect(screen, Colours._lightGrey, (1015, 635, 80, 40), 0) # User bet increase background (bottom right)
        screen.blit(assets.computerBetBox, (557.5, 485)) # The background for the bet box, lower central table

        screen.blit(assets.chipsText, (450, 610)) # "Chips:" user left
        screen.blit(assets.userBetText, (562.5, 490)) # "Bet: " bottom middle table 58 x 37


        screen.blit(assets.userIncreaseText, (1020, 640)) # User bet increase text bottom right
        screen.blit(assets.userChipsText, (450, 640)) # User chips value text left

        pygame.display.update()

    def getBlinds(self):
        if self.dealerButtonLocation == 0:
            self.smallBlindFunction(computer1)
            self.bigBlindFunction(computer2)
            self.updateComputersChips()
            self.playerTurn = 3

        elif self.dealerButtonLocation == 1:
            self.smallBlindFunction(computer2)
            self.bigBlindFunction(computer3)
            self.updateComputersChips()
            self.updateUserChips()
            self.playerTurn = 0

        elif self.dealerButtonLocation == 2:
            self.smallBlindFunction(computer3)
            self.bigBlindFunction(user)
            self.updateComputersChips()
            self.updateUserChips()
            self.playerTurn = 1

        elif self.dealerButtonLocation == 3:
            self.smallBlindFunction(user)
            self.bigBlindFunction(computer1)
            self.updateComputersChips()
            self.updateUserChips()
            self.playerTurn = 2

        self.dealerButtonLocation = self.dealerButtonLocation + 1

    def smallBlindFunction(self, smallBlindPlayer):
        smallBlindPlayer.bet = smallBlindPlayer.bet + self.smallBlind
        smallBlindPlayer.Chips = smallBlindPlayer.Chips - self.smallBlind

    def bigBlindFunction(self, bigBlindPlayer):
        bigBlindPlayer.bet = bigBlindPlayer.bet + self.bigBlind
        bigBlindPlayer.Chips = bigBlindPlayer.Chips - self.bigBlind

    def restart(self):

        ## Variables
        self.dealerButtonLocation = 1
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
        self.bigBlind = 100
        self.smallBlind = 50
        self.pot = 0
        self.round = -1
        self.playerTurn = 0
        self.hands = 0
        self.totalValue = 0
        self.noOfPair = 0
        self.playerValue = [0, 0, 0, 0]
        self.currentBet = 0
        self.previousBet = 0

        cards.getCardList()
        dealer.getDealerCards()

    def lose(self):
        screen.blit(assets.back, (0, 0))

        pygame.display.update()

    def displayFlop(self):
        while self.flopX > 600:
            for i in range(3):
                self.flopCards = pygame.image.load(river.riverCards[i][2])
                self.flopCards = pygame.transform.scale(self.flopCards, assets.cardScale)
                screen.blit(self.flopCards, (self.flopX, 306))
                self.flopX = self.flopX - 125
                time.sleep(0.5)
                pygame.display.update()

    def displayTurn(self):
        self.turnCard = pygame.image.load(river.riverCards[3][2])
        self.turnCard = pygame.transform.scale(self.turnCard, assets.cardScale)
        screen.blit(self.turnCard, (475, 306))
        time.sleep(0.5)
        pygame.display.update()

    def displayRiver(self):
        self.riverCard = pygame.image.load(river.riverCards[4][2])
        self.riverCard = pygame.transform.scale(self.riverCard, assets.cardScale)
        screen.blit(self.riverCard, (350, 306))
        time.sleep(0.5)
        pygame.display.update()

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

        self.helpPage1 = assets.helpFont.render("How to play", True, Colours._white)  # 249 x 45
        self.helpPage2 = assets.helpFont.render("How to win", True, Colours._white)  # 235 x 45
        self.helpPage3 = assets.helpFont.render("Possible hands", True, Colours._white)  # 332 x 45

        self.help1 = assets.compChipsFont.render("The quick brown fox jumps over the lazy dog. 123456789", True,
                                            Colours._white)
        self.help2 = assets.helpFont.render("increase or decrease your bet, when you want to make the", True,
                                            Colours._white)
        self.help3 = assets.helpFont.render("bet click the box that your bet is in, if you do not wish", True,
                                            Colours._white)
        self.help4 = assets.helpFont.render("to make a bet and the opponent has not  made a bet click", True,
                                            Colours._white)
        self.help5 = assets.helpFont.render("the check/call button and the next cards in the river will", True,
                                            Colours._white)
        self.help6 = assets.helpFont.render("be displayed. At the start of each hand there are blinds", True,
                                            Colours._white)
        self.help7 = assets.helpFont.render("which is a forced bet that both players have to bet, this", True,
                                            Colours._white)
        self.help8 = assets.helpFont.render("is default to 100 chips however you can change this to be", True,
                                            Colours._white)
        self.help9 = assets.helpFont.render("higher or lower in multiples of 50.", True, Colours._white)

        self.help12 = assets.helpFont.render("To win get all of your opponents chips by betting your", True,
                                             Colours._white)
        self.help13 = assets.helpFont.render("own chips with theirs when you think you have a better", True,
                                             Colours._white)
        self.help14 = assets.helpFont.render("hand. E.g. if you only have one pair you may not want to", True,
                                             Colours._white)
        self.help15 = assets.helpFont.render("bet as much as if you had a flush or straight.", True, Colours._white)

        self.help16 = assets.inGameFont.render("Pair:", True, Colours._white)
        self.help17 = assets.inGameFont.render("Two Pair:", True, Colours._white)
        self.help18 = assets.inGameFont.render("Three of a kind:", True, Colours._white)
        self.help19 = assets.inGameFont.render("Straight:", True, Colours._white)
        self.help20 = assets.inGameFont.render("Flush:", True, Colours._white)
        self.help21 = assets.inGameFont.render("Full House:", True, Colours._white)
        self.help22 = assets.inGameFont.render("Four of a kind:", True, Colours._white)
        self.help23 = assets.inGameFont.render("Straight Flush:", True, Colours._white)
        self.help24 = assets.inGameFont.render("Royal Flush:", True, Colours._white)

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
        self.threeOAK = pygame.transform.scale(self.threeOAK, (67, 103))
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
        screen.blit(self.back, (0, 0))

        self.titleBack = pygame.transform.scale(assets.titleBack, (750, 120))
        screen.blit(self.titleBack, (265, 10))

        screen.blit(assets.titleText, (543.5, 10))  # 193 x 69

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
computer1 = Computer(1)
computer2 = Computer(2)
computer3 = Computer(3)
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
