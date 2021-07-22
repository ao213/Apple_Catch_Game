from controller.gamecontroller import GameController
import pygame
import pygame.image
import pygame.display
from setting import *


class Game:
    def __init__(self):
        self.fps_clock = pygame.time.Clock()
        pygame.init()
        self.controller = GameController()
        self.run()

    def run(self):

        while 1:
            pygame.display.update()

            self.controller.display_base_screen()

            self.controller.apple_process()

            self.controller.display_objects()

            self.controller.display_hud()

            if self.controller.check_game_over():
                print("game over")
                # break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    self.controller.set_player_postion(x)
