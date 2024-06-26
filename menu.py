import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1000, 1000))
menu = pygame_menu.Menu('Catch Up!', 600, 400)
def func():
    print("menu")

menu.add.button('two players', func)
menu.mainloop(surface)