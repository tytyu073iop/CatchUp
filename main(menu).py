import pygame
import pygame_menu
import game
import Global_variables
import json
##########################
##########################
pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((500, 500))
menu = pygame_menu.Menu('Catch Up!', 500, 500)

def FSChange(state, **kwargs):#Изменение полного экрана
    Global_variables.IsFullScreen = state
    print("switched: Full screen", game.IsFullScreen, state)


def VChange(state, **kwargs):#Изменение V-Sync
    Global_variables.IsVSync = state


def ChangeBot(state, **kwargs):
    game.Bot = state



def changeSpeed(value, *args, **kwargs):#Изменение скорости игры
    print(args, kwargs)
    Global_variables.speed = (value[1] + 1) * 5


def changeVolume(val, *args, **kwargs):#Изменение звука
    print(args, kwargs)
    Global_variables.volume = (val[1] + 1)/10
    pygame.mixer.music.set_volume(game.volume)



############################################Список для скорости игры
lr = []
for i in range (1, 21):
    lr.append(str(i))
############################################Список для громкости звука
ln = []
for i in range (1, 11):
    ln.append(str(i))


menu.add.toggle_switch('Полный экран', False, onchange=FSChange)#Полный экран

#####################

menu.add.toggle_switch('VSync', False, onchange=VChange)#V-Sync

#№№№№№№№№№№№№№№№№

menu.add.toggle_switch('Два - Бот', False, onchange = ChangeBot)#Режим игры

##############################

menu.add.selector('Чуствительность', lr, onchange=changeSpeed, default=0)#Скорость игры

#$$$$$$$$$$$$$$$$$$

menu.add.selector('Звук', ln, onchange=changeVolume, default=8)#Громкость звука

# table = menu.add.table()
# sc = json.load(open('score.json', 'r'))
# table.add_row(['Blue', 'Pink'])
# for i in sc:
#     table.add_row([str(i['Blue']), str(i['Pink'])])
#
pygame.display.set_caption("Догонялки-Убегалки")
#############################
menu.add.button('Играть', game.game, False)
# отвечает за запуск меню
menu.mainloop(surface)
