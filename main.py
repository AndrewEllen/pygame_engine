import pygame
import math

from event_manager import EventHandler
from player_object import PlayerObject

pygame.init()

#Create pygame window

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Engine Example")
clock = pygame.time.Clock()

player = PlayerObject("Player")

def playerHandler(deltaTime):
  player.MovePlayer(deltaTime)
  player.renderPlayer(screen, player.playerColour, player.playerModel)



def main_loop():
  while True:
    # resetting the screen each loop
    screen.fill((0,0,0))
    # 60 is the fps
    deltaTime = clock.tick(60)/1000
    
    EventHandler()
    playerHandler(deltaTime)

    
    print(player.controller.position)

    #Flip updates the whole screen, you could use update which allows only a portion to update with given arguments
    pygame.display.flip()


main_loop()