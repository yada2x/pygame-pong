import pygame
import os

BASE_PATH = "data/images/"

def load_image(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img = pygame.Surface.convert_alpha(img)
    return img