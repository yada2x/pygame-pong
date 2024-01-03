import pygame
import random

class PhysicsEntity:
    def __init__(self, game, type, pos, size):
        self.game = game
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.type = type
        self.pos = list(pos)
        self.size = size
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, movement=0, speed=0):
        self.pos[1] += movement * speed
        entity_rect = self.rect()

        # Check vertical bounds
        if entity_rect.bottom > self.screen_height:
            self.pos[1] = self.screen_height - self.size[1]
        if entity_rect.top <= 47:
            self.pos[1] = 47

    def render(self, surface: pygame.Surface):
        surface.blit(self.game.assets[self.type], self.pos)

class Ball(PhysicsEntity):
    def __init__(self, game, type, pos, size, x_dir, y_dir, speed, players: list[PhysicsEntity]):
        super().__init__(game, type, pos, size)
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.speed = speed
        self.players = players

    def update(self):
        # Wall Collisions
        wall = False
        paddle = False

        self.pos[0] += self.speed * self.x_dir
        self.pos[1] += self.speed * self.y_dir

        ball_rect = self.rect()
        if ball_rect.bottom > self.screen_height:
            self.pos[1] = self.screen_height - self.size[1]
            self.y_dir *= -1
            wall = True
        if ball_rect.top <= 47:
            self.pos[1] = 47
            self.y_dir *= -1
            wall = True

        # Goal collisions
        if ball_rect.left < 0:
            self.pos[0] = 0
            return 3

        if ball_rect.right >= 805:
            self.pos[0] = self.screen_width - self.size[0]
            return 4

        # Player collisions
        for player in self.players:
            rect = player.rect()
            if ball_rect.colliderect(rect):
                if self.x_dir > 0:
                    self.pos[0] = rect.left - self.size[0]
                else:
                    self.pos[0] = rect.right
                self.x_dir *= -1
                self.speed = min(self.speed + 2, 30)
                paddle = True
        
        if paddle:
            return 1
        if wall:
            return 2
                