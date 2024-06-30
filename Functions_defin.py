from B_P import *
from Global_variables import *
import pygame
from enum import Enum
class TeamMember(Enum):
    blue = 'Blue'
    pink = 'Pink'
def Ghosts_respawn(ghost_b, ghost_p):
    global B_x
    global B_y
    global P_y
    global P_x
    global game_status
#     if sco.score[TeamMember.pink.value] >= 20 or sco.score[TeamMember.blue.value] >= 20:
#         game_status = False
    if IsFullScreen:
        ghost_b.rect.x = 500
        ghost_p.rect.x = 1000
        ghost_b.rect.y = 500
        ghost_p.rect.y = 100
        B_x = 500
        B_y = 500
        P_x = 1000
        P_y = 100
    else:
        ghost_b.rect.x = 100
        ghost_p.rect.x = 600
        ghost_b.rect.y = 100
        ghost_p.rect.y = 100
        B_x = 100
        B_y = 100
        P_x = 600
        P_y = 100
###################
# счётчик очков
def ghost_collide(ghost_b, ghost_p, jud, sco, kick):
    global B_C
    if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color_c == (176, 232, 240):
        jud.increase(TeamMember.blue.value, 5)
        kick.play()
        Ghosts_respawn(ghost_b, ghost_p)
        B_C  = True
    if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color_c == (240, 184, 248):
        jud.increase(TeamMember.pink.value, 5)
        kick.play()
        Ghosts_respawn()
        B_C = False
