import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, game, x, y)

  self.game = game
  player._layer =  PLAYER_LAYER
  self.groups = self.game.all_sprites
  pygame.sprite.SPRITE.__init__(self, self.groups)

  self.x = x * TILESIZE
  self.y = y * TILESIZE
  self.HEIGHT = TILESIZE
  self.WIDTH = TILESIZE

