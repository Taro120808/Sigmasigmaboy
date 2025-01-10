import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, game, x, y):

    self.game = game
    player._layer =  PLAYER_LAYER
    self.groups = self.game.all_sprites
    pygame.sprite.SPRITE.__init__(self, self.groups)

    self.x = x * TILESIZE
    self.y = y * TILESIZE
    self.HEIGHT = TILESIZE
    self.WIDTH = TILESIZE

    self.image = pygame.Surface([self.width, self.height])
    self.image.fill(RED) #will be changed in a future update

    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y

  def update(self):
    pass #just a boolean
