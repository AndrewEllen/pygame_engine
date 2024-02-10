import pygame

class PlayerController():
  def __init__(self):
    self.position = (0,0)

  def UpdatePosition(self, x, y, deltaTime):

    current_x = self.position[0]
    current_y = self.position[1]

    self.position = (current_x + x * deltaTime, current_y + y * deltaTime)