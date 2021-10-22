"""Mouse"""
# import
import pygame , sys

# หน้าต่าง
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Mouse")
screen = pygame.display.set_mode((800,800), 0, 40)

img = pygame.image.load('Test2.png').convert()

offset = [0, 0]

clicking = False
right_click = False
middle_click = False

# เชคว่ากดป่าว
while True:

    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    rot = 0
    loc = [mx, my]
    if clicking:
        rot -= 90
    if right_click:
        rot += 90
    if middle_click:
        rot += 180
    screen.blit(pygame.transform.rotate(img, rot), (loc[0] + offset[0], loc[1] + offset[1]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
            if event.button == 3:
                right_click = True
            if event.button == 2:
                middle_click = not middle_click
            if event.button == 4:
                offset[1] -= 10
            if event.button == 5:
                offset[1] += 10
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
            if event.button == 3:
                right_click = False
            if event.button == 2:
                middle_click = False


    pygame.display.update()
    mainClock.tick(60)
