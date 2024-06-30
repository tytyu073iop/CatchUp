import pygame.draw
import pygame
import pygame_menu
import pygame_menu.controls as ctrl
import judge
import score
import sys
import Sounds
from enum import Enum
from Chosts_moving import *
from Functions_defin import *
import Global_variables
from B_P import *
###################
    
###################


#
Bot = False#Режим бота
#
# pygame.mixer.init()
# pygame.mixer.music.load('Смешарики - Тема погони.mp3')
# pygame.mixer.music.play(1)
Sounds.set_sound('Смешарики - Тема погони.mp3')
pygame.font.init()
font = pygame.font.Font(None,50)
clock = pygame.time.Clock()




# same as previous


# starts from menu
def game(IsAI):
    sco = score.Score((TeamMember.blue.value, TeamMember.pink.value), 'score.json')
    jud = judge.Judge(sco)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    global Resolution
    if IsFullScreen:
        Resolution = pygame.display.get_desktop_sizes()[0]
    flags = 0
    if IsFullScreen:
        flags |= pygame.FULLSCREEN
    window = pygame.display.set_mode(Resolution, flags, vsync=int(IsVSync))
    background = pygame.transform.scale(pygame.image.load("Cave_background.png"), Resolution)

    # предигровая настройка
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    pygame.font.init()
    font = pygame.font.Font(None,50)
    win_b = font.render(
        'BLUE WIN"S ', True, (0,0,255)
    )
    win_p = font.render(
        'PINCK WIN"S ', True, (250, 192, 203)
    )

    ghost_b = BlueGhost(window)
    ghost_p = PinkGhost(window, Bot)
    kick = pygame.mixer.Sound('for-karl_-made-with-Voicemod.ogg')
    kick.set_volume(volume)
    Ghosts_respawn(ghost_b, ghost_p)
    counter_location_x = 300
    counter_location_y = 20
    winner_location_x = 300
    winner_location_y = 300
    if IsFullScreen:
        counter_location_x = 750
        winner_location_x = 750
    milisecond = 5000
    pygame.time.set_timer(pygame.USEREVENT, milisecond)

    #menu config
    def continue_button():
        nonlocal menu
        global run
        global color_c
        run = True
        menu.disable()
        print('continue')
    menu = pygame_menu.Menu('Pause', Resolution[0], Resolution[1])
    menu.disable()
    menu.add.button('continue', continue_button)
    menu.add.button('Exit', pygame_menu.events.EXIT)

    # game cycle
    while True:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            menu.enable()
            menu.mainloop(window)
            print('pressed',menu.is_enabled())
            run = not menu.is_enabled()

        if run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                    run = False
                if e.type == pygame.USEREVENT and Global_variables.color_c == (176, 232, 240):
                    jud.increase(TeamMember.pink.value, 1)
                if Global_variables.color_c == (240, 184, 248) and e.type == pygame.USEREVENT:
                    jud.increase(TeamMember.blue.value, 1)
                if e.type == pygame.KEYDOWN:
                    global game_status
                    if game_status == False:
                        sco.save()
                        sco.saveToFile()
                        game_status = True
                        sco.score[TeamMember.blue.value] = 0
                        sco.score[TeamMember.pink.value] = 0
            pygame.draw.circle(background, Global_variables.color_c, (40, 40), 20)
            if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85:
                if Global_variables.color_c == (176, 232, 240):
                    Global_variables.color_c = (240, 184, 248)
                else:
                    Global_variables.color_c = (176, 232, 240)
            if game_status == True:
                counter = font.render(
                    str('blue count') + ' ' + str(sco.score[TeamMember.blue.value]) + ':' + str(sco.score[TeamMember.pink.value]) + ' ' + str('pink count'), True,
                    (255, 255, 255))
                window.blit(background, (0, 0))
                ghost_collide(ghost_b, ghost_p, jud, sco, kick)
                window.blit(counter, (counter_location_x, counter_location_y))
                ghost_b.update()
                ghost_p.update()
            if game_status == False:
                if sco.score[TeamMember.blue.value] >= 20:
                    winner_b = font.render('Blue Wins', True, (176, 232, 240))
                    window.blit(winner_b, (winner_location_x, winner_location_y))
                elif sco.score[TeamMember.pink.value] >= 20:
                    winner_p = font.render('Pink Wins', True, (240, 184, 248))
                    window.blit(winner_p, (winner_location_x, winner_location_y))
        if menu.is_enabled():
            menu.update(pygame.event.get())
            menu.draw(window)
            # print('menu enabled')
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    exit()