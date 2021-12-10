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
used = "[used]"
def text(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

ship = {
        "hull" : [10, 10],
        "red" : [1, 1], # Trooper
        "blue" : [1, 1], # Supporter
        "yellow" : [1, 1], # Engineer
        "man" : 10, # Power
        "current" : 0,
        "boss" : 25
    }
red = "Tro"
blue = "Sup"
yellow = "Eng"
man = "Power"

font = "Fonts/ZF#2ndPixelus.ttf"
UIfont = "Fonts/ZF#2ndPixelus.ttf"
box = 64

white=(255, 255, 255)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red1=(255, 0, 0)
green=(0, 255, 0)
blue1=(98, 197, 218)
yellow1=(255, 255, 0)
darkmagenta=(139,0,139)
purple=(98,24,245)
textcolor=(62, 170, 174)
outlinecolor=(140,104,121)
selectcolor=(255, 170, 94)
pink1=(255,67,164)
orange=(252, 106, 3)

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
    "Degenerate" : "-1 %s -> +1 MAX %s %s %s" %(man, red, blue, yellow),
    "Eat Ship" : "-1 HULL to +1 %s %s %s" %(red, blue, yellow),
    "Engineer Exchange" : "-1 MAX %s to +1 %s %s" %(yellow, red, blue),
    "Trooper ExChange" : "-1 MAX %s to +1 %s %s" %(red, yellow, blue),
    "Supporter ExChange" : "-1 MAX %s to +1 %s %s" %(blue, red, yellow),
    "Engineer Saving" : "-1 %s to +3 %s" %(man, yellow),
    "Supporter Saving" : "-1 %s to +3 %s" %(man, blue),
    "Trooper Saving" : "-1 %s to +3 %s" %(man, red),
    "Trooper Sacrifice" : "-1 MAX %s to +1 %s" %(red, man),
    "Supporter Sacrifice" : "-1 MAX %s to +1 %s" %(blue, man),
    "Engineer Sacrifice" : "-1 MAX %s to +1 %s" %(yellow, man), # บ่อย 50%
    "Repair" : "-1 %s and -1 %s to +1 HULL" %(blue, yellow),
    "Trooper power up" : "-2 %s to +1 MAX %s" %(red, red),
    "Supporter power up" : "-2 %s to +1 MAX %s" %(blue, blue),
    "Engineer power up" : "-2 %s to +1 MAX %s" %(yellow, yellow),
    "Engineer at work" : "-2 %s to +1 %s" %(yellow, man),
    "Trooper at work" : "-2 %s to +1 %s" %(red, man),
    "Supporter at work" : "-2 %s to +1 %s" %(blue, man),
    "Engineer Overtime" : "-3 %s to +2 %s" %(yellow, man),
    "Trooper Overtime" : "-3 %s to +2 %s" %(red, man),
    "Supporter Overtime" : "-3 %s to +2 %s" %(blue, man), # กลางๆ 30%
    "Trooper Volunteer" : "-1 %s to +2 MAX %s" %(red, red),
    "Supporter Volunteer" : "-1 %s to +2 MAX %s" %(blue, blue),
    "Engineer Volunteer" : "-1 %s to +2 MAX %s" %(yellow, yellow), # น้อย 10%
}
event_prob1 = [0.5 for _ in range(11)]
event_prob2 = [0.3 for _ in range(10)]
event_prob3 = [0.1 for _ in range(3)]
bonus_events = {
    "Effective Generator" : "+2 %s" %(man),
    "Motivated Officers" : "+1 MAX %s %s %s" %(red, blue, yellow),
    "Motivated Trooper" : "+2 MAX %s" %(red),
    "Motivated Supporter" : "+2 MAX %s" %(blue),
    "Motivated Engineer" : "+2 MAX %s" %(yellow)
}
bonus_prob = [0.1 for _ in range(5)]
bad_events = {
    "Broken Hull" : "2 %s to avoid -2 HULL" %yellow,
    "Damaged Hull" : "2 %s to avoid -2 HULL" %red,
    "Leaked Hull" : "2 %s to avoid -2 HULL" %blue,
    "Generator Supporting" : "2 %s to avoid -2 %s" %(blue, man),
    "Strike" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Defend" : "2 %s to avoid -1 %s" %(red, man),
    "Generator Reparing" : "2 %s to avoid -1 %s" %(yellow, man),
    "Get Damaged" : "2 %s to avoid -1 %s" %(blue, man),
    "Generator Treatment" : "-1 %s %s %s to avoid -2 %s" %(red, blue, yellow, man)
}
bad_prob = [0.2 for _ in range(9)]
all_event = [eve for eve in events] + [eve for eve in bonus_events] + [eve for eve in bad_events]
all_prob = event_prob1 + event_prob2 + event_prob3 + bonus_prob + bad_prob

