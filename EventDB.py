"""Events Database"""
import random
import os
import pygame
import time

def text(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

ship = {
        "hull" : [1, 10],
        "red" : [0, 0], #♞ Trooper
        "blue" : [1, 1], #♝ Supporter
        "yellow" : [1, 1], #♜ Engineer
        "man" : 10, #♟
        "current" : 0,
        "boss" : 25
    }
red = "♞"
blue = "♝"
yellow = "♜"
man = "♟"

font = "PressStart2P.ttf"
UIfont = "consola.ttf"

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
    "Recovery" : "2%s to +1 HULL" %(man),
    "EV2" : "%s → MAX%s" %(man, red),
    "EV3" : "%s → MAX%s" %(man, blue),
    "EV4" : "%s → MAX%s" %(man, yellow),
    "Bad1" : "2%s to avoid -2 HULL" %yellow,
    "Bad2" : "2%s to avoid -2 %s" %(blue, man),
    "Bad3" : "2%s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Change1" : "-1 MAX%s to +2 MAX%s" %(yellow, red),
    "Change2" : "-1 MAX%s to +2 MAX%s" %(red, blue),
    "Change3" : "-1 MAX%s to +2 MAX%s" %(blue, yellow)
}
bonus_events = {
    
}
bad_events = {
    "Bad1" : "2%s to avoid -2 HULL" %yellow,
    "Bad2" : "2%s to avoid -2 %s" %(blue, man),
    "Bad3" : "2%s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Bonus1" : "+2 %s" %(man),
    "Bonus2" : "+1 %s %s %s" %(red, blue, yellow)
}
boss_events = {
    "Badass1" : "4%s to avoid -1 extra damage" %yellow,
    "Badass2" : "4%s to avoid -2 extra damage" %man,
    "Badass3" : "2 %s %s %s to avoid -1 extra damage" %(red, blue, yellow),
    "Badass4" : "4%s to avoid -2 %s" %(blue, man),
    "Badass5" : "4%s to avoid -2 %s %s" %(yellow, red, blue),
    "Badass6" : "2 %s %s %s to avoid -2 %s" %(red, blue, yellow, man),
    "Badass7" : "2 %s to avoid -1 %s %s %s" %(man, red, blue, yellow)
}
def ship_hud(ship): #สร้างหน้าบอก Resource
    """Make Ship HUD"""
    print("Stage %d" %ship['current'])
    print("╔"+"═"*49+"╗")
    print("║HULL: "+("▮"*ship['hull'][0])+"▯"*(ship['hull'][1]-ship['hull'][0]), end="  ║")
    print(" %02d %s ║" %(ship['man'], man), end="")
    print(" %d/%d %s ║" %(ship['red'][0], ship['red'][1], red), end="")
    print(" %d/%d %s ║" %(ship['blue'][0], ship['blue'][1], blue), end="")
    print(" %d/%d %s ║" %(ship['yellow'][0], ship['yellow'][1], yellow))
    print("╚"+"═"*49+"╝")

def sector_cards(): #สุ่มว่าจะมีการ์ดออกมากี่ใบ
    """Draw Sector Cards"""
    ship['red'][0] = ship['red'][1]
    ship['blue'][0] = ship['blue'][1]
    ship['yellow'][0] = ship['yellow'][1]
    all_event = [eve for eve in events.values()]
    num = random.random()*100
    if num >= 0 and num < 25:
        num = 3
    elif num >= 25 and num < 75:
        num = 4
    else:
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
            print("(%d): %s" %(i+1, cards[i]))
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
    for values in bad_events.values():
        if values in cards:
            print('------------------------Trigger', values)

