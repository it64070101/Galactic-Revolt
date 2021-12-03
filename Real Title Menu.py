import pygame
from pygame.locals import *
import os
import EventDB as edb
import time

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

def mainloop():
    """Main Loop"""
    stars = 1 #จำนวนดาวที่จะไป
    win = True
    while edb.ship['current'] < stars or win == True:
        #edb.bonus_event()
        cards = edb.sector_cards()
        win = edb.choose_card(cards)
        #os.system('cls')
        edb.ship['current']  += 1
    if win == False:
        print("Game Over")
    else:
        print("BOSS STAGE")
        print("Your Power: %d VS %d: Boss Power" %(edb.ship["man"], edb.ship["boss"]))
        if edb.ship["boss"] >= edb.ship["man"]:
            print("===== YOU LOSE ! =====")
        else:
            print("===== YOU WIN ! =====")

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
textcolor=(62, 170, 174)
outlinecolor=(140,104,121)
selectcolor=(255, 170, 94)

# Game Background
bg = pygame.image.load("title.png").convert()
bg_big = pygame.transform.scale(bg, (1024, 768))

# Game Font
font = "PressStart2P.ttf"
font = "ZF#2ndPixelus.ttf"
# Game Framerate
clock = pygame.time.Clock()
FPS=30

def title_draw(selected):
    screen.blit(bg_big, [0, 0])
    title=text("Galactic", font, 200, textcolor)
    title2=text("Revolt !", font, 200, textcolor)
    if selected%2 == 0:
        text_start=text("START <<<", font, 128, selectcolor)
    else:
        text_start = text("START", font, 128, white)
    if selected%2 == 1:
        text_quit=text("QUIT <<<", font, 128, selectcolor)
    else:
        text_quit = text("QUIT", font, 128, white)
    screen.blit(text_start, (580, 400))
    screen.blit(text_quit, (656, 480))

def showstar(starnum):
    bg = pygame.transform.scale(pygame.image.load("Space.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("▮▮▮▮▮▮▯▯▯▯▯▯", font, 48, white), (512, 384))
    pygame.display.update()
    time.sleep(3)
    bg = pygame.transform.scale(pygame.image.load("test.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

# Menu
def menu():
    menu=True
    selected=0
    
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected += 1
                elif event.key==pygame.K_DOWN:
                    selected -= 1
                if event.key==pygame.K_RETURN:
                    if selected%2 == 0: #Start
                        print("Start")
                        screen.fill((0,0,0))
                        #pygame.draw.rect(screen, blue, (200,150,100,50))
                        #edb.ship_hud2(screen, edb.ship)
                        #edb.card("1")
                        eventpress()
                        #eventpress()
                    if selected%2 == 1: #Quit
                        pygame.quit()
                        quit()

        # UI Output
        title_draw(selected)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Galactic Revolt!")

def eventpress():
    eventpress=True
    selected=0

    while eventpress:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected -= 1
                elif event.key==pygame.K_DOWN:
                    selected += 1
                if event.key==pygame.K_RETURN:
                    if selected%5 == 0:
                        print("1")
                    elif selected%5 == 1:
                        print("2")
                    elif selected%5 == 2:
                        print("3")
                    elif selected%5 == 3:
                        print("4")
                    elif selected%5 == 4:
                        print("5")
                    if selected=="quit":
                        pygame.quit()
                        quit()
        edb.card(selected)
        pygame.display.update()
    time.sleep(5)


#Initialize Game
menu()
pygame.quit()
quit()
