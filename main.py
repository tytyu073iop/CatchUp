from pygame import *

font.init()
font = font.Font(None,50)
window = display.set_mode((1000, 600))
display.set_caption("Догонялки-Убегалки")
background = transform.scale(image.load("background.png"), (1000, 600))
clock = time.Clock()
FPS = 60
run = True
finish = False
width = 100
height = 100
score = [0,0]

class BlueGhost:
    def __init__(self, window, transfotm=None):
        self.index = 0
        self.move_right = [
    transform.scale(image.load('BlueGhost_1.png'),(width, height)),
    transform.scale(image.load('BlueGhost_2.png'),(width, height)),
    transform.scale(image.load('BlueGhost_3.png'),(width, height)),
    transform.scale(image.load('BlueGhost_1.png'),(width, height)),
    transform.scale(image.load('BlueGhost_2.png'),(width, height)),
    transform.scale(image.load('BlueGhost_3.png'),(width, height))
]
        self.move_left = [
    transform.scale(image.load('BlueGhost_1(L).png'),(width, height)),
    transform.scale(image.load('BlueGhost_2(L).png'),(width, height)),
    transform.scale(image.load('BlueGhost_3(L).png'),(width, height)),
    transform.scale(image.load('BlueGhost_1(L).png'), (width, height)),
    transform.scale(image.load('BlueGhost_2(L).png'), (width, height)),
    transform.scale(image.load('BlueGhost_3(L).png'), (width, height))
]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(100,100))
        self.speed = 5
        self.Faceid = True

    def update(self):
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.image = self.move_left[self.index // 5]
            self.Faceid = False
        if keys_pressed[K_d] and self.rect.x < 895:
            self.rect.x += self.speed
            self.image = self.move_right[self.index // 5]
            self.Faceid = True
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
        if self.index < 25:
            self.index += 1
        else:
            self.index = 0
        self.window.blit(self.image, self.rect)

class PinkGhost:
    def __init__(self, window):
        self.index = 0
        self.move_right = [
        transform.scale(image.load('PinkGhost_1.png'), (width, height)),
        transform.scale(image.load('PinkGhost_2.png'), (width, height)),
        transform.scale(image.load('PinkGhost_3.png'), (width, height)),
        transform.scale(image.load('PinkGhost_1.png'), (width, height)),
        transform.scale(image.load('PinkGhost_2.png'), (width, height)),
        transform.scale(image.load('PinkGhost_3.png'), (width, height))
]
        self.move_left = [
        transform.scale(image.load('PinkGhost_1(L).png'),(width, height)),
        transform.scale(image.load('PinkGhost_2(L).png'),(width, height)),
        transform.scale(image.load('PinkGhost_3(L).png'),(width, height)),
        transform.scale(image.load('PinkGhost_1(L).png'), (width, height)),
        transform.scale(image.load('PinkGhost_2(L).png'), (width, height)),
        transform.scale(image.load('PinkGhost_3(L).png'), (width, height))
]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(600,100))
        self.speed = 5
        self.Faceid = True

    def update(self):
        if self.Faceid:
            self.image = self.move_right[self.index // 5]
        else:
            self.image = self.move_left[self.index // 5]
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.image = self.move_left[self.index // 5]
            self.Faceid = False
        if keys_pressed[K_RIGHT] and self.rect.x < 895:
            self.rect.x += self.speed
            self.image = self.move_right[self.index // 5]
            self.Faceid = True
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
        if self.index < 25:
            self.index += 1
        else:
            self.index = 0
        self.window.blit(self.image, self.rect)


ghost_b = BlueGhost(window)
ghost_p = PinkGhost(window)

color = (176,232,240)
def ghost_collide():
    if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color == (176, 232, 240):
        score[0] += 1
        Ghosts_respawn()
    if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85 and color == (240, 184, 248):
        score[1] += 1
        Ghosts_respawn()

def Ghosts_respawn():
    ghost_b.rect.x = 100
    ghost_p.rect.x = 600
    ghost_b.rect.y = 100
    ghost_p.rect.y = 100
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    draw.circle(background, color, (40, 40), 20)
    if abs(ghost_b.rect.x - ghost_p.rect.x) < 50 and abs(ghost_b.rect.y - ghost_p.rect.y) < 85:
        if color == (176, 232, 240):
            color = (240, 184, 248)
        else:
            color = (176, 232, 240)
    win = font.render(str('blue count') + ' ' + str(score[0]) + ':' + str(score[1]) + ' ' + str('pink count'), True,(255, 255, 255))
    window.blit(background, (0,0))
    ghost_collide()
    window.blit(win,(500,500))
    ghost_b.update()
    ghost_p.update()
    display.update()
    clock.tick(FPS)

