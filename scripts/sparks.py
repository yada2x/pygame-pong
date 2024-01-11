import math
import pygame

class Spark:
    def __init__(self, pos, angle, speed, x_dir):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
        self.x_dir = x_dir
    
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed

    def render(self, surface: pygame.Surface, collisions):
        render_points = [
            (self.pos[0] + math.cos(self.angle) * 10, self.pos[1] + math.sin(self.angle)* 10),
            (self.pos[0] + math.cos(self.angle + math.pi) * 10, self.pos[1] + math.sin(self.angle + math.pi) * 10),
            (self.pos[0] + math.cos(self.angle + math.pi) * 10, self.pos[1] + math.sin(self.angle + math.pi) * 10),
            (self.pos[0] + math.cos(self.angle - math.pi) * 10, self.pos[1] + math.sin(self.angle - math.pi) * 10),
        ]
        pygame.draw.polygon(surface, (255, 255, 255), render_points)
    

