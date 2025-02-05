import pygame
from config import *
from sprites import *
import sys

class Game:
        def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
                self.clock = pygame.time.Clock()
                self.running = True

        def new(self):
                self.playing = True

                self.all_sprites = pygame.sprite.LayeredUpdates()
                self.blocks = pygame.sprite.LayeredUpdates()
                self.mob1 = pygame.sprite.LayeredUpdates()

                self.player = Player(self, 1, 2)

        def update(self):
                self.all_sprites.update()

        def draw(self):
                self.screen.fill(BLACK)
                self.all_sprites.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.update()

        def main(self):
                while self.playing:
                        self.events()
                        self.update()
                        self.draw()
                self.running = False

        def game_over(self):

g = Game()
g.intro_screen()
g.new()
while g.running:
        g.main()
        g.game_over()

pygame.quit()
sys.exit()
