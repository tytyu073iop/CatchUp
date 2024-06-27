import pygame
import pygame_menu
import game

pygame.init()
surface = pygame.display.set_mode((1000, 1000))
menu = pygame_menu.Menu('Catch Up!', 1000, 1000)
def FSChange(state, **kwargs):
    game.IsFullScreen = state
    print("switched: Full screen", game.IsFullScreen, state)
menu.add.toggle_switch('Полный экран', False, onchange=FSChange)
def VChange(state, **kwargs):
    game.IsVSync = state
menu.add.toggle_switch('VSync', False, onchange=VChange)
pygame.display.set_caption("Догонялки-Убегалки")
menu.add.button('two players', game.game, False)
menu.mainloop(surface)