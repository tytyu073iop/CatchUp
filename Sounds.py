import pygame
def set_sound( name):
    pygame.mixer.init()
    pygame.mixer.music.load(name)