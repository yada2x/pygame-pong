import pygame

class PhysicsEntity:
    def __init__(self, game, type, pos, size):
        self.game = game
        self.type = type
        self.pos = list(pos)
        self.size = size
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, movement, speed):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.pos[1] += movement * speed
        # FIGURE OUT TOP AND BOTTOM COLLISIONS 

    def render(self, surface: pygame.Surface):
        surface.blit(self.game.assets[self.type], self.pos)