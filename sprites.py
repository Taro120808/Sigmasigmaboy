import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
        def __init__(self, game, x, y):

                self.game = game
                self._layer =  PLAYER_LAYER
                self.groups = self.game.all_sprites
                pygame.sprite.Sprite.__init__(self, self.groups)

                self.x = x * TILESIZE
                self.y = y * TILESIZE
                self.HEIGHT = TILESIZE
                self.WIDTH = TILESIZE

                self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
                self.image.fill(RED) #will be changed in a future update

                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        
        def update(self):
                def movement(self):
                        key = pygame.key.get_pressed()
                        if [pygame.K_a]:
                                self.x_change -= Player_Speed
                                self.facing = 'left'
                                
                        if [pygame.K_d]:
                                self.x_change += Player_Speed
                                self.facing = 'right'

                        if [pygame.K_w]:
                                self.y_change -= Player_Speed
                                self.facing = 'up'

                        if [pygame.K_s]:
                                self.y_change += Player_Speed
                                self.facing = 'down'
