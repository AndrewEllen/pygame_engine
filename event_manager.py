import pygame
from sys import exit

def EventHandler():
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()