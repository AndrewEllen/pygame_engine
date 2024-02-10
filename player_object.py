import pygame
from player_controller import PlayerController

class PlayerObject():
  def __init__(self, username):
    self.username = username
    self.controller = PlayerController()

  def MovePlayer(self, deltaTime):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
      self.controller.UpdatePosition(0, 1, deltaTime)
    if keys[pygame.K_s]:
      self.controller.UpdatePosition(0, -1, deltaTime)
    if keys[pygame.K_d]:
      self.controller.UpdatePosition(1, 0, deltaTime)
    if keys[pygame.K_a]:
      self.controller.UpdatePosition(-1, 0, deltaTime)