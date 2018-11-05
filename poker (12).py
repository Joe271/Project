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

cards = Cards()

class Dealer():
    def __init__(self):
        self.dealerCards = cards.cardList
        self.pot = 0

dealer = Dealer()

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

user = User()

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

computer = Computer()

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

river = River()

class Assets():
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
        self.menuSize = 50
        self.titleSize = 100

        self.inGameFont = pygame.font.Font("freesansbold.ttf", self.inGameSize)
        self.menuFont = pygame.font.Font("freesansbold.ttf", self.menuSize)
        self.titleFont = pygame.font.Font("freesansbold.ttf", self.titleSize)

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

assets = Assets()

class Game():
    def __init__(self):

        ## Variables

        self.turn = 0
        self.bet = 0
        self.playerCardsX = 567
        self.flopX = 850
        self.cardScale = (71, 108)
        self.betButtonScale = (50,50)

        ## Gets cards for each player

        user.getUserCards()
        computer.getComputerCards()
        river.getRiverCards()

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

        def displayFlop():
            while self.flopX > 600:
                for i in range(3):
                    self.flopCards = pygame.image.load(river.riverCards[i])
                    self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
                    screen.blit(self.flopCards, (self.flopX, 306))
                    self.flopX = self.flopX - 125
                    #time.sleep(0.5)
                    pygame.display.update()

        def displayTurn():
            self.flopCards = pygame.image.load(river.riverCards[3])
            self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
            screen.blit(self.flopCards, (475, 306))
            time.sleep(0.5)
            pygame.display.update()

        def displayRiver():
            self.flopCards = pygame.image.load(river.riverCards[4])
            self.flopCards = pygame.transform.scale(self.flopCards, self.cardScale)
            screen.blit(self.flopCards, (350, 306))
            #time.sleep(0.5)
            pygame.display.update()

        def makeBet():
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
                                    screen.blit(self.userBetText,(1020,640))
                                    self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                                    screen.blit(self.userChipsText,(450,640))
                                    self.upBetPress = pygame.transform.scale(assets.upBetPress, self.betButtonScale)
                                    screen.blit(self.upBetPress, (950,600))
                                    pygame.display.update()
                                    time.sleep(0.12)
                                    screen.blit(self.upBet,(950,600))
                                    pygame.display.update()
                                else:
                                    user.Chips = 0

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 660:
                            if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 7100:
                                if user.Chips < 5000:
                                    pygame.draw.rect(screen, Colours.lightGrey, (1015,635,80,40), 0)
                                    pygame.draw.rect(screen, Colours.lightGrey, (445,640,105,40), 0)
                                    self.bet = self.bet - 50
                                    user.Chips = user.Chips + 50
                                    self.userBetText = assets.inGameFont.render(str(self.bet), True, Colours.black)
                                    screen.blit(self.userBetText,(1020,640))
                                    self.userChipsText = assets.inGameFont.render(str(user.Chips), True, Colours.black)
                                    screen.blit(self.userChipsText,(450,640))
                                    self.downBetPress = pygame.transform.scale(assets.downBetPress, self.betButtonScale)
                                    screen.blit(self.downBetPress, (950,660))
                                    pygame.display.update()
                                    time.sleep(0.12)
                                    screen.blit(self.downBet,(950,660))
                                    pygame.display.update()
                                else:
                                    user.Chips = 5000

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >=1015 and pygame.mouse.get_pos()[1] >= 635:
                            if pygame.mouse.get_pos()[0] <= 1095 and pygame.mouse.get_pos()[1] <= 670:
                                if self.bet > 0:
                                    dealer.pot = self.bet
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

        while True:
            self.gamePress = pygame.transform.scale(assets.menuButtonPress, (100,50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    False
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
                            makeBet()
                    if pygame.mouse.get_pos()[0] >=723 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710 and self.bet == 0:
                            screen.blit(self.gamePress, (723,660))
                            screen.blit(assets.callButtonText, (726,670))
                            pygame.display.update()
                            time.sleep(0.2)
                            screen.blit(self.menuButton, (723,660))
                            screen.blit(assets.callButtonText, (726,670))
                            pygame.display.update()
                            displayFlop()
                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            print("3")

class Help():
    def __init__(self):
        pass
        # this next <-------------------------------------------------------------------------------------------------------------------


class Menu():
    def __init__(self):

        self.back = pygame.transform.scale(assets.back, (1280, 720))
        screen.blit(self.back,(0,0))

        self.titleBack = pygame.transform.scale(assets.titleBack, (750, 120))
        screen.blit(self.titleBack, (265, 10))

        screen.blit(assets.titleText,(497.5, 20))

        assets.menuButton = pygame.transform.scale(assets.menuButton, (500,80))
        assets.menuButtonPress = pygame.transform.scale(assets.menuButtonPress, (500,80))
        screen.blit(assets.menuButton, (390,185.5))
        screen.blit(assets.menuButton, (390,285.5))
        screen.blit(assets.menuButton, (390,385.5))
        screen.blit(assets.menuButton, (390,485.5))
        screen.blit(assets.menuButton, (390,585.5))

        screen.blit(assets.playText, (587,200))
        screen.blit(assets.saveText, (579.5,300))
        screen.blit(assets.loadText, (579.5,400))
        screen.blit(assets.helpText, (582.5,500))
        screen.blit(assets.exitText, (590.5,600))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 390 and pygame.mouse.get_pos()[0] <= 890:
                        if pygame.mouse.get_pos()[1] >= 185.5 and pygame.mouse.get_pos()[1] <= 265.5:
                            screen.blit(assets.menuButtonPress, (390,185.5))
                            screen.blit(assets.playText, (587,200))
                            pygame.display.update()
                            time.sleep(0.2)
                            game = Game()

                        if pygame.mouse.get_pos()[1] >= 285.5 and pygame.mouse.get_pos()[1] <= 365.5:
                            print("2")

                        if pygame.mouse.get_pos()[1] >= 385.5 and pygame.mouse.get_pos()[1] <= 465.5:
                            print("3")

                        if pygame.mouse.get_pos()[1] >= 485.5 and pygame.mouse.get_pos()[1] <= 565.5:
                            print("4")

                        if pygame.mouse.get_pos()[1] >= 585.5 and pygame.mouse.get_pos()[1] <= 665.5:
                            pygame.quit()
                            sys.exit()

if __name__ == "__main__":
    screenwidth = 1280
    screenheight = 720
    framerate = 60
    clock = pygame.time.Clock()
    screenSize = ((screenwidth,screenheight))
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Poker")
    menu = Menu()
