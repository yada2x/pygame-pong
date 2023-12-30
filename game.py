import pygame
import sys
import random

from scripts.utils import load_image
from scripts.entities import PhysicsEntity, Ball

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PyPong")

        self.screen = pygame.display.set_mode((800, 497))

        self.clock = pygame.time.Clock()

        self.assets = {
            'ball': load_image('Ball.png'),
            'ballmotion': load_image('BallMotion.png'),
            'board': load_image('Board.png'),
            'computer': load_image('Computer.png'),
            'player': load_image('Player.png'),
            'scorebar': load_image('ScoreBar.png')
        }

        # Entities
        self.player = PhysicsEntity(self, 'player', (750, (self.screen.get_height() - 120 + 47) // 2), (17, 120))
        self.computer = PhysicsEntity(self, 'computer', (50 - 17, (self.screen.get_height() - 120 + 47) // 2), (17, 120))
        self.ball = Ball(self, 'ball', ((self.screen.get_width() - 30) // 2, (self.screen.get_height() - 30 + 47) // 2), (30, 30), random.random() * random.randint(0, 1) * 2 - 1, random.random() * random.randint(0, 1) * 2 - 1, 5, [self.player, self.computer])
        self.movement = [False, False] # [Up, Down] For Player
        self.comp_movement = [False, False] # [Up, Down] For Player

        # UI stuff
        self.player_score = 0
        self.computer_score = 0
        self.timer = 120

    def run(self):
        while True:
            # self.screen.fill((0, 0, 0)) # Clear everything
            self.screen.blit(self.assets['board'], (0, 47))
            self.screen.blit(self.assets['scorebar'], (0, 0))
            self.screen.blit(pygame.transform.flip(self.assets['scorebar'], True, False), (459, 0))

            # Player Code
            self.player.update(self.movement[1] - self.movement[0], 5)
            self.player.render(self.screen)

            # Computer Code
            self.computer.update(self.comp_movement[1] - self.comp_movement[0], 5)
            self.computer.render(self.screen)

            # Ball Code
            self.ball.update()
            self.ball.render(self.screen)
            print(self.ball.speed)
            # Input Checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.comp_movement[0] = True
                    if event.key == pygame.K_s:
                        self.comp_movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.comp_movement[0] = False
                    if event.key == pygame.K_s:
                        self.comp_movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()