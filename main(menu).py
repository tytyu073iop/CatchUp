import pygame
import pygame_menu
import game

pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((1000, 1000))
menu = pygame_menu.Menu('Catch Up!', 1000, 1000)


def FSChange(state, **kwargs):
    game.IsFullScreen = state
    print("switched: Full screen", game.IsFullScreen, state)


menu.add.toggle_switch('Полный экран', False, onchange=FSChange)


def VChange(state, **kwargs):
    game.IsVSync = state


menu.add.toggle_switch('VSync', False, onchange=VChange)


def changeSpeed(value, *args, **kwargs):
    print(args, kwargs)
    game.speed = (value[1] + 1) * 5

lr = []
for i in range (1, 21):
    lr.append(str(i))
menu.add.selector('Чуствительность', lr, onchange=changeSpeed, default=0)

def changeVolume(val, *args, **kwargs):
    print(args, kwargs)
    game.volume = (val[1] + 1)/10
    pygame.mixer.music.set_volume(game.volume)

ln = []
for i in range (1, 11):
    ln.append(str(i))
menu.add.selector('Звук', ln, onchange=changeVolume, default=8)
pygame.display.set_caption("Догонялки-Убегалки")
menu.add.button('two players', game.game, False)
# отвечает за запуск меню
menu.mainloop(surface)
