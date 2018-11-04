## Poker

import random, pygame, sys, time
from pygame.locals import *

class Colours():
    white = pygame.Color(255,255,255)
    black = pygame.Color(0,0,0)
    blue = pygame.Color(0, 75, 255)

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
        print("U",user.Cards)

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
        print("C",computer.Cards)

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
        print("R",river.riverCards)

river = River()

class Game():
    def __init__(self):

        self.turn = 0
        self.bet = 0

        self.back = pygame.image.load("back3.JPG")
        screen.blit(self.back,(0,0))
        self.table = pygame.image.load("table2.JPG")
        screen.blit(self.table,(150,150))
##        screen.blit(cards.backOfCard,(605,0))
        pygame.display.update()

        #Gets the cards
        user.getUserCards()
        computer.getComputerCards()
        river.getRiverCards()

        pygame.draw.rect(screen, Colours.blue, (723, 600, 100, 50), 0) #Bet
        pygame.draw.rect(screen, Colours.blue, (723, 660, 100, 50), 0) #Call
        pygame.draw.rect(screen, Colours.blue, (833, 600, 100, 50), 0) #Fold
        self.upButton = pygame.image.load("upBet.fw.PNG")
        self.upButton = pygame.transform.scale(self.upButton, (50,50))
        self.downButton = pygame.image.load("downBet.fw.PNG")
        self.downButton = pygame.transform.scale(self.downButton, (50,50))
        screen.blit(self.upButton,(950,600))
        screen.blit(self.downButton,(950,660))

        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.checkButton = self.font.render("Bet", True, Colours.black)
        screen.blit(self.checkButton,(726,610))

        self.callButton = self.font.render("Call", True, Colours.black)
        screen.blit(self.callButton,(726,670))

        self.foldButton = self.font.render("Fold", True, Colours.black)
        screen.blit(self.foldButton,(838,610))

        #got chips on the screen
        pygame.draw.rect(screen, Colours.black, (445,600,105,80), 0)
        pygame.draw.rect(screen, Colours.black, (445,10,105,80), 0)
        pygame.draw.rect(screen, Colours.black, (1015, 635, 80, 40), 0)
        self.userBetText = self.font.render(str(self.bet), True, Colours.white)
        screen.blit(self.userBetText, (1020, 640))
        self.chipsText = self.font.render("Chips:", True, Colours.white)
        screen.blit(self.chipsText,(450,610))
        screen.blit(self.chipsText,(450,20))
        self.userChipsText = self.font.render(str(user.Chips), True, Colours.white)
        self.computerChipsText = self.font.render(str(computer.Chips), True, Colours.white)
        screen.blit(self.userChipsText,(450,640))
        screen.blit(self.computerChipsText,(450,50))

        self.potBox = pygame.draw.rect(screen, Colours.black, (595,195,165,40))
        self.potText = self.font.render("Pot: "+str(dealer.pot), True, (Colours.white))
        screen.blit(self.potText,(600,200))

        pygame.display.update()

        time.sleep(1)

        x = 567
        for z in range (2): #Displays all 4 player cards
            self.Card = pygame.image.load(user.Cards[z])
            self.Card = pygame.transform.scale(self.Card, (71, 108))
            screen.blit(self.Card, (x, 600))
            screen.blit(cards.backOfCard, (x, 10))
            x = x + 75
            time.sleep(0.75)
            pygame.display.update()

        def displayFlop():
            x = 850
            for i in range(3):
                self.flopCards = pygame.image.load(river.riverCards[i])
                self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
                screen.blit(self.flopCards, (x, 306))
                x = x - 125
                time.sleep(0.5)
                pygame.display.update()

        def displayTurn():
            self.flopCards = pygame.image.load(river.riverCards[3])
            self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
            screen.blit(self.flopCards, (475, 306))
            time.sleep(0.5)
            pygame.display.update()

        def displayRiver():
            self.flopCards = pygame.image.load(river.riverCards[4])
            self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
            screen.blit(self.flopCards, (350, 306))
            time.sleep(0.5)
            pygame.display.update()

        def makeBet():
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 600:
                            if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 650:
                                if user.Chips > 0:
                                    pygame.draw.rect(screen, Colours.black, (1015,635,80,40), 0)
                                    pygame.draw.rect(screen, Colours.black, (445,640,105,40), 0)
                                    self.bet = self.bet + 50
                                    user.Chips = user.Chips - 50
                                    self.userBetText = self.font.render(str(self.bet), True, Colours.white)
                                    screen.blit(self.userBetText,(1020,640))
                                    self.userChipsText = self.font.render(str(user.Chips), True, Colours.white)
                                    screen.blit(self.userChipsText,(450,640))
                                    self.upBetPress = pygame.image.load("upBetPress.fw.PNG")
                                    self.upBetPress = pygame.transform.scale(self.upBetPress,(50,50))
                                    screen.blit(self.upBetPress, (950,600))
                                    pygame.display.update()
                                    time.sleep(0.05)
                                    screen.blit(self.upButton,(950,600))
                                    pygame.display.update()
                                else:
                                    user.Chips = 0

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= 950 and pygame.mouse.get_pos()[1] >= 660:
                            if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 7100:
                                if user.Chips < 5000:
                                    pygame.draw.rect(screen, Colours.black, (1015,635,80,40), 0)
                                    pygame.draw.rect(screen, Colours.black, (445,640,105,40), 0)
                                    self.bet = self.bet - 50
                                    user.Chips = user.Chips + 50
                                    self.userBetText = self.font.render(str(self.bet), True, Colours.white)
                                    screen.blit(self.userBetText,(1020,640))
                                    self.userChipsText = self.font.render(str(user.Chips), True, Colours.white)
                                    screen.blit(self.userChipsText,(450,640))
                                    self.downBetPress = pygame.image.load("downBetPress.fw.PNG")
                                    self.downBetPress = pygame.transform.scale(self.downBetPress,(50,50))
                                    screen.blit(self.downBetPress, (950,660))
                                    pygame.display.update()
                                    time.sleep(0.1)
                                    screen.blit(self.downButton,(950,660))
                                    pygame.display.update()
                                else:
                                    user.Chips = 5000

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >=1015 and pygame.mouse.get_pos()[1] >= 635:
                            if pygame.mouse.get_pos()[0] <= 1095 and pygame.mouse.get_pos()[1] <= 670:
                                if self.bet > 0:
                                    dealer.pot = self.bet
                                    self.bet = 0
                                    self.potBox = pygame.draw.rect(screen, Colours.black, (595,195,1651,40))
                                    self.potText = self.font.render("Pot: "+str(dealer.pot), True, (Colours.white))
                                    screen.blit(self.potText,(600,200))
                                    pygame.draw.rect(screen, Colours.black, (1015,635,80,40), 0)
                                    self.userBetText = self.font.render(str(self.bet), True, Colours.white)
                                    screen.blit(self.userBetText,(1020,640))
                                    pygame.display.update()
                                else:
                                    pass

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 650:
                            makeBet()
                    if pygame.mouse.get_pos()[0] >=723 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710 and self.bet == 0:
                            displayFlop()
                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            print("3")

    def menu(self):
        screen.blit(self.back,(0,0))

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screenwidth = 1280
    screenheight = 720
    framerate = 60
    clock = pygame.time.Clock()
    screenSize = ((screenwidth,screenheight))
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Poker")
    game = Game()
