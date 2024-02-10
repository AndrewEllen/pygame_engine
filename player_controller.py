import pygame

class PlayerController():
  def __init__(self):
    #
    self.position = (pygame.display.Info().current_w/2,pygame.display.Info().current_h/2)

  def UpdatePosition(self, x, y, playerSpeed, deltaTime):

    current_x = self.position[0]
    current_y = self.position[1]

    self.position = (current_x + (x * playerSpeed) * deltaTime, current_y + (y * playerSpeed) * deltaTime)

    #Console log of position
    print(self.position)