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
        # Check new pos before updating?
        self.pos[0] += self.speed * self.x_dir
        self.pos[1] += self.speed * self.y_dir
        ball_rect = self.rect()
        if ball_rect.bottom > self.screen_height:
            self.pos[1] = self.screen_height - self.size[1]
            self.y_dir *= -1
        if ball_rect.top <= 47:
            self.pos[1] = 47
            self.y_dir *= -1

        # Temporary
        if ball_rect.left < 0:
            self.pos[0] = 0
            self.x_dir *= -1
        if ball_rect.right >= 800:
            self.pos[0] = 800 - self.size[0]
            self.x_dir *= -1

        # Player collisions
        for player in self.players:
            rect = player.rect()
            if ball_rect.colliderect(rect):
                # if ball_rect.bottom >= rect.top and ball_rect.right > rect.left:
                #     if self.y_dir > 0:
                #         self.y_dir *= -1
                #     self.pos[1] = rect.top - self.size[1]
                #     print("TOP")

                # elif ball_rect.top <= rect.bottom and ball_rect.right > rect.left:
                #     if self.y_dir < 0:
                #         self.y_dir *= -1
                #     self.pos[1] = rect.bottom
                #     print("BOT")
                self.x_dir *= -1
                self.y_dir = random.random() * self.y_dir
                self.speed += 1