## Poker

import random, pygame, sys, time
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
        self.backOfCard = pygame.image.load("BackOfCard.JPG")
        self.backOfCard = pygame.transform.scale(self.backOfCard, (71, 108))
        self.number = 0
        self.cardList = []
        for number in range(13):
            self.cardList.append(["C"+str(number+1)+".JPG","C",number+1])
        for number in range(13):
            self.cardList.append(["D"+str(number+1)+".JPG","D",number+1])
        for number in range(13):
            self.cardList.append(["H"+str(number+1)+".JPG","H",number+1])
        for number in range(13):
            self.cardList.append(["S"+str(number+1)+".JPG","S",number+1])

class Dealer():
    def __init__(self):
        self.dealerCards = cards.cardList
        self.pot = 0

class Player():
    def __init__(self):
        self.Cards = ["",""]
        self.Chips = 5000

class User(Player):
    def __init__(self):
        super().__init__()

    def getUserCards(self):
        counter = 51
        for i in range (2):
            pick = random.randint(0,counter)
            user.Cards[i] = dealer.dealerCards[pick][0]
            dealer.dealerCards.pop(pick)
            counter = counter - 1

class Computer(Player):
    def __init__(self):
        super().__init__()

    def getComputerCards(self):
        counter = 49
        for i in range (2):
            pick = random.randint(0,counter)
            computer.Cards[i] = dealer.dealerCards[pick][0]
            dealer.dealerCards.pop(pick)
            counter = counter - 1

class River():
    def __init__(self):
        self.riverCards = ["","","","",""]

    def getRiverCards(self):
        counter = 47
        for q in range (5):
            pick = random.randint(0,counter)
            river.riverCards[q] = dealer.dealerCards[pick][0]
            dealer.dealerCards.pop(pick)
            counter = counter - 1

class Assets(): # All assets but cards
    def __init__(self):

        ## Loading all images

        self.back = pygame.image.load("background (2).JPG")
        self.table = pygame.image.load("table (2).PNG")
        self.titleBack = pygame.image.load("titleBack.PNG")
        self.upBet = pygame.image.load("upBet.fw.PNG")
        self.downBet = pygame.image.load("downBet.fw.PNG")
        self.upBetPress = pygame.image.load("upBetPress.fw.PNG")
        self.downBetPress = pygame.image.load("downBetPress.fw.PNG")
        self.menuButton = pygame.image.load("menuButton.PNG")
        self.menuButtonPress = pygame.image.load("menuButtonPress.PNG")

        ## Defining fonts

        self.inGameSize = 30
        self.helpSize = 44
        self.menuSize = 50
        self.titleSize = 100

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
        self.userBetText = self.inGameFont.render("0", True, Colours.black)
        self.userChipsText = self.inGameFont.render("5000", True, Colours.black)
        self.computerChipsText = self.inGameFont.render("5000", True, Colours.black)
        self.chipsText = self.inGameFont.render("Chips:", True, Colours.black)
        self.potText = self.inGameFont.render("Pot: 0", True, (Colours.black))
        self.nextButtonText = self.menuFont.render("Next", True, (Colours.black))
        self.backButtonText = self.menuFont.render("Back", True, (Colours.black))

