import pygame
from pygame.locals import Rect
from player_controller import PlayerController

class PlayerObject():
  def __init__(self, username):
    self.username = username
    self.controller = PlayerController()
    # 
    self.playerWidth = 60
    self.playerHeight = 100
    self.playerModel = Rect(self.controller.position[0], self.controller.position[1], self.playerWidth, self.playerHeight)
    self.playerColour = (255,0,0)
    self.playerSpeed = 100

  def MovePlayer(self, deltaTime):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
      self.controller.UpdatePosition(0, 1, self.playerSpeed, deltaTime)
    if keys[pygame.K_w]:
      self.controller.UpdatePosition(0, -1, self.playerSpeed, deltaTime)
    if keys[pygame.K_d]:
      self.controller.UpdatePosition(1, 0, self.playerSpeed, deltaTime)
    if keys[pygame.K_a]:
      self.controller.UpdatePosition(-1, 0, self.playerSpeed, deltaTime)

  def renderPlayer(self, screen, colour, model):
    self.playerModel = Rect(self.controller.position[0], self.controller.position[1], self.playerWidth, self.playerHeight)
    pygame.draw.rect(screen, colour, model)