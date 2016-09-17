import time
import sys
import random
import pygame
from pygame.locals import *

#Variables
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
neonYellow = (227, 255, 51)
neonGreen = (51, 255, 233)

pygame.init()

screen = pygame.display.set_mode((1200,600))


def flicker(listy):
    while True:
        for i in range(len(listy)):
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    pygame.quit()

            changeColor(listy[i])


def changeColor(color):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    pygame.time.wait(200)



flicker([black,white,neonYellow])
