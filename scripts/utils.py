import pygame
import os

BASE_PATH = "data/images/"

def load_image(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img = pygame.Surface.convert_alpha(img)
    img.set_colorkey((0, 0, 0))
    return img

def display_text(surface: pygame.Surface, text, font: pygame.Font, colour, x, y):
    img = font.render(text, True, colour)
    surface.blit(img, (x, y))

def update_score(left_score, right_score):
    pass