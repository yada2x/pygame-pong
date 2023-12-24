import pygame

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

    def update(self, movement, speed):
        self.pos[1] += movement * speed
        entity_rect = self.rect()

        if entity_rect.bottom > self.screen_height:
            self.pos[1] = self.screen_height - self.size[1]
        if entity_rect.top <= 0:
            self.pos[1] = 0

    def render(self, surface: pygame.Surface):
        surface.blit(self.game.assets[self.type], self.pos)

class Player(PhysicsEntity):
    def __init__(self, game, type, pos, size):
        super().__init__(game, type, pos, size)

class Computer(PhysicsEntity):
    def __init__(self, game, type, pos, size):
        super().__init__(game, type, pos, size)

class Ball(PhysicsEntity):
    def __init__(self, game, type, pos, size):
        super().__init__(game, type, pos, size)
