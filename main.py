import pygame.draw
from pygame import *

window = display.set_mode((1000, 600))
display.set_caption("Догонялки-Убегалки")
background = transform.scale(image.load("Cave_background.png"), (1000, 600))
#Комментарий

# данные о спрайте-картинке
x1 = 100
y1 = 200
x2 = 800
y2 = 300
count_exp = 0
sprite1 = transform.scale(image.load('BlueGhost_1.png'), (100, 100))
sprite2 = transform.scale(image.load('PinkGhost_1.png'), (100, 100))
speed = 10
# игровой цикл
run = True
clock = time.Clock()
FPS = 60
color = (0,0,255)
font.init()
font = font.Font(None,70)
win_b = font.render(
    'BLUE WIN"S ', True, (0,0,255)
)
win_p = font.render(
    'PINCK WIN"S ', True, (250, 192, 203)
)

#счётчик очков
while run:     
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    pygame.draw.circle(background, color, (40, 40), 20)
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()


    if abs(x1 - x2) < 50 and abs(y1 - y2) < 100:
        if color == (0, 0, 255):
            window.blit(win_b,(200,200))
            color = (250, 192, 203)
        else:
            color = (0, 0, 255)
            window.blit(win_p, (200,200))
        x1 = 100
        y1 = 200
        x2 = 800
        y2 = 300
    #if keys_pressed [K_h]:

    if keys_pressed [K_r]:
        x1 = 100
        y1 = 300
        x2 = 300
        y2 = 300
        color = (0, 0, 255)
    if keys_pressed[K_a] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_d] and x1 < 895:
        x1 += speed
    if keys_pressed[K_w] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_s] and y1 < 495:
        y1 += speed

    if keys_pressed[K_LEFT] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_RIGHT] and x2 < 895:
        x2 += speed
    if keys_pressed[K_UP] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_DOWN] and y2 < 495:
        y2 += speed

    display.update()
    clock.tick(FPS)