class Game():
    def __init__(self):

        ## Variables

        self.playerTurn = True
        self.bet = 0
        self.playerCardsX = 567
        self.flopX = 850
        self.cardScale = (71, 108)
        self.betButtonScale = (50,50)
        self.bigBlind = 100
        self.smallBlind = 50

        ## Gets cards for each player

        user.getUserCards()
        computer.getComputerCards()
        river.getRiverCards()

    def playGame(self):
        ## Displays all starting assets
        self.back = pygame.transform.scale(assets.back, (1280,720))
        self.table = pygame.transform.scale(assets.table, (980,420))
        screen.blit(self.back,(0,0))
        screen.blit(self.table,(150,150))

        self.menuButton = pygame.transform.scale(assets.menuButton, (100,50))
        screen.blit(self.menuButton, (723,600)) # Bet button image
        screen.blit(self.menuButton, (723,660)) # Call button image
        screen.blit(self.menuButton, (833,600)) # Fold button image
        #pygame.draw.rect(screen, Colours.blue, (723, 600, 100, 50), 0) # Bet button rect
        #pygame.draw.rect(screen, Colours.blue, (723, 660, 100, 50), 0) # Call button rect
        #pygame.draw.rect(screen, Colours.blue, (833, 600, 100, 50), 0) # Fold button rect
        screen.blit(assets.betButtonText,(726,610)) # Bet button text
        screen.blit(assets.callButtonText,(726,670)) # Call button text
        screen.blit(assets.foldButtonText,(838,610)) # Fold button text

        self.upBet = pygame.transform.scale(assets.upBet, self.betButtonScale) # Grey increase bet button
        self.downBet = pygame.transform.scale(assets.downBet, self.betButtonScale) # Grey decrease bet button
        screen.blit(self.upBet,(950,600))
        screen.blit(self.downBet,(950,660))

        pygame.draw.rect(screen, Colours.lightGrey, (445,600,105,80), 0) # User chips background
        pygame.draw.rect(screen, Colours.lightGrey, (445,10,105,80), 0) # Computer chips background
        pygame.draw.rect(screen, Colours.lightGrey, (1015, 635, 80, 40), 0) # User bet background

        screen.blit(assets.userBetText, (1020, 640)) # User bet text
        screen.blit(assets.chipsText,(450,610)) # "Chips:" user
        screen.blit(assets.chipsText,(450,20)) # "Chips:" computer
        screen.blit(assets.userChipsText,(450,640)) # User chips text
        screen.blit(assets.computerChipsText,(450,50)) # Computer chips text

        self.potBox = pygame.draw.rect(screen, Colours.lightGrey, (595,195,165,40)) # Pot background
        screen.blit(assets.potText,(600,200))

        screen.blit(help.backPage, (30, 620))
        screen.blit(assets.backButtonText, (65, 625))

        pygame.display.update()

        #time.sleep(1)

        for z in range (2): #Displays all 4 player cards
            self.Card = pygame.image.load(user.Cards[z])
            self.Card = pygame.transform.scale(self.Card, self.cardScale)
            screen.blit(self.Card, (self.playerCardsX, 600))
            screen.blit(cards.backOfCard, (self.playerCardsX, 10))
            self.playerCardsX = self.playerCardsX + 75
            #time.sleep(0.75)
            pygame.display.update()

        self.playerCardsX = 567

        while True:
            self.gamePress = pygame.transform.scale(assets.menuButtonPress, (100,50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 650:
                            screen.blit(self.gamePress, (723,600))
                            screen.blit(assets.betButtonText, (726,610))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(self.menuButton, (723,600))
                            screen.blit(assets.betButtonText, (726,610))
                            pygame.display.update()
                            self.makeBet()
                    if pygame.mouse.get_pos()[0] >=723 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710 and self.bet == 0:
                            screen.blit(self.gamePress, (723,660))
                            screen.blit(assets.callButtonText, (726,670))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(self.menuButton, (723,660))
                            screen.blit(assets.callButtonText, (726,670))
                            pygame.display.update()
                            self.displayFlop()
                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            print("3")

                    if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 620:
                        if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 695:
                            screen.blit(help.backPagePress, (30, 620))
                            screen.blit(assets.backButtonText, (65, 635))
                            pygame.display.update()
                            time.sleep(0.1)
                            menu.displayMenu()


    def displayFlop(self):
        while self.flopX > 600:
            for i in range(3):
                self.flopCards = pygame.image.load(river.riverCards[i])
                self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
                screen.blit(self.flopCards, (self.flopX, 306))
                self.flopX = self.flopX - 125
                #time.sleep(0.5)
                pygame.display.update()

    def displayTurn(self):
        self.flopCards = pygame.image.load(river.riverCards[3])
        self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
        screen.blit(self.flopCards, (475, 306))
        time.sleep(0.5)
        pygame.display.update()

    def displayRiver(self):
        self.flopCards = pygame.image.load(river.riverCards[4])
        self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
        screen.blit(self.flopCards, (350, 306))
        #time.sleep(0.5)
        pygame.display.update()

    def makeBet(self):
        self.betting = True
        while self.betting:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 650:
                            if user.Chips > 0:
                                pygame.draw.rect(screen, Colours.lightGrey, (1015,635,80,40), 0)
                                pygame.draw.rect(screen, Colours.lightGrey, (445,640,105,40), 0)
                                self.bet = self.bet + 50
                                user.Chips = user.Chips - 50
                                self.userBetText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                                screen.blit(self.userBetText,(1020,640))
                                screen.blit(self.userChipsText,(450,640))
                                self.upBetPress = pygame.transform.scale(assets.upBetPress, self.betButtonScale)
                                screen.blit(self.upBetPress, (950,600))
                                pygame.display.update()
                                time.sleep(0.12)
                                screen.blit(self.upBet,(950,600))
                                pygame.display.update()

                            else:
                                user.Chips = 0

                    if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 7100:
                            if user.Chips < 5000:
                                pygame.draw.rect(screen, Colours.lightGrey, (1015,635,80,40), 0)
                                pygame.draw.rect(screen, Colours.lightGrey, (445,640,105,40), 0)
                                self.bet = self.bet - 50
                                user.Chips = user.Chips + 50
                                self.userBetText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                                screen.blit(self.userBetText,(1020,640))
                                screen.blit(self.userChipsText,(450,640))
                                self.downBetPress = pygame.transform.scale(assets.downBetPress, self.betButtonScale)
                                screen.blit(self.downBetPress, (950,660))
                                pygame.display.update()
                                time.sleep(0.12)
                                screen.blit(self.downBet,(950,660))
                                pygame.display.update()

                            else:
                                user.Chips = 5000

                    if pygame.mouse.get_pos()[0] >=1015 and pygame.mouse.get_pos()[1] >= 635:
                        if pygame.mouse.get_pos()[0] <= 1095 and pygame.mouse.get_pos()[1] <= 670:
                            if self.bet > 0:
                                dealer.pot = dealer.pot + self.bet
                                self.bet = 0
                                self.potBox = pygame.draw.rect(screen, Colours.lightGrey, (595,195,165,40))
                                self.potText = assets.inGameFont.render("Pot: "+str(dealer.pot), True, (Colours.black))
                                screen.blit(self.potText,(600,200))
                                pygame.draw.rect(screen, Colours.lightGrey, (1015,635,80,40), 0)
                                self.userBetText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                screen.blit(self.userBetText,(1020,640))
                                pygame.display.update()
                                self.betting = False

                            else:
                                pass

    def blinds(self):
        pass

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
        self.nextPagePress = pygame.transform.scale(assets.menuButtonPress, (175,75))
        self.backPagePress = self.nextPagePress

    def page1(self):
        screen.blit(self.back, (0,0))
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
        screen.blit(self.back, (0,0))
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
        screen.blit(self.back, (0,0))
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
        self.straight1 = pygame.transform.scale(self.straight1, (67,103))
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
user = User()
computer = Computer()
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
    screenSize = ((screenwidth,screenheight))
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Poker")
    menu.displayMenu()
