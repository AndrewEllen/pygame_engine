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

def main_loop():
  while True:
    # 60 is the fps
    deltaTime = clock.tick(60)/1000
    
    EventHandler()
    player.MovePlayer(deltaTime)
    
    print(player.controller.position)


main_loop()