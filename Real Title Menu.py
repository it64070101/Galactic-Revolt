import pygame
from pygame.locals import *
import os
import Galavolt as gv

# Install Pygame
pygame.init()

# Game Aplication Center
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Resolution
screen_width=1024
screen_height=768
screen=pygame.display.set_mode((screen_width, screen_height))

# Text format for render
def text(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
darkmagenta=(139,0,139)
purple=(98,24,245)

# Game Background
bg = pygame.image.load("Space.png").convert()
bg_big = pygame.transform.scale(bg, (1024, 768))

# Game Font
font = "PressStart2P.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Menu
def menu():
    menu=True
    selected="start"
    
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                        gv.mainloop()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # UI Output
        screen.blit(bg_big, [0, 0])
        title=text("Galactic", font, 48, white)
        title_outline=text("Galactic", font, 48, black)
        title2=text("Revolt", font, 48, white)
        title2_outline=text("Revolt", font, 48, black)
        if selected=="start":
            text_start=text("START", font, 32, red)
        else:
            text_start = text("START", font, 32, white)
        if selected=="quit":
            text_quit=text("QUIT", font, 32, red)
        else:
            text_quit = text("QUIT", font, 32, white)
        
        # Text Output
        screen.blit(title_outline, (27, 77))
        screen.blit(title_outline, (27, 83))
        screen.blit(title_outline, (21, 77))
        screen.blit(title_outline, (21, 83))
        screen.blit(title, (24, 80))
        screen.blit(title2_outline, (21, 143))
        screen.blit(title2_outline, (21, 137))
        screen.blit(title2_outline, (27, 143))
        screen.blit(title2_outline, (27, 137))
        screen.blit(title2, (24, 140))
        screen.blit(text_start, (60, 300))
        screen.blit(text_quit, (60, 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Galactic Revolt - Demo")

#Initialize Game
menu()
pygame.quit()
quit()