evdb = {
    "Degenerate" : "-1 %s -> +1 MAX %s %s %s" %(man, red, blue, yellow),
    "Eat Ship" : "-1 HULL to +1 %s %s %s" %(red, blue, yellow),
    "Engineer Exchange" : "-1 MAX %s to +1 %s %s" %(yellow, red, blue),
    "Trooper ExChange" : "-1 MAX %s to +1 %s %s" %(red, yellow, blue),
    "Supporter ExChange" : "-1 MAX %s to +1 %s %s" %(blue, red, yellow),
    "Engineer Saving" : "-1 %s to +3 %s" %(man, yellow),
    "Supporter Saving" : "-1 %s to +3 %s" %(man, blue),
    "Trooper Saving" : "-1 %s to +3 %s" %(man, red),
    "Trooper Sacrifice" : "-1 MAX %s to +1 %s" %(red, man),
    "Supporter Sacrifice" : "-1 MAX %s to +1 %s" %(blue, man),
    "Engineer Sacrifice" : "-1 MAX %s to +1 %s" %(yellow, man), # บ่อย 50%
    "Repair" : "-1 %s and -1 %s to +1 HULL" %(blue, yellow),
    "Trooper power up" : "-2 %s to +1 MAX %s" %(red, red),
    "Supporter power up" : "-2 %s to +1 MAX %s" %(blue, blue),
    "Engineer power up" : "-2 %s to +1 MAX %s" %(yellow, yellow),
    "Engineer at work" : "-2 %s to +1 %s" %(yellow, man),
    "Trooper at work" : "-2 %s to +1 %s" %(red, man),
    "Supporter at work" : "-2 %s to +1 %s" %(blue, man),
    "Engineer Overtime" : "-3 %s to +2 %s" %(yellow, man),
    "Trooper Overtime" : "-3 %s to +2 %s" %(red, man),
    "Supporter Overtime" : "-3 %s to +2 %s" %(blue, man), # กลางๆ 30%
    "Trooper Volunteer" : "-1 %s to +2 MAX %s" %(red, red),
    "Supporter Volunteer" : "-1 %s to +2 MAX %s" %(blue, blue),
    "Engineer Volunteer" : "-1 %s to +2 MAX %s" %(yellow, yellow),
    "Effective Generator" : "+2 %s" %(man),
    "Motivated Officers" : "+1 MAX %s %s %s" %(red, blue, yellow),
    "Motivated Trooper" : "+2 MAX %s" %(red),
    "Motivated Supporter" : "+2 MAX %s" %(blue),
    "Motivated Engineer" : "+2 MAX %s" %(yellow),
    "Broken Hull" : "2 %s to avoid -2 HULL" %yellow,
    "Damaged Hull" : "2 %s to avoid -2 HULL" %red,
    "Leaked Hull" : "2 %s to avoid -2 HULL" %blue,
    "Generator Supporting" : "2 %s to avoid -2 %s" %(blue, man),
    "Strike" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Defend" : "2 %s to avoid -1 %s" %(red, man),
    "Generator Reparing" : "2 %s to avoid -1 %s" %(yellow, man),
    "Get Damaged" : "2 %s to avoid -1 %s" %(blue, man),
    "Generator Treatment" : "-1 %s %s %s to avoid -2 %s" %(red, blue, yellow, man)
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

def sector_cards(all_event, all_prob): #สุ่มว่าจะมีการ์ดออกมากี่ใบ
    """Draw Sector Cards"""
    ship['red'][0] = ship['red'][1]
    ship['blue'][0] = ship['blue'][1]
    ship['yellow'][0] = ship['yellow'][1]
    # print(all_event)
    num = 5
    cards = []
    for _ in range(num):
        cards.append("".join((random.choices(all_event, all_prob))))
    return cards

def random_event(all_event, num): #สุ่มว่าจะเจออีเวนต์อะไรบ้าง
    """Random Event"""
    cards = []
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
    if evt == "Repair" and ship["blue"][0] >= 1 and ship["yellow"][0] >= 1 and ship["hull"][0] < 10:
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
        ship["hull"][0] += 1
    elif evt == "Degenerate" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["blue"][1] += 1
        ship["red"][1] += 1
        ship["yellow"][1] += 1
    elif evt == "Eat Ship" and ship["hull"][0] >= 2:
        ship["hull"][0] -= 1
        ship["blue"][1] += 1
        ship["red"][1] += 1
        ship["yellow"][1] += 1
    elif evt == "Engineer Exchange" and ship["yellow"][1] >= 1:
        ship["yellow"][0] -= 1
        ship["red"][0] += 1
    elif evt == "Trooper ExChange" and ship["red"][1] >= 1:
        ship["red"][0] -= 1
        ship["blue"][0] += 1
    elif evt == "Supporter ExChange" and ship["blue"][1] >= 1:
        ship["blue"][0] -= 1
        ship["yellow"][0] += 1
    elif evt == "Effective Generator":
        ship["man"] += 2
    elif evt == "Motivated Officers":
        ship["yellow"][1] += 1
        ship["red"][1] += 1
        ship["blue"][1] += 1
    elif evt == "Motivated Trooper":
        ship["red"][1] += 2
    elif evt == "Motivated Supporter":
        ship["blue"][1] += 2
    elif evt == "Motivated Engineer":
        ship["yellow"][1] += 2
    elif evt == "Engineer Saving" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["yellow"][0] += 3
    elif evt == "Supporter Saving" and ship["man"] >= 1: 
        ship["man"] -= 1
        ship["blue"][0] += 3
    elif evt == "Trooper Saving" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["red"][0] += 3
    elif evt == "Trooper Sacrifice" and ship["red"][1] >= 1:
        ship["man"] += 1
        ship["red"][1] -= 1
    elif evt == "Supporter Sacrifice" and ship["blue"][1] >= 1:
        ship["man"] += 1
        ship["blue"][1] -= 1
    elif evt == "Engineer Sacrifice" and ship["yellow"][1] >= 1:
        ship["man"] += 1
        ship["yellow"][1] -= 1
    elif evt == "Trooper power up" and ship["red"][0] >= 2:
        ship["red"][1] += 1
        ship["red"][0] -= 2
    elif evt == "Supporter power up" and ship["blue"][0] >= 2:
        ship["blue"][1] += 1
        ship["blue"][0] -= 2
    elif evt == "Engineer power up" and ship["yellow"][0] >= 2:
        ship["yellow"][1] += 1
        ship["yellow"][0] -= 2
    elif evt == "Engineer at work" and ship["yellow"][0] >= 2:
        ship["man"] += 1
        ship["yellow"][0] -= 2
    elif evt == "Trooper at work" and ship["red"][0] >= 2:
        ship["man"] += 1
        ship["red"][0] -= 2
    elif evt == "Supporter at work" and ship["blue"][0] >= 2:
        ship["man"] += 1
        ship["blue"][0] -= 2
    elif evt == "Engineer Overtime" and ship["yellow"][0] >= 3:
        ship["man"] += 2
        ship["yellow"][0] -= 3
    elif evt == "Trooper Overtime" and ship["red"][0] >= 3:
        ship["man"] += 2
        ship["red"][0] -= 3
    elif evt == "Supporter Overtime" and ship["blue"][0] >= 3:
        ship["man"] += 2
        ship["blue"][0] -= 3
    elif evt == "Trooper Volunteer" and ship["red"][0] >= 1:
        ship["red"][1] += 2
    elif evt == "Supporter Volunteer" and ship["blue"][0] >= 1:
        ship["blue"][1] += 2
    elif evt == "Engineer Volunteer" and ship["yellow"][0] >= 1:
        ship["yellow"][1] += 2
    elif evt == "Strike" and (ship["blue"][1] >= 1 and ship["yellow"][1] >= 1):
        ship["blue"][1] -= 1
        ship["yellow"][1] -= 1
    elif evt == "Generator Treatment" and ship["red"][0] >= 1 and ship["blue"][0] >= 1 and ship["yellow"][0] >= 1:
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
    elif evt == "Defend" and ship["red"][0] >= 2:
        ship["red"][0] -= 2
    elif evt == "Generator Reparing" and ship["yellow"][0] >= 2:
        ship["yellow"][0] -= 2
    elif evt == "Get Damaged" and ship["blue"][0] >= 2:
        ship["blue"][0] -= 2
    elif evt == "Broken Hull" and ship["yellow"][0] >= 2:
        ship["yellow"][0] -= 2
    elif evt == "Damaged Hull" and ship["red"][0] >= 2:
        ship["red"][0] -= 2
    elif evt == "Leaked Hull" and ship["blue"][0] >= 2:
        ship["blue"][0] -= 2
    elif evt == "Generator Supporting" and ship["blue"][0] >= 2:
        ship["blue"][0] -= 2
    
    else:
        print("no")
        return False
    return True

def bad_event(evt):
    """Trigger Bad Event"""
    if evt == "Broken Hull":
        ship["hull"][0] -= 2
    elif evt == "Damaged Hull":
        ship["hull"][0] -= 2
    elif evt == "Leaked Hull":
        ship["hull"][0] -= 2
    elif evt == "Generator Supporting":
        ship["man"] -= 2
    elif evt == "Strike":
        ship["blue"][1] -= 1
        ship["yellow"][1] -= 1
    elif evt == "Defend":
        ship["man"] -= 1
    elif evt == "Generator Reparing":
        ship["man"] -= 1
    elif evt == "Get Damaged":
        ship["man"] -= 1
    elif evt == "Generator Treatment":
        ship["man"] -= 2

def test(screen):
    bg = pygame.transform.scale(pygame.image.load("Images/test.png").convert(), (1024, 768))
    screen.blit(bg, [0, 0])
    screen.blit(text("Stage %d" %ship['current'], font, 48, white), (512, 384))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
#bg = pygame.transform.scale(pygame.image.load("Space_Background_4.png").convert_alpha(), (1024, 768))
ui_1 = pygame.transform.scale(pygame.image.load("Images/hud.png").convert_alpha(), (1024, 768))
def ship_hud2(screen, ship): #สร้างหน้าบอก Resource
    """Make Ship pygame"""
    screen.blit(ui_1, [0, 0])
    screen.blit(text("Star %d: %s" %(ship['current']+1, starname[ship['current']]), UIfont, 64, textcolor), (64, 32))
    screen.blit(text("HULL: ["+("O"*ship['hull'][0])+"_"*(ship['hull'][1]-ship['hull'][0])+"]", UIfont, 100, green), (256, 576-48))
    screen.blit(text("%02d %s" %(ship['man'], man), UIfont, 128, blue1), (704-192, 640-48))
    screen.blit(text("%d/%d %s " %(ship['red'][0], ship['red'][1], red), UIfont, 64, white), (256, 580+16))
    screen.blit(text("%d/%d %s " %(ship['blue'][0], ship['blue'][1], blue), UIfont, 64, white), (256, 620+16))
    screen.blit(text("%d/%d %s " %(ship['yellow'][0], ship['yellow'][1], yellow), UIfont, 64, white), (256, 660+16))      
    pygame.display.update()
   # time.sleep(5)
def showused(card):
    """changeName"""
    return "[used]" if card == False else card

#bg_big = pygame.image.load("Images/Stars/%d.png" %).convert()
def card(selected, cards, bg):
    """card ui"""
    screen.blit(pygame.image.load("Images/Stars/%d.png" %bg).convert(), [0, 0])
    if selected%6 == 0:
        text_1 = text("%s <<" %evdb.get(cards[0], used), UIfont, 64, selectcolor)
    else:
        text_1 = text("%s" %showused(cards[0]), UIfont, 64, white)
    if selected%6 == 1:
        text_2=text("%s <<" %evdb.get(cards[1], used), UIfont, 64, selectcolor)
    else:
        text_2 = text("%s" %showused(cards[1]), UIfont, 64, white)
    if selected%6 == 2:
        text_3 = text("%s <<" %evdb.get(cards[2], used), UIfont, 64, selectcolor)
    else:
        text_3 = text("%s" %showused(cards[2]), UIfont, 64, white)
    if selected%6 == 3:
        text_4 = text("%s <<" %evdb.get(cards[3], used), UIfont, 64, selectcolor)
    else:
        text_4 = text("%s" %showused(cards[3]), UIfont, 64, white)
    if selected%6 == 4:
        text_5 = text("%s <<" %evdb.get(cards[4], used), UIfont, 64, selectcolor)
    else:
        text_5 = text("%s" %showused(cards[4]), UIfont, 64, white)
    if selected%6 == 5:
        text_6 = text(">> Next Star >>", UIfont, 64, yellow1)
    else:
        text_6 = text(">> Next Star", UIfont, 64, white)
    gui = pygame.transform.scale(pygame.image.load("Images/ui.png"), (1024, 768))
    screen.blit(gui, (0, 0))
    screen.blit(text_1, (64, 120))
    screen.blit(text_2, (64, 180))
    screen.blit(text_3, (64, 240))
    screen.blit(text_4, (64, 300))
    screen.blit(text_5, (64, 360))
    screen.blit(text_6, (64, 420))
    #pygame.display.update()
    # time.sleep(5)
