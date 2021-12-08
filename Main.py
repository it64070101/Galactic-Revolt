import pygame
from pygame.locals import *
import os

from pygame.mixer import Sound
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

def play_sound(sound):
    my_sound = pygame.mixer.Sound(sound)
    my_sound.set_volume(0.5)
    my_sound.play()
def play_music(music):
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

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
bg = pygame.image.load("Images/title.png").convert()
bg_big = pygame.transform.scale(bg, (1024, 768))

# Game Font
font = "PressStart2P.ttf"
font = "Fonts/ZF#2ndPixelus.ttf"
# Game Framerate
clock = pygame.time.Clock()
FPS=30

def title_draw(selected):
    screen.blit(bg_big, [0, 0])
    title=text("Galactic", font, 200, textcolor)
    title2=text("Revolt !", font, 200, textcolor)
    if selected%3 == 0:
        text_start=text("START <<<", font, 100, selectcolor)
    else:
        text_start = text("START", font, 100, white)
    if selected%3 == 1:
        text_quit=text("QUIT <<<", font, 100, selectcolor)
    else:
        text_quit = text("QUIT", font, 100, white)
    if selected%3 == 2:
        text_htp=text("How to play <<<", font, 100, selectcolor)
    else:
        text_htp = text("How to play", font, 100, white)
    screen.blit(text_start, (480, 400))
    screen.blit(text_htp, (480, 480))
    screen.blit(text_quit, (480, 560))

def showstar():
    bg = pygame.transform.scale(pygame.image.load("Images/Space.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("▮▮▮▮▮▮▯▯▯▯▯▯", font, 48, white), (512, 384))
    pygame.display.update()
    time.sleep(3)
    bg = pygame.transform.scale(pygame.image.load("Images/test.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

# Menu
def menu():
    menu=True
    selected=0
    #play_music("menu.wav")
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    # play_sound("Text.wav")
                    selected += 1
                elif event.key==pygame.K_DOWN:
                    # play_sound("Text.wav")
                    selected -= 1
                if event.key==pygame.K_RETURN:
                    if selected%3 == 0: #Start
                        # play_sound("Confirm.wav")
                        print("Start")
                        statecheck()
                    if selected%3 == 1: #Quit
                        # play_sound("Cancel.wav")
                        time.sleep(1)
                        pygame.quit()
                        quit()
                    if selected%3 == 2: #Howtoplay
                        print("How to play")
                        screen.fill((0,0,0))

        # UI Output
        title_draw(selected)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Galactic Revolt!")
def statecheck():
    """Nextstar"""
    edb.ship = {
        "hull" : [10, 10],
        "red" : [1, 1], # Trooper
        "blue" : [1, 1], # Supporter
        "yellow" : [1, 1], # Engineer
        "man" : 10, # Power
        "current" : 0,
        "boss" : 25
    }
    win = True
    while edb.ship['current'] < 4 and win == True:
        screen.fill((0,0,0))
        cards = edb.sector_cards()
        print(cards)
        win = eventpress(cards)
        #check
        for values in edb.bad_events:
            if values in cards:
                edb.bad_event(values)
                print('------------------------Trigger', values)
        edb.ship["current"]+= 1
        edb.ship["man"]-= 1
    if not win and edb.ship["man"] <= edb.ship["boss"]:
        print("You Lose")
    else:
        print("You Win")


def eventpress(cards):
    eventpress=True
    selected=0
    cards1 = True
    
    while eventpress:
        for event in pygame.event.get():
            if edb.ship["hull"][0] <= 0 or edb.ship["man"] <= 0:
                return False
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected -= 1
                elif event.key==pygame.K_DOWN:
                    selected += 1
                if event.key==pygame.K_RETURN:
                    if selected%6 == 0 and cards[0]:
                        print(edb.events[cards[0]])
                        canuse = edb.event(cards[0])
                        if canuse:
                            cards[0] = False
                    elif selected%6 == 1:
                        canuse = edb.event(cards[1])
                        if canuse:
                            cards[1] = False
                    elif selected%6 == 2:
                        canuse = edb.event(cards[2])
                        if canuse:
                            cards[2] = False
                    elif selected%6 == 3:
                        canuse = edb.event(cards[3])
                        if canuse:
                            cards[3] = False
                    elif selected%6 == 4:
                        canuse = edb.event(cards[4])
                        if canuse:
                            cards[4] = False
                    elif selected%6 == 5:
                        return True
                    if selected=="quit":
                        pygame.quit()
                        quit()
        #edb.ship_hud2(screen, edb.ship)
        edb.card(selected, cards)
        edb.ship_hud2(screen, edb.ship)
        pygame.display.update()
    time.sleep(5)


#Initialize Game
menu()
pygame.quit()
quit()
