import pygame
import pygame_menu
import main

pygame.init()
surface = pygame.display.set_mode((1000, 1000))
menu = pygame_menu.Menu('Catch Up!', 1000, 1000)
menu.add.button('two players', main.game, False)
menu.mainloop(surface)