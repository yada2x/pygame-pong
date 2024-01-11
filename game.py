import pygame
import sys
import random
import math

from scripts.utils import load_image, display_text
from scripts.entities import PhysicsEntity, Ball

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PyPong")

        self.screen = pygame.display.set_mode((800, 657))
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.time_left = 30

        self.assets = {
            'ball': load_image('Ball.png'),
            'board': load_image('Board.png'),
            'computer': load_image('Computer.png'),
            'player': load_image('Player.png'),
            'scorebar': load_image('ScoreBar.png')
        }
        
        self.sfx = {
            'paddle': pygame.mixer.Sound('data/sound/paddle.wav'),
            'wall': pygame.mixer.Sound('data/sound/wall.wav'),
            'start': pygame.mixer.Sound('data/sound/start.wav'),
            'score': pygame.mixer.Sound('data/sound/score.wav')
        }

        self.sfx['paddle'].set_volume(0.2)
        self.sfx['wall'].set_volume(0.2)
        self.sfx['start'].set_volume(0.3)
        self.sfx['score'].set_volume(0.3)

        # Movement
        self.movement = [False, False] # [Up, Down] For Player
        self.comp_movement = [False, False] # [Up, Down] For Player
        self.paddle_speed = 10

        # UI 
        self.player_score = 0
        self.computer_score = 0

    def restart(self):
        self.sfx['start'].play()
        self.player = PhysicsEntity(self, 'player', (750, (self.screen.get_height() - 120 + 47) // 2), (17, 120))
        self.computer = PhysicsEntity(self, 'computer', (50 - 17, (self.screen.get_height() - 120 + 47) // 2), (17, 120))
        self.ball = Ball(self, 'ball', ((self.screen.get_width() - 30) // 2, (self.screen.get_height() - 30 + 47) // 2), (30, 30), random.choice([-1, 1]), random.choice([-1, -0.5, 0.5, 1]), 5, [self.player, self.computer])

    def gameover(self, result):
        font = pygame.font.SysFont("Comic Sans", 40)
        if result == 1:
            display_text(self.screen, "PLAYER WINS", font, (255, 255, 255), self.screen.get_width()//2 - font.size("PLAYER WINS")[0]//2, self.screen.get_height()//2 - 57)
        elif result == 2:
            display_text(self.screen, "COMPUTER WINS", font, (255, 255, 255), self.screen.get_width()//2 - font.size("COMPUTER WINS")[0]//2, self.screen.get_height()//2 - 57)
        elif result == 3:
            display_text(self.screen, "DRAW", font, (255, 255, 255), self.screen.get_width()//2 - font.size("DRAW")[0]//2, self.screen.get_height()//2 - 57)

    def run(self):
        self.restart()
        while True:
            # Rendering assets
            self.screen.fill((0, 0, 0)) # Clear everything
            self.screen.blit(self.assets['board'], (0, 300))
            self.screen.blit(self.assets['board'], (0, 47))
            self.screen.blit(self.assets['scorebar'], (0, 0))
            self.screen.blit(pygame.transform.flip(self.assets['scorebar'], True, False), (459, 0))
            display_text(self.screen, str(self.computer_score), pygame.font.SysFont("Comic Sans", 40), (0, 0, 0), self.screen.get_width()//2 - 150, -5)
            display_text(self.screen, str(self.player_score), pygame.font.SysFont("Comic Sans", 40), (0, 0, 0), self.screen.get_width()//2 + 126, -5)
            display_text(self.screen, str(self.time_left), pygame.font.SysFont("Comic Sans", 40), (255, 255, 255), self.screen.get_width()//2 - (20 if self.time_left >= 10 else 10), -5)

            # Player Code
            self.player.update(self.movement[1] - self.movement[0], self.paddle_speed)
            self.player.render(self.screen)

            # Computer Code
            self.computer.update(self.comp_movement[1] - self.comp_movement[0], self.paddle_speed)
            self.computer.render(self.screen)

            # Ball Code
            collision = self.ball.update()
            self.ball.render(self.screen)
            
            # Collision code
            restart = False

            if collision == 1:
                self.sfx['paddle'].play()
            elif collision == 2:
                self.sfx['wall'].play()
            elif collision == 3:
                self.player_score += 1
                self.sfx['score'].play()
                self.ball.render(self.screen)
                restart = True
            elif collision == 4:
                self.computer_score += 1
                self.sfx['score'].play()
                self.ball.render(self.screen)
                restart = True

            # End-State Code
            if self.time_left <= 0:
                restart = True
                if self.player_score > self.computer_score: 
                    result = 1
                elif self.player_score < self.computer_score:
                    result = 2
                else:
                    result = 3
                self.gameover(result)
                self.player_score = 0
                self.computer_score = 0
                self.time_left = 30

            # Input Checker
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.time_left -= 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        self.restart()
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

            if restart:
                pygame.time.delay(1000)
                self.restart()
                self.time_left += 1

Game().run()