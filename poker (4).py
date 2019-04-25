import random, pygame, sys, time
from pygame.locals import *

class Cards():
    def __init__(self):
        self.backOfCard = pygame.image.load("BackOfCard.JPG")
        self.backOfCard = pygame.transform.scale(self.backOfCard, (71, 108))
        self.number = 0
        self.cardList = []
##        self.clubList = []
##        self.diamondList = []
##        self.heartList = []
##        self.spadeList = []
        for number in range(13):
            self.cardList.append(["C"+str(number+1)+".JPG","C",number+1])
        for number in range(13):
            self.cardList.append(["D"+str(number+1)+".JPG","D",number+1])
        for number in range(13):
            self.cardList.append(["H"+str(number+1)+".JPG","H",number+1])
        for number in range(13):
            self.cardList.append(["S"+str(number+1)+".JPG","S",number+1])
        #self.allCardList = [self.clubList, self.diamondList, self.heartList, self.spadeList]
        
cards = Cards()
        
class Dealer():
    def __init__(self):
        self.dealerCards = cards.cardList

dealer = Dealer()
    
class User():
    def __init__(self):
        self.userCards = ["",""]
        self.userChips = 5000

    def getUserCards(self):
        counter = 51
        for i in range (2):
            pick = random.randint(0,counter)
            user.userCards[i] = dealer.dealerCards[pick][0]
            dealer.dealerCards.pop(pick)
            counter = counter - 1
        print("U",user.userCards)

user = User()

class Computer():
    def __init__(self):
        self.computerCards = ["",""]
        self.computerChips = 5000

    def getComputerCards(self):
        counter = 49
        for i in range (2):
            pick = random.randint(0,counter)
            computer.computerCards[i] = dealer.dealerCards[pick][0]
            dealer.dealerCards.pop(pick)
            counter = counter - 1
        print("C",computer.computerCards)

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

class Setup():
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

        self.back = pygame.image.load("background.JPG")
        self.screen.blit(self.back,(0,0))
        self.table = pygame.image.load("table1.JPG")
        self.screen.blit(self.table,(150,150))
        #self.screen.blit(cards.backOfCard,(605,0))
        pygame.display.update()

        #Gets the cards
        user.getUserCards()
        computer.getComputerCards()
        river.getRiverCards()
    
        time.sleep(1)
        
        x = 567
        for z in range (2): #Displays all 4 cards
            self.userCard = pygame.image.load(user.userCards[z])
            self.userCard = pygame.transform.scale(self.userCard, (71, 108))
            self.screen.blit(self.userCard, (x, 600))
            self.screen.blit(cards.backOfCard, (x, 10))
            x = x + 75
            time.sleep(0.75)
            pygame.display.update()

        x = 850
        for p in range (5): #Displays river
            self.riverCards = pygame.image.load(river.riverCards[p])
            self.riverCards = pygame.transform.scale(self.riverCards, (71, 108))
            self.screen.blit(self.riverCards, (x, 306))
            x = x - 125
            time.sleep(0.5)
            pygame.display.update()
        

##        x = 0
##        for each in cards.clubList:
##            self.C = pygame.image.load(each)
##            self.C = pygame.transform.scale(self.C, (71, 108))
##            self.screen.blit(self.C,(x,0))
##            x = x + 73
##        x = 0
##        for each in cards.diamondList:
##            self.D = pygame.image.load(each)
##            self.D = pygame.transform.scale(self.D, (71, 108))
##            self.screen.blit(self.D,(x,110))
##            x = x + 73
##        x = 0
##        for each in cards.heartList:
##            self.H = pygame.image.load(each)
##            self.H = pygame.transform.scale(self.H, (71, 108))
##            self.screen.blit(self.H,(x,220))
##            x = x + 73
##        x = 0
##        for each in cards.spadeList:
##            self.S = pygame.image.load(each)
##            self.S = pygame.transform.scale(self.S, (71, 108))
##            self.screen.blit(self.S,(x,330))
##            x = x + 73
    
if __name__ == "__main__":
    poker = Setup()
