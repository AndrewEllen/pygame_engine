import pygame

class PlayerController():
  def __init__(self):
    #
    self.position = (pygame.display.Info().current_w/2,pygame.display.Info().current_h/2)
    self.cameraPosition = (0,0)

  def UpdatePosition(self, x, y, playerSpeed, deltaTime):

    current_x = self.cameraPosition[0]
    current_y = self.cameraPosition[1]

    self.cameraPosition = (current_x + (x * playerSpeed) * deltaTime, current_y + (y * playerSpeed) * deltaTime)
    if self.cameraPosition[0] < 0:
      self.cameraPosition = (0, self.cameraPosition[1])
    if self.cameraPosition[1] < 0:
      self.cameraPosition = (self.cameraPosition[0], 0)
    if self.cameraPosition[0] > (4096-pygame.display.Info().current_w): #4096 is the resolution of the map png. Taking away the height/width keeps player in boundary
      self.cameraPosition = ((4096-pygame.display.Info().current_w), self.cameraPosition[1])
    if self.cameraPosition[1] > (4096-pygame.display.Info().current_h):
      self.cameraPosition = (self.cameraPosition[0], (4096-pygame.display.Info().current_h))

    #Console log of position
    print(self.cameraPosition)