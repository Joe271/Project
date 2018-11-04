import random, pygame, sys, time
from pygame.locals import *

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

        pygame.init()
        pygame.font.init()
        self.screenwidth = 1280
        self.screenheight = 720
        self.framerate = 60
        self.clock = pygame.time.Clock()
        self.screenSize = ((self.screenwidth,self.screenheight))
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Poker")
        self.turn = 0

        self.back = pygame.image.load("back3.JPG")
        self.screen.blit(self.back,(0,0))
        self.table = pygame.image.load("table2.JPG")
        self.screen.blit(self.table,(150,150))
##        self.screen.blit(cards.backOfCard,(605,0))
        pygame.display.update()

        #Gets the cards
        user.getUserCards()
        computer.getComputerCards()
        river.getRiverCards()

        time.sleep(1)

        x = 567
        for z in range (2): #Displays all 4 player cards
            self.Card = pygame.image.load(user.Cards[z])
            self.Card = pygame.transform.scale(self.Card, (71, 108))
            self.screen.blit(self.Card, (x, 600))
            self.screen.blit(cards.backOfCard, (x, 10))
            x = x + 75
            #time.sleep(0.75)
            pygame.display.update()

        #time.sleep(0.75)
        pygame.draw.rect(self.screen, pygame.Color(0, 75, 255), (723, 600, 100, 50), 0) #Check
        pygame.draw.rect(self.screen, pygame.Color(0, 75, 255), (723, 660, 100, 50), 0) #Call
        pygame.draw.rect(self.screen, pygame.Color(0, 75, 255), (833, 600, 100, 50), 0) #Fold

        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.checkButton = self.font.render("Check", True, (0,0,0))
        self.screen.blit(self.checkButton,(726,610))

        self.callButton = self.font.render("Call", True, (0,0,0))
        self.screen.blit(self.callButton,(726,670))

        self.foldButton = self.font.render("Fold", True, (0,0,0))
        self.screen.blit(self.foldButton,(838,610))

        #got chips on the screen
        self.chipsText = self.font.render("Chips:", True, (210,210,210))
        self.screen.blit(self.chipsText,(450,610))
        self.screen.blit(self.chipsText,(450,10))
        self.userChipsText = self.font.render(str(user.Chips), True, (210,210,210))
        self.computerChipsText = self.font.render(str(computer.Chips), True, (210,210,210))
        self.screen.blit(self.userChipsText,(450,640))
        self.screen.blit(self.computerChipsText,(450,40))

        self.potText = self.font.render("Pot: "+str(dealer.pot), True, (0,0,0))
        self.screen.blit(self.potText,(600,200))

        pygame.display.update()

        def displayFlop():
            x = 850
            for i in range(3):
                self.flopCards = pygame.image.load(river.riverCards[i])
                self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
                self.screen.blit(self.flopCards, (x, 306))
                x = x - 125
                time.sleep(0.5)
                pygame.display.update()

        def displayTurn():
            self.flopCards = pygame.image.load(river.riverCards[3])
            self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
            self.screen.blit(self.flopCards, (475, 306))
            time.sleep(0.5)
            pygame.display.update()

        def displayRiver():
            self.flopCards = pygame.image.load(river.riverCards[4])
            self.flopCards = pygame.transform.scale(self.flopCards, (71, 108))
            self.screen.blit(self.flopCards, (350, 306))
            time.sleep(0.5)
            pygame.display.update()

        def makeBet():
            self.userBet = []
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_BACKSPACE:
                            self.userBet = self.userBet[0:-1]
                            self.text = self.font.render(str(self.userBet), True, (0,0,0))
                            self.screen.blit(self.text, (800, 200))
                            pygame.display.update()
                        elif event.key == K_RETURN:
                            False
                        elif event.key <= 127:
                            self.userBet.append(chr(event.key))
                            self.text = self.font.render(str(self.userBet), True, (0,0,0))
                            self.screen.blit(self.text, (800, 200))
                            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 650:
                            print("1")
                            makeBet()
                    if pygame.mouse.get_pos()[0] >=723 and pygame.mouse.get_pos()[1] >= 660:
                        if pygame.mouse.get_pos()[0] <= 823 and pygame.mouse.get_pos()[1] <= 710:
                            print("2")
                    if pygame.mouse.get_pos()[0] >=833 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 933 and pygame.mouse.get_pos()[1] <= 650:
                            print("3")

if __name__ == "__main__":
    poker = Game()
