## Menu

import pygame, sys, time
from pygame.locals import *

pygame.init()
pygame.font.init()

screenwidth = 1280
screenheight = 720
framerate = 60
clock = pygame.time.Clock()
screenSize = ((screenwidth,screenheight))
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Poker")

class Colours():
    white = pygame.Color(255,255,255)
    black = pygame.Color(0,0,0)
    blue = pygame.Color(0, 75, 255)

class Menu():
    def __init__(self):
        self.back = pygame.image.load("back3.JPG")
        self.inGameSize = 30
        self.menuSize = 50
        self.titleSize = 100

        self.inGameFont = pygame.font.Font("freesansbold.ttf", self.inGameSize)
        self.menuFont = pygame.font.Font("freesansbold.ttf", self.menuSize)
        self.titleFont = pygame.font.Font("freesansbold.ttf", self.titleSize)

        self.titleText = self.titleFont.render("Poker", True, (Colours.black)) #285 x 101
        self.playText = self.menuFont.render("Play", True, (Colours.black)) # 106 x 51
        self.saveText = self.menuFont.render("Save", True, (Colours.black)) # 121 x 51
        self.loadText = self.menuFont.render("Load", True, (Colours.black)) # 121 x 51
        self.helpText = self.menuFont.render("Help", True, (Colours.black)) # 115 x 51
        self.exitText = self.menuFont.render("Exit", True, (Colours.black)) # 99 x 51

    def displayMenu(self):

        screen.blit(self.back,(0,0))

        screen.blit(self.titleText,(497.5,10))

        pygame.draw.rect(screen, Colours.blue, (390,185.5,500,80))
        pygame.draw.rect(screen, Colours.blue, (390,285.5,500,80))
        pygame.draw.rect(screen, Colours.blue, (390,385.5,500,80))
        pygame.draw.rect(screen, Colours.blue, (390,485.5,500,80))
        pygame.draw.rect(screen, Colours.blue, (390,585.5,500,80))

        screen.blit(self.playText, (587,200))
        screen.blit(self.saveText, (579.5,300))
        screen.blit(self.loadText, (579.5,400))
        screen.blit(self.helpText, (582.5,500))
        screen.blit(self.exitText, (590.5,600))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 390 and pygame.mouse.get_pos()[0] <= 890:
                        if pygame.mouse.get_pos()[1] >= 185.5 and pygame.mouse.get_pos()[1] <= 265.5:
                            print("1")

                        if pygame.mouse.get_pos()[1] >= 285.5 and pygame.mouse.get_pos()[1] <= 365.5:
                            print("2")

                        if pygame.mouse.get_pos()[1] >= 385.5 and pygame.mouse.get_pos()[1] <= 465.5:
                            print("3")

                        if pygame.mouse.get_pos()[1] >= 485.5 and pygame.mouse.get_pos()[1] <= 565.5:
                            print("4")

                        if pygame.mouse.get_pos()[1] >= 585.5 and pygame.mouse.get_pos()[1] <= 665.5:
                            print("5")

start = Menu()

if __name__ == "__main__":
    start.displayMenu()
