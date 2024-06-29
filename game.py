import pygame.draw
import pygame
import pygame_menu
import pygame_menu.controls as ctrl

speed = 2
volume = 1.0
pygame.mixer.init()
pygame.mixer.music.load('Смешарики - Тема погони.mp3')
pygame.mixer.music.play(1)
pygame.font.init()
font = pygame.font.Font(None,50)
clock = pygame.time.Clock()
FPS = 45
run = True
finish = False
width = 100
height = 100
score = [0,0]
IsFullScreen = False
IsVSync = False
Resolution = (1000, 600)
Blue_ghost_spawn_point_x = 100
Pink_ghost_spawn_point_x = 600
Blue_ghost_spawn_point_y = 100
Pink_ghost_spawn_point_y = 100
color = (0,0,255)
game_status = True

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
        self.rect = self.image.get_rect(center=(Blue_ghost_spawn_point_x,Blue_ghost_spawn_point_y))
        self.Faceid = True
        self.lock_x, self.lock_y = window.get_size()

    # this code handles the movement and animation of a game object based on user input from the arrow keys.
    def update(self):
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= speed + 3
            self.image = self.move_left[self.index // 5]
            self.Faceid = False
        if keys_pressed[pygame.K_d] and self.rect.x < self.lock_x - 100:
            self.rect.x += speed + 3
            self.image = self.move_right[self.index // 5]
            self.Faceid = True
        if keys_pressed[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= speed + 3
        if keys_pressed[pygame.K_s] and self.rect.y < self.lock_y - 100:
            self.rect.y += speed + 3
        if self.index < 39:
            self.index += 1
        else:
            self.index = 0
        if IsFullScreen:
            self.height = 50  # height * 600/y
            self.width = 50  # width * 1000/x
        self.window.blit(self.image, self.rect)

# same as previous
class PinkGhost:
    def __init__(self, window):
        self.index = 0
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



    def update(self,ghost_b, color_c):
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]

        '''
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
            self.image = self.move_left[self.index // 5]
            self.Faceid = False
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < self.lock_x - 100:
            self.rect.x += speed
            self.image = self.move_right[self.index // 5]
            self.Faceid = True
        if keys_pressed[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[pygame.K_DOWN] and self.rect.y < self.lock_y - 100:
            self.rect.y += speed
        '''
        if color_c == (240, 184, 248):
            if self.rect.x != ghost_b.rect.x or self.rect.y != ghost_b.rect.y:
                '''Условие, если координата x игрока не равна координате x курсора 
                или координата y игрока не равна координате y курсора'''
                if self.rect.x != ghost_b.rect.x or self.rect.y != ghost_b.rect.y:

                    '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                    (вверх, вниз, влево, вправо) сделать анимацию'''

                    if self.rect.x >= ghost_b.rect.x and self.rect.y >= ghost_b.rect.y:

                        '''Условие, если координата x игрока больше координаты x курсора 
                    или координата y игрока больше координаты y курсора'''

                        self.image = self.move_left[self.index // 5]  # Отрисовываем анимацию перемещения влево
                        self.rect.x -= speed  # Перемещаем персонажа влево
                        self.rect.y -= speed  # И одновременно перемещаем его вверх

                    elif self.rect.x < ghost_b.rect.x and self.rect.y < ghost_b.rect.y:
                        self.image = self.move_right[self.index // 5]  # Отрисовываем анимацию перемещения вправо
                        self.rect.x += speed  # Перемещаем персонажа вправо
                        self.rect.y += speed  # И одновременно перемещаем его вниз

                    elif self.rect.x < ghost_b.rect.x and self.rect.y > ghost_b.rect.y:
                        self.image = self.move_right[self.index // 5]
                        self.rect.x += speed  # Перемещаем персонажа вправо
                        self.rect.y -= speed  # И одновременно перемещаем его вверх

                    elif self.rect.x >= ghost_b.rect.x and self.rect.y <= ghost_b.rect.y:
                        self.image = self.move_left[self.index // 5]
                        self.rect.x -= speed  # Перемещаем персонажа влево
                        self.rect.y += speed  # И одновременно перемещаем его вниз

                elif self.rect.y != ghost_b.rect.y:
                    if self.rect.y < ghost_b.rect.y:
                        self.rect.y += speed  # Перемещаем персонажа вниз
                    elif self.rect.y > ghost_b.rect.y:
                        self.rect.y -= speed  # Перемещаем персонажа вверх
                elif self.rect.x != ghost_b.rect.x:
                    if self.rect.x < ghost_b.rect.x:
                        self.rect.x += speed  # Перемещаем персонажа вправо
                        self.image = self.move_right[self.index // 5] # Отрисовываем анимацию перемещения вправо
                    elif self.rect.x> ghost_b.rect.x:
                        self.rect.x -= speed  # Перемещаем персонажа влево
                        self.image = self.move_left[self.index // 5]  # Отрисовываем анимацию перемещения влево
        else:
            if (self.rect.x != ghost_b.rect.x or self.rect.y != ghost_b.rect.y) and self.rect.x > 5 and self.rect.x < self.lock_x - 100 and self.rect.y > 5 and self.rect.y < self.lock_y - 100:
                '''Условие, если координата x игрока не равна координате x курсора 
                или координата y игрока не равна координате y курсора'''
                if self.rect.x != ghost_b.rect.x or self.rect.y != ghost_b.rect.y:

                    '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                    (вверх, вниз, влево, вправо) сделать анимацию'''

                    if self.rect.x >= ghost_b.rect.x and self.rect.y >= ghost_b.rect.y:

                        '''Условие, если координата x игрока больше координаты x курсора 
                    или координата y игрока больше координаты y курсора'''

                        self.image = self.move_left[self.index // 5]  # Отрисовываем анимацию перемещения влево
                        self.rect.x += speed  # Перемещаем персонажа влево
                        self.rect.y += speed  # И одновременно перемещаем его вверх

                    elif self.rect.x < ghost_b.rect.x and self.rect.y < ghost_b.rect.y:
                        self.image = self.move_right[self.index // 5]  # Отрисовываем анимацию перемещения вправо
                        self.rect.x -= speed  # Перемещаем персонажа вправо
                        self.rect.y -= speed  # И одновременно перемещаем его вниз

                    elif self.rect.x < ghost_b.rect.x and self.rect.y > ghost_b.rect.y:
                        self.image = self.move_right[self.index // 5]
                        self.rect.x -= speed  # Перемещаем персонажа вправо
                        self.rect.y += speed  # И одновременно перемещаем его вверх

                    elif self.rect.x >= ghost_b.rect.x and self.rect.y <= ghost_b.rect.y:
                        self.image = self.move_left[self.index // 5]
                        self.rect.x += speed  # Перемещаем персонажа влево
                        self.rect.y -= speed  # И одновременно перемещаем его вниз

                elif self.rect.y != ghost_b.rect.y:
                    if self.rect.y < ghost_b.rect.y:
                        self.rect.y -= speed  # Перемещаем персонажа вниз
                    elif self.rect.y > ghost_b.rect.y:
                        self.rect.y += speed  # Перемещаем персонажа вверх
                elif self.rect.x != ghost_b.rect.x:
                    if self.rect.x < ghost_b.rect.x:
                        self.rect.x -= speed  # Перемещаем персонажа вправо
                        self.image = self.move_right[self.index // 5]  # Отрисовываем анимацию перемещения вправо
                    elif self.rect.x > ghost_b.rect.x:
                        self.rect.x += speed  # Перемещаем персонажа влево
                        self.image = self.move_left[self.index // 5]  # Отрисовываем анимацию перемещения влево

        if self.index < 39:
            self.index += 1
        else:
            self.index = 0
        self.window.blit(self.image, self.rect)

# starts from menu
def game(IsAI):
    pygame.mixer.music.set_volume(volume)
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
    ghost_p = PinkGhost(window)
    kick = pygame.mixer.Sound('for-karl_-made-with-Voicemod.ogg')
    kick.set_volume(volume)
    color_c = (176,232,240)

    # счётчик очков
    def ghost_collide():
        if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color_c == (176, 232, 240):
            score[0] += 5
            kick.play()
            Ghosts_respawn()
        if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color_c == (240, 184, 248):
            score[1] += 5
            kick.play()
            Ghosts_respawn()

    def Ghosts_respawn():
        global game_status
        if score[1] >= 20 or score[0] >= 20:
            game_status = False
        if IsFullScreen:
            ghost_b.rect.x = 500
            ghost_p.rect.x = 1000
            ghost_b.rect.y = 500
            ghost_p.rect.y = 100
        else:
            ghost_b.rect.x = 100
            ghost_p.rect.x = 600
            ghost_b.rect.y = 100
            ghost_p.rect.y = 100
        
    Ghosts_respawn()
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
                    run = False
                if e.type == pygame.USEREVENT and color_c == (176, 232, 240):
                    score[1] += 1
                if color_c == (240, 184, 248) and e.type == pygame.USEREVENT:
                    score[0] += 1
                if e.type == pygame.KEYDOWN:
                    global game_status
                    if game_status == False:
                        game_status = True
                        score[1] = 0
                        score[0] = 0
            pygame.draw.circle(background, color_c, (40, 40), 20)
            if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85:
                if color_c == (176, 232, 240):
                    color_c = (240, 184, 248)
                else:
                    color_c = (176, 232, 240)
            if game_status == True:
                counter = font.render(
                    str('blue count') + ' ' + str(score[0]) + ':' + str(score[1]) + ' ' + str('pink count'), True,
                    (255, 255, 255))
                window.blit(background, (0, 0))
                ghost_collide()
                window.blit(counter, (counter_location_x, counter_location_y))
                ghost_b.update()
                ghost_p.update(ghost_b, color_c)
            if game_status == False:
                if score[0] >= 20:
                    winner_b = font.render('Blue Wins', True, (176, 232, 240))
                    window.blit(winner_b, (winner_location_x, winner_location_y))
                elif score[1] >= 20:
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