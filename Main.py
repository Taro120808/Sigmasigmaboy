import pygame
from config import *
from sprites import *
import sys

class Game:
        def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
                self.clock = pygame.time.Clock()
                self.font = pygame.font.Font('League Spartan', 32)
                self.running = True

        def new(self):
                self.playing = True

                self.all_sprites = pygame.sprite.LayeredUpdates()
                self.blocks = pygame.sprite.LayeredUpdates()
                self.mob1 = pygame.sprite.LayeredUpdates()

                self.player = Player(self, 1, 2)
