import pygame
import math

from event_manager import EventHandler
from player_object import PlayerObject

pygame.init()

#Create pygame window

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Engine Example")
clock = pygame.time.Clock()

background = pygame.image.load("map.png")
player = PlayerObject("Player")

def playerHandler(deltaTime):
  player.MovePlayer(deltaTime)
  player.renderPlayer(screen)



def main_loop():
  while True:
    # resetting the screen each loop
    screen.blit(background, (0, 0))
    # 60 is the fps
    deltaTime = clock.tick(60)/1000
    
    EventHandler()
    playerHandler(deltaTime)


main_loop()