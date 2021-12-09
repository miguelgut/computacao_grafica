import pygame
from pygame.locals import *
import os


pygame.init()
win = pygame.display.set_mode((1420, 880))
# win_photo = pygame.display.set_mode((400, 480))
pygame.display.set_caption("Moving spyder")

run = True

black = (0, 0, 0)
peach = (255, 175, 128)
green = (0, 104, 55)
white = (255, 255, 255)

speed = 4.5

def definePerna(tamanho, cor1, cor2, angulo, pos, npos):
    perna = pygame.Surface(tamanho)
    perna.fill(cor1)
    perna.set_colorkey(cor2)
    pygame.draw.ellipse(perna, cor1, (10, 0, 50, 7))

    target = pygame.Vector2(npos)

    return win.blit(pygame.transform.rotate(perna, angulo), pos), perna

def defineCorpo(cor, posicao, tamanho, perna_surf):
    corpo_rect = pygame.draw.circle(win, cor, posicao, tamanho)
    corpo = pygame.Surface(corpo_rect.size)
    corpo.fill(cor)
    corpo.set_colorkey(green)

    return perna_surf.blit(corpo, corpo_rect)

pos = [
[(100, 100),(124, 140),(100, 100)],
[(130, 140),(140, 160),(130, 140)],
[(110, 240),(110, 240),(100, 240)],
[(76, 240),(91, 240),(82, 240)],
[(122, 260),(117, 260),(112, 260)],
[(87, 260),(101, 282),(77, 260)],
[(130, 290),(130, 290),(120, 290)],
[(79, 290),(108, 290),(113, 300)],
[(245, 100),(245, 100),(238, 140)],
[(222, 135),(222, 135),(225, 160)],
[(220, 240),(220, 240),(220, 210)],
[(262, 240),(267, 240),(250, 210)],
[(200, 260),(200, 260),(230, 260)],
[(253, 260),(263, 260),(265, 267)],
[(220, 290),(220, 290),(230, 290)],
[(245, 290),(245, 305),(255, 290)],
]

ang = [
[306,307,306 ],
[105,105,105 ],
[160,140,165],
[60,40,70],
[160,200,165],
[60,70,60],
[160,180,21],
[60,75,85,],
[54,54,54 ],
[255,255,255 ],
[-160,-170,40],
[-60,-60,140],
[-160,-160,350],
[-60,-50,290],
[-160,-210,0],
[-60,-85,280],
]

tam = [
[(50 ,5),(25 ,5),(50 ,5)],
[(100 ,5),(50 ,5),(100 ,5)],
[(50, 5),(40, 5),(50, 5)],
[(70, 5),(25, 5),(45, 5)],
[(62, 5),(70, 5),(70, 5)],
[(70, 5),(50, 5),(65, 5)],
[(31, 5),(31, 5),(30, 5)],
[(101, 5),(70, 5),(90, 5)],
[(50 ,5),(50 ,5),(25 ,5)],
[(100 ,5),(100 ,5),(50 ,5)],
[(50, 5),(50, 5),(40, 5)],
[(70, 5),(45, 5),(25, 5)],
[(62, 5),(70, 5),(40, 5)],
[(70, 5),(40, 5),(50, 5)],
[(30, 5),(30, 5),(31, 5)],
[(100, 5),(90, 5),(80, 5)],
]

posicao = [
(190, 220),
(190, 270),
]

tamanho = [
40,
50,
]

for j in range(3):
    win.fill((0,0,0))
    for i in range(len(tam)):
        pernas, perna_s = definePerna(tam[i][j], white, green, ang[i][j] , pos[i][j], 0)

    for i in range(len(tamanho)):
        corpos = defineCorpo(white, posicao[i], tamanho[i], perna_s)

    print(win)
    pygame.image.save(win, 'p%d.png'%j)

j = 0
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            npos = pygame.mouse.get_pos()

            if j < 2:
                j+=1
            else:
                j = 0

            win.fill((0,0,0))

            image_raw = pygame.image.load('p%d.png'%j)
            image = image_raw.convert_alpha()

            rect = image.get_rect()

            new_pos = npos[0]-(rect[0]+rect[0]/4), npos[1]-(rect[1]+rect[1]/2)

            for i in range(2):
                rect.move_ip(npos[0]-(rect[0]+rect[0]/4), npos[1]-(rect[1]+rect[1]/2))

            for i in range(2):
                win.blit(image, rect)

            pygame.display.flip()

        pygame.display.update()

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
  
pygame.quit()
