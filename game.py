import pygame
import sys

from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PyPong")

        self.screen = pygame.display.set_mode((802, 456))
        # self.display = pygame.Surface((401, 228))

        self.clock = pygame.time.Clock()

        self.movement = [False, False] # [Up, Down]

        self.assets = {
            'ball': load_image('Ball.png'),
            'ballmotion': load_image('BallMotion.png'),
            'board': load_image('Board.png'),
            'computer': load_image('Computer.png'),
            'player': load_image('Player.png'),
            'scorebar': load_image('ScoreBar.png')
        }

    def run(self):
        
        while True:    
            self.screen.blit(self.assets['board'], (0, 0)) # Blits background


            # Input Checker
            for event in pygame.event.get():
                # Quitting
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()