def event(evt): #ใช้งานอีเวนต์
    """Trigger Event"""
    if evt == events["Recruit"]:
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
        ship["man"] += 1
    elif evt == events["Recovery"]:
        ship["man"] -= 2
        ship["hull"][0] += 1
    elif evt == events["EV2"]:
        ship["man"] -= 1
        ship["red"][1] += 1
    elif evt == events["EV3"]:
        ship["man"] -= 1
        ship["blue"][1] += 1
    elif evt == events["EV4"]:
        ship["man"] -= 1
        ship["yellow"][1] += 1
    elif evt == events["Change1"]:
        ship["yellow"][1] -= 1
        ship["red"][1] += 2
    elif evt == events["Change2"]:
        ship["red"][1] -= 1
        ship["blue"][1] += 2
    elif evt == events["Change3"]:
        ship["blue"][1] -= 1
        ship["yellow"][1] += 2
    else:
        print("no")

def bad_event(evt):
    """Trigger Bad Event"""
    if evt == bad_events["Bad1"]:
        ship["hull"][0] -= 2
    elif evt == bad_events["Bad2"]:
        ship["man"] -= 2
    elif evt == bad_events["Bad3"]:
        ship["blue"][1] -= 1
        ship["yellow"][1] -= 1

def bonus_event():
    """Random Bonus Event"""
    bonus = random.random()*100
    if bonus <= 40:
        print("Trigger")

def boss_event(evt):
    """Trigger Boss Event"""
    if evt == boss_events["Badass1"]:
        ship["hull"][0] -= 2
    if evt == boss_events["Badass2"]:
        ship["hull"][0] -= 3
    if evt == boss_events["Badass3"]:
        ship["hull"][0] -= 2
    if evt == boss_events["Badass4"]:
        ship["man"] -= 2
    if evt == boss_events["Badass5"]:
        ship["red"][1] -= 2
        ship["blue"][1] -= 2
    if evt == boss_events["Badass6"]:
        ship["man"] -= 2
    if evt == boss_events["Badass7"]:
        ship["yellow"][1] -= 1
        ship["red"][1] -= 1
        ship["blue"][1] -= 1

def boss_stage():
    """Boos Stage"""
    boss_deck = [boss for boss in boss_events.values()]
    random_event(boss_deck, 5)
    print(boss_deck)

def test(screen):
    bg = pygame.transform.scale(pygame.image.load("test.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("Stage %d" %ship['current'], font, 48, white), (512, 384))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()
    
def ship_hud(screen, ship): #สร้างหน้าบอก Resource
    """Make Ship pygame"""
    bg = pygame.transform.scale(pygame.image.load("Card1.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("Stage %d" %ship['current'], UIfont, 48, red1), (0, 50))
    #screen.blit(text("╔"+"═"*49+"╗", UIfont, 48, blue1), (700, 50))
    screen.blit(text("HULL: "+("▮"*ship['hull'][0])+"▯"*(ship['hull'][1]-ship['hull'][0]), UIfont, 48, black), (0, 75))
    screen.blit(text(" %02d %s " %(ship['man'], man), UIfont, 48, green), (0, 1000))
    screen.blit(text(" %d/%d %s " %(ship['red'][0], ship['red'][1], red), UIfont, 48, black), (0, 125))
    screen.blit(text(" %d/%d %s " %(ship['blue'][0], ship['blue'][1], blue), UIfont, 48, black), (0, 150))
    screen.blit(text(" %d/%d %s " %(ship['yellow'][0], ship['yellow'][1], yellow), UIfont, 48, black), (0, 175))
    #screen.blit(text("╚"+"═"*49+"╝", UIfont, 48, black), (700, 200))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

# def eventpress():
#     eventpress=True
#     selected="1"

#     while eventpress:
#         for event in pygame.event.get():
#             if event.type==pygame.KEYDOWN:
#                 if event.key==pygame.K_1:
#                     selected="1"
#                 elif event.key==pygame.K_2:
#                     selected="2"
#                 elif event.key==pygame.K_3:
#                     selected="3"
#                 elif event.key==pygame.K_4:
#                     selected="4"
#                 elif event.key==pygame.K_5:
#                     selected="5"
#                 if event.key==pygame.K_RETURN:
#                     if selected=="1":
#                         pass
#                     elif selected=="2":
#                         pass
#                     elif selected=="3":
#                         pass
#                     elif selected=="4":
#                         pass
#                     elif selected=="5":
#                         pass
#                     if selected=="quit":
#                         pygame.quit()
#                         quit()
