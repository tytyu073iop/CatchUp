import pygame
from Chosts_moving import *
from Global_variables import *
class BlueGhost:
    def __init__(self, window, transfotm=None):
        self.index = 0
        self.width = 100
        self.height = 100
        self.move_right = [
    pygame.transform.scale(pygame.image.load('BlueGhost_1.png'),(self.width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1.png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2.png'),(width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2.png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1.png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1.png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2.png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2.png'), (width, height)),

]
        self.move_left = [
    pygame.transform.scale(pygame.image.load('BlueGhost_1(L).png'),(width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1(L).png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2(L).png'),(width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2(L).png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1(L).png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_1(L).png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2(L).png'), (width, height)),
    pygame.transform.scale(pygame.image.load('BlueGhost_2(L).png'), (width, height)),
]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(Blue_ghost_spawn_point_x, Blue_ghost_spawn_point_y))
        self.Faceid = True
        self.lock_x, self.lock_y = window.get_size()

    # this code handles the movement and animation of a game object based on user input from the arrow keys.
    def update(self):
        global B_x
        global B_y
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x > 5:
            moving_left(self)
            B_x -= speed
        if keys_pressed[pygame.K_d] and self.rect.x < self.lock_x - 100:
            moving_right(self)
            B_x += speed
        if keys_pressed[pygame.K_w] and self.rect.y > 5:
            moving_up(self)
            B_y -= speed
        if keys_pressed[pygame.K_s] and self.rect.y < self.lock_y - 100:
            moving_down(self)
            B_y += speed
        if self.index < 39:
            self.index += 1
        else:
            self.index = 0
        if IsFullScreen:
            self.height = 50  # height * 600/y
            self.width = 50  # width * 1000/x
        self.window.blit(self.image, self.rect)
        
class PinkGhost:
    def __init__(self, window, isBot):
        self.index = 0
        self.moving  = 19
        self.move_right = [
        pygame.transform.scale(pygame.image.load('PinkGhost_1.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3.png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3.png'), (width, height)),
]
        self.move_left = [
        pygame.transform.scale(pygame.image.load('PinkGhost_1(L).png'),(width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1(L).png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3(L).png'),(width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3(L).png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1(L).png'),(width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_1(L).png'), (width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3(L).png'),(width, height)),
        pygame.transform.scale(pygame.image.load('PinkGhost_3(L).png'), (width, height)),
]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(Pink_ghost_spawn_point_x,Pink_ghost_spawn_point_y))
        self.Faceid = True
        self.lock_x, self.lock_y = window.get_size()
        self.Bot = isBot


    def update(self):
        global B_x
        global B_y
        global P_x
        global P_y
        global speed
        global B_C
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]
        if self.Bot == False:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT] and self.rect.x > 5:
                moving_left(self)
            if keys_pressed[pygame.K_RIGHT] and self.rect.x < self.lock_x - 100:
                moving_right(self)
            if keys_pressed[pygame.K_UP] and self.rect.y > 5:
                moving_up(self)
            if keys_pressed[pygame.K_DOWN] and self.rect.y < self.lock_y - 100:
                moving_down(self)
            if self.index < 39:
                self.index += 1
            else:
                self.index = 0
        else:###############################
            if B_C:
                if B_x > P_x:
                    if self.rect.x > 5 and self.moving == 19:
                        moving_left(self)
                        P_x -= speed
                    else:
                        if self.moving > 0:
                            self.moving -= 1
                            moving_right(self)
                        else:
                            self.moving = 19
                elif B_x < P_x:
                    if self.rect.x < self.lock_x - 100 and self.moving == 19:
                        moving_right(self)
                    else:
                        if self.moving > 0:
                            self.moving -= 1
                            moving_left(self)
                        else:
                            self.moving = 19
                if B_y < P_y:
                    if self.rect.y < self.lock_y - 100 and self.moving == 19:
                        moving_down(self)
                    else:
                        if self.moving > 0:
                            self.moving -= 1
                            moving_up(self)
                        else:
                            self.moving = 19
                elif B_y > P_y:
                    if self.rect.y > 5 and self.moving == 19:
                        moving_up(self)
                    else:
                        if self.moving > 0:
                            self.moving -= 1
                            moving_down(self)
                        else:
                            self.moving = 19
            else:
                speed /= 1.5
                if B_x > P_x:
                    moving_right(self)
                    P_x += speed
                else:
                    moving_left(self)
                    P_x -= speed
                if B_y > P_y:
                    moving_down(self)
                    P_y += speed
                else:
                    moving_up(self)
                    P_y -= speed
                speed *= 1.5
            if self.index < 39:
                self.index += 1
            else:
                self.index = 0
        self.window.blit(self.image, self.rect)