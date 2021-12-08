"""Events Database"""
import random
import os
import pygame
import time
import randomstar

starname = randomstar.starname

screen_width=1024
screen_height=768
screen=pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FPS=30

def text(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

ship = {
        "hull" : [1, 10],
        "red" : [1, 1], #♞ Trooper
        "blue" : [1, 1], #♝ Supporter
        "yellow" : [1, 1], #♜ Engineer
        "man" : 10, #♟
        "current" : 0,
        "boss" : 25
    }
red = "T"
blue = "S"
yellow = "E"
man = "Power"

font = "PressStart2P.ttf"
UIfont = "PressStart2P.ttf"
box = 64

white=(255, 255, 255)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red1=(255, 0, 0)
green=(0, 255, 0)
blue1=(0, 0, 255)
yellow1=(255, 255, 0)
darkmagenta=(139,0,139)
purple=(98,24,245)
textcolor=(62, 170, 174)
outlinecolor=(140,104,121)
selectcolor=(255, 170, 94)
pink1=(255,67,164)

# เพิ่มเฉพาะสี
# เพิ่มคน
# เพิ่มค่า Max ของสี
# ทำให้อนาคตเกิดผลดี (บอสลดการ์ด)
# เพิ่มจำนวนการ์ดในอนาคต


# ไม่ทำแล้วสุ่มผลเสีย
# ลด Max ของสี
# บอสจะแข็งแกร่งขึ้น (เลือดเยอะขึ้น, จำนวดการ์ดในกองบอสเยอะขึ้น, ....)
# ลดจำนวนการ์ดในอนาคต
# ถ้าไม่ทำจะเสียคน
# ไม่ทำมี Damage

events = {
    "Recruit" : "%s + %s + %s → %s" %(red, blue ,yellow, man),
    "Recovery1" : "-2 %s to +1 HULL" %(man),
    "Recovery2" : "-2 %s to +1 HULL" %(man),
    "Recovery3" : "-2 %s to +1 HULL" %(man),
    "EV2" : "-1 %s → +1 MAX %s" %(man, red),
    "EV3" : "-1 %s → +1 MAX %s" %(man, blue),
    "EV4" : "-1 %s → +1 MAX %s" %(man, yellow),
    "Bad1" : "2 %s to avoid -1 HULL" %yellow,
    "Bad2" : "2 %s to avoid -2 %s" %(blue, man),
    "Bad3" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Change1" : "-1 MAX %s to +2 MAX %s" %(yellow, red),
    "Change2" : "-1 MAX %s to +2 MAX %s" %(red, blue),
    "Change3" : "-1 MAX %s to +2 MAX %s" %(blue, yellow),
    "Bonus1" : "+2 %s" %(man),
    "Bonus2" : "+1 %s %s %s" %(red, blue, yellow),
    "ExChange1" : "-1 MAX %s to +1 MAX %s %s" %(yellow, red, blue),
    "ExChange2" : "-1 MAX %s to +1 MAX %s %s" %(red, yellow, blue),
    "ExChange3" : "-1 MAX %s to +1 MAX %s %s" %(blue, red, yellow),
    "LastSave1" : "-1 MAX %s to +2 %s" %(red, blue),
    "LastSave2" : "-1 MAX %s to +2 %s" %(red, yellow),
    "LastSave3" : "-1 MAX %s to +2 %s" %(blue, red),
    "LastSave4" : "-1 MAX %s to +2 %s" %(blue, yellow),
    "LastSave5" : "-1 MAX %s to +2 %s" %(yellow, blue),
    "LastSave6" : "-1 MAX %s to +2 %s" %(yellow, red),
    "ThebigSave1" : "-1 %s to +3 %s" %(man, yellow),
    "ThebigSave2" : "-1 %s to +3 %s" %(man, blue),
    "ThebigSave3" : "-1 %s to +3 %s" %(man, red),
    "ThePowerUP1" : "-1 MAX %s to +1 %s" %(red, man),
    "ThePowerUP2" : "-1 MAX %s to +1 %s" %(blue, man),
    "ThePowerUP3" : "-1 MAX %s to +1 %s" %(yellow, man),

}
bonus_events = {
    
}
bad_events = {
    "Bad1" : "2 %s to avoid -2 HULL" %yellow,
    "Bad2" : "2 %s to avoid -2 %s" %(blue, man),
    "Bad3" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    #"Bonus1" : "+2 %s" %(man),
    "VeryBad1" : "2 %s to avoid -1 %s" %(red, man),
    #"Bonus2" : "+1 %s %s %s" %(red, blue, yellow)
    "VeryBad2" : "2 %s to avoid -1 %s" %(yellow, man),
    "VeryBad3" : "2 %s to avoid -1 %s" %(blue, man),
    "Goduck1" : "-1 All Resource to avoid -2 %s" %man,
}
def ship_hud(ship): #สร้างหน้าบอก Resource
    """Make Ship HUD"""
    #len_1 = len(" HULL: "+("▮"*ship['hull'][0])+"▯"*(ship['hull'][1]-ship['hull'][0]))
    #len_2 = len(" %02d %s ║" %(ship['man'], man))
    #len_3 = len(" %d/%d %s ║" %(ship['blue'][0], ship['blue'][1], blue))
   # len_4 = len(" %d/%d %s ║" %(ship['yellow'][0], ship['yellow'][1]))
   # len_re = int(len_1)+int(len_2)+int(len_3)+int(len_4)
    print("Stage %d" %ship['current'])
    print("╔"+"═"*75+"╗")
    print("║ HULL: "+("▮"*ship['hull'][0])+"▯"*(ship['hull'][1]-ship['hull'][0]), end="  ║")
    print(" %02d %s ║" %(ship['man'], man), end="")
    print(" %d/%d %s ║" %(ship['red'][0], ship['red'][1], red), end="")
    print(" %d/%d %s ║" %(ship['blue'][0], ship['blue'][1], blue), end="")
    print(" %d/%d %s ║" %(ship['yellow'][0], ship['yellow'][1], yellow))
    print("╚"+"═"*75+"╝")

def sector_cards(): #สุ่มว่าจะมีการ์ดออกมากี่ใบ
    """Draw Sector Cards"""
    ship['red'][0] = ship['red'][1]
    ship['blue'][0] = ship['blue'][1]
    ship['yellow'][0] = ship['yellow'][1]
    all_event = [eve for eve in events]
    num = random.random()*100
    if num >= 0 and num < 25:
        num = 3
    elif num >= 25 and num < 75:
        num = 4
    else:
        num = 5
    num = 5
    cards = random_event(all_event, num)
    return cards

def random_event(all_event, num): #สุ่มว่าจะเจออีเวนต์อะไรบ้าง
    """Random Event"""
    cards = []
    random.shuffle(all_event)
    for _ in range(num):
        cards.append(all_event.pop())
    return cards

def choose_card(cards): #เลือกการ์ด
    """Choose Card"""
    while cards:
        if ship["hull"][0] <= 0:
            return False
        ship_hud(ship)
        print("Please choose a card")
        for i in range(len(cards)):
            print("(%d) %s: %s" %(i+1, cards[i], events[cards[i]]))
        choose = int(input())
        if choose == 0:
            break
        elif choose-1 in range(len(cards)):
            event(cards[choose-1])
            del cards[choose-1]
            #os.system('cls')       
        else:
            print("ERROR")
    print(cards)
    for values in bad_events:
        if values in cards:
            print('------------------------Trigger', values)

def event(evt): #ใช้งานอีเวนต์
    """Trigger Event"""
    if evt == "Recruit" and (ship["red"][0] > 0 and ship["blue"][0] > 0 and ship["yellow"][0] > 0):
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
        ship["man"] += 1
    elif evt == "Recovery1" and ship["man"] >= 2:
        ship["man"] -= 2
        ship["hull"][0] += 1
    elif evt == "EV2" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["red"][1] += 1
    elif evt == "EV3" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["blue"][1] += 1
    elif evt == "EV4" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["yellow"][1] += 1
    elif evt == "Change1" and ship["yellow"][1] >= 1:
        ship["yellow"][1] -= 1
        ship["red"][1] += 2
    elif evt == "Change2" and ship["red"][1] >= 1:
        ship["red"][1] -= 1
        ship["blue"][1] += 2
    elif evt == "Change3" and ship["blue"][1] >= 1:
        ship["blue"][1] -= 1
        ship["yellow"][1] += 2
    elif evt == "Bonus1":
        ship["man"] += 2
    elif evt == "Bonus2":
        ship["yellow"][1] += 1
        ship["red"][1] += 1
        ship["blue"][1] += 1
    elif evt == "ExChange1":
        ship["yellow"][1] -= 1
        ship["red"][1] += 1
        ship["blue"][1] += 1
    elif evt == "ExChange2":
        ship["yellow"][1] += 1
        ship["red"][1] -= 1
        ship["blue"][1] += 1
    elif evt == "ExChange3":
        ship["yellow"][1] += 1
        ship["red"][1] += 1
        ship["blue"][1] -= 1 
    elif evt == "LastSave1":
        ship["blue"][0] += 2
        ship["red"][1] -= 1
    elif evt == "LastSave2":
        ship["yellow"][0] += 2
        ship["red"][1] -= 1
    elif evt == "LastSave3":
        ship["red"][0] += 2
        ship["blue"][1] -= 1
    elif evt == "LastSave4":
        ship["yellow"][0] += 2
        ship["blue"][1] -= 1
    elif evt == "LastSave5":
        ship["blue"][0] += 2
        ship["yellow"][1] -= 1
    elif evt == "LastSave6":
        ship["red"][0] += 2
        ship["yellow"][1] -= 1
    elif evt == "ThebigSave1":
        ship["man"] -= 1
        ship["yellow"][0] += 3
    elif evt == "ThebigSave2":
        ship["man"] -= 1
        ship["blue"][0] += 3
    elif evt == "ThebigSave3":
        ship["man"] -= 1
        ship["red"][0] += 3
    elif evt == "ThePowerUP1":
        ship["man"] += 1
        ship["red"][1] -= 1
    elif evt == "ThePowerUP2":
        ship["man"] += 1
        ship["blue"][1] -= 1
    elif evt == "ThePowerUP3":
        ship["man"] += 1
        ship["yellow"][1] -= 1
    else:
        print("no")

def bad_event(evt):
    """Trigger Bad Event"""
    if evt == "Bad1" and ship["hull"][0] >= 1:
        ship["hull"][0] -= 1
    elif evt == "Bad2" and ship["man"] >= 2:
        ship["man"] -= 2
    elif evt == "Bad3" and (ship["blue"][1] >= 1 and ship["yellow"][1] >= 1):
        ship["blue"][1] -= 1
        ship["yellow"][1] -= 1
    elif evt == "VeryBad1":
        ship["man"] -= 1
    elif evt == "VeryBad2":
        ship["man"] -= 1
    elif evt == "VeryBad3":
        ship["man"] -= 1
    elif evt == "Goduck1":
        ship["man"] -= 2

def bonus_event():
    """Random Bonus Event"""
    bonus = random.random()*100
    if bonus <= 40:
        print("Trigger")

def test(screen):
    bg = pygame.transform.scale(pygame.image.load("test.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("Stage %d" %ship['current'], font, 48, white), (512, 384))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
#bg = pygame.transform.scale(pygame.image.load("Space_Background_4.png").convert_alpha(), (1024, 768))
ui_1 = pygame.transform.scale(pygame.image.load("hud.png").convert_alpha(), (1024, 768))
def ship_hud2(screen, ship): #สร้างหน้าบอก Resource
    """Make Ship pygame"""
  #  bg = pygame.transform.scale(pygame.image.load("Space_Background_4.png").convert_alpha(), (1024, 768))
   # ui_1 = pygame.transform.scale(pygame.image.load("hud.png").convert_alpha(), (1024, 768))
    #screen.blit(bg, [0, 0])
    screen.blit(ui_1, [0, 0])
    screen.blit(text("Star %d: %s" %(ship['current']+1, starname[ship['current']]), UIfont, 36, textcolor), (64, 32))
    #screen.blit(text("╔"+"═"*49+"╗", UIfont, 48, blue1), (700, 50))
    screen.blit(text("HULL: "+("O"*ship['hull'][0])+"-"*(ship['hull'][1]-ship['hull'][0]), UIfont, 24, white), (256, 576))
    screen.blit(text("%02d %s " %(ship['man'], man), UIfont, 24, green), (256, 640))
    screen.blit(text("%d/%d %s " %(ship['red'][0], ship['red'][1], red), UIfont, 24, white), (704, 580))
    screen.blit(text("%d/%d %s " %(ship['blue'][0], ship['blue'][1], blue), UIfont, 24, white), (704, 620))
    screen.blit(text("%d/%d %s " %(ship['yellow'][0], ship['yellow'][1], yellow), UIfont, 24, white), (704, 660))
    #screen.blit(text("╚"+"═"*49+"╝", UIfont, 48, black), (700, 200))
    #screen.blit(text(events["Recruit"], UIfont, 10, white), (box*1, box*2))
    #screen.blit(text(events["Recovery1"], UIfont, 10, white), (box*1, box*3))   
    #screen.blit(text(events["Bad1"], UIfont, 10, white), (box*1, box*4))   
    #screen.blit(text(events["Bad2"], UIfont, 10, white), (box*1, box*5))
    #screen.blit(text(events["Bad2"], UIfont, 10, white), (box*1, box*5))          
    pygame.display.update()
   # time.sleep(5)

bg_big = pygame.image.load("Space Background.png").convert()
def card(selected, cards):
    """card ui"""
    screen.blit(bg_big, [0, 0])
    if selected%6 == 0:
        text_1 = text("%s <<" %events[cards[0]], UIfont, 24, selectcolor)
    else:
        text_1 = text("%s" %cards[0], UIfont, 24, white)
    if selected%6 == 1:
        text_2=text("%s <<" %events[cards[1]], UIfont, 24, selectcolor)
    else:
        text_2 = text("%s" %cards[1], UIfont, 24, white)
    if selected%6 == 2:
        text_3 = text("%s <<" %events[cards[2]], UIfont, 24, selectcolor)
    else:
        text_3 = text("%s" %cards[2], UIfont, 24, white)
    if selected%6 == 3:
        text_4 = text("%s <<" %events[cards[3]], UIfont, 24, selectcolor)
    else:
        text_4 = text("%s" %cards[3], UIfont, 24, white)
    if selected%6 == 4:
        text_5 = text("%s <<" %events[cards[4]], UIfont, 24, selectcolor)
    else:
        text_5 = text("%s" %cards[4], UIfont, 24, white)
    if selected%6 == 5:
        text_6 = text(">> SKIPPED <<", UIfont, 24, red1)
    else:
        text_6 = text(">> SKIPPED", UIfont, 24, pink1)
    
    screen.blit(text_1, (64, 120))
    screen.blit(text_2, (64, 180))
    screen.blit(text_3, (64, 240))
    screen.blit(text_4, (64, 300))
    screen.blit(text_5, (64, 360))
    screen.blit(text_6, (64, 420))
    #pygame.display.update()
    # time.sleep(5)
