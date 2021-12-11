import pygame
from pygame.locals import *
import os

from pygame.mixer import Sound
import EventDB as edb
import time
import random

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
    my_sound.set_volume(0.3)
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
all_bg = [i+1 for i in range(12)]
random.shuffle(all_bg)

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
    play_music("Audio/menu.wav")
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    play_sound("Audio/Text.wav")
                    selected += 1
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    play_sound("Audio/Text.wav")
                    selected -= 1
                if event.key==pygame.K_RETURN or event.key==pygame.K_SPACE:
                    if selected%3 == 0: #Start
                        play_sound("Audio/Confirm.wav")
                        # print("Start")
                        statecheck()
                    if selected%3 == 1: #Quit
                        play_sound("Audio/Confirm.wav")
                        time.sleep(1)
                        pygame.quit()
                        quit()
                    if selected%3 == 2: #Howtoplay
                        play_sound("Audio/Confirm.wav")
                        # print("How to play")
                        howtoplay()

        # UI Output
        title_draw(selected)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Galactic Revolt!")
def statecheck():
    """Nextstar"""
    play_music("Audio/play.wav")
    edb.ship = {
        "hull" : [10, 10],
        "red" : [1, 1], # Trooper
        "blue" : [1, 1], # Supporter
        "yellow" : [1, 1], # Engineer
        "man" : 10, # Power
        "current" : 0,
        "boss" : 20
    }
    win = True
    while edb.ship['current'] < 10 and win == True:
        play_sound("Audio/start-level.wav")
        screen.fill((0,0,0))
        cards = edb.sector_cards(edb.all_event, edb.all_prob)
        # print(cards)
        win = eventpress(cards)
        #check
        for values in edb.bad_events:
            if values in cards:
                edb.bad_event(values)
                # print('------------------------Trigger', values)
        edb.ship["current"]+= 1
        random_hit = random.random()
        if random_hit <= 0.25:
            edb.ship["hull"][0] -= 1
        edb.ship["man"]-= 1
    if not win or edb.ship["man"] <= edb.ship["boss"]:
        play_music("Audio/lose.wav")
        bg = pygame.transform.scale(pygame.image.load("Images/lose.jpg").convert(), (1024, 768))
        # screen.blit(bg, [0, 0])
        runing = True
        while runing:
            screen.blit(bg,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                        runing = False
            pygame.display.update()
        menu()
        # pygame.display.update()
        # time.sleep(3)
    else:
        play_music("Audio/win.wav")
        bg = pygame.transform.scale(pygame.image.load("Images/win.jpg").convert(), (1024, 768))
        # screen.blit(bg, [0, 0])
        runing = True
        while runing:
            screen.blit(bg,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                        runing = False
            pygame.display.update()
        menu()
        # pygame.display.update()
        # time.sleep(3)
    play_music("Audio/menu.wav")

def howtoplay():
    """how to play"""
    # play_music("Audio/menu.wav")
    howto=0
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                play_sound("Audio/Text.wav")
                if event.key==pygame.K_ESCAPE:
                    runing = False
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    howto+=1
                elif event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    howto-=1
            if howto%4 == 0:
                bg = pygame.transform.scale(pygame.image.load("Images/howtoplay1.jpg").convert(), (1024, 768))
                screen.blit(bg,(0,0))
            elif howto%4 == 1:
                bg = pygame.transform.scale(pygame.image.load("Images/howtoplay2.jpg").convert(), (1024, 768))
                screen.blit(bg,(0,0))
            elif howto%4 == 2:
                bg = pygame.transform.scale(pygame.image.load("Images/howtoplay3.jpg").convert(), (1024, 768))
                screen.blit(bg,(0,0))
            elif howto%4 == 3:
                bg = pygame.transform.scale(pygame.image.load("Images/howtoplay4.jpg").convert(), (1024, 768))
                screen.blit(bg,(0,0))
        pygame.display.update()
    menu()

def eventpress(cards):
    eventpress=True
    selected=0
    bg = random.randint(1, 12)
    while eventpress:
        for event in pygame.event.get():
            if edb.ship["hull"][0] <= 0 or edb.ship["man"] <= 0:
                return False
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    play_sound("Audio/Text.wav")
                    selected -= 1
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    play_sound("Audio/Text.wav")
                    selected += 1
                if event.key==pygame.K_RETURN or event.key==pygame.K_SPACE:
                    #play_sound("Audio/Confirm.wav")
                    if selected%6 == 0 and cards[0]:
                        #print(edb.events[cards[0]])
                        canuse = edb.event(cards[0])
                        if canuse:
                            play_sound("Audio/Confirm.wav")
                            cards[0] = False
                        else:
                            play_sound("Audio/no.wav")
                    elif selected%6 == 1:
                        canuse = edb.event(cards[1])
                        if canuse:
                            play_sound("Audio/Confirm.wav")
                            cards[1] = False
                        else:
                            play_sound("Audio/no.wav")
                    elif selected%6 == 2:
                        canuse = edb.event(cards[2])
                        if canuse:
                            play_sound("Audio/Confirm.wav")
                            cards[2] = False
                        else:
                            play_sound("Audio/no.wav")
                    elif selected%6 == 3:
                        canuse = edb.event(cards[3])
                        if canuse:
                            play_sound("Audio/Confirm.wav")
                            cards[3] = False
                        else:
                            play_sound("Audio/no.wav")
                    elif selected%6 == 4:
                        canuse = edb.event(cards[4])
                        if canuse:
                            play_sound("Audio/Confirm.wav")
                            cards[4] = False
                        else:
                            play_sound("Audio/no.wav")
                    elif selected%6 == 5:
                        return True
                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    return True
                if event.key==pygame.K_LCTRL or event.key==pygame.K_RCTRL or event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    if edb.ship["red"][0] > 0 and edb.ship["blue"][0] > 0 and edb.ship["yellow"][0] > 0:
                        play_sound("Audio/generate.wav")
                        edb.ship["red"][0] -= 1
                        edb.ship["blue"][0] -= 1
                        edb.ship["yellow"][0] -= 1
                        edb.ship["man"] += 1
                    else:
                        play_sound("Audio/no.wav")
        #edb.ship_hud2(screen, edb.ship)
        edb.card(selected, cards, bg)
        edb.ship_hud2(screen, edb.ship)
        pygame.display.update()
    time.sleep(5)


#Initialize Game
menu()
pygame.quit()
quit()
