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
used = "used"
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
    "Generate" : "%s + %s + %s -> +2 %s" %(red, blue ,yellow, man),
    "Repair" : "-1 %s and -1 %s to +1 HULL" %(blue, yellow),
    "Sacrifice" : "-1 %s -> +1 MAX %s %s %s" %(man, red, blue, yellow),
    "Eat Ship" : "-1 HULL to +1 %s %s %s" %(red, blue, yellow),
   # "EV3" : "-1 %s -> +1 MAX %s" %(man, blue),
   # "EV4" : "-1 %s -> +1 MAX %s" %(man, yellow),
   # "Bad1" : "2 %s to avoid -1 HULL" %yellow,
   # "Bad2" : "2 %s to avoid -2 %s" %(blue, man),
   # "Bad3" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    "Change1" : "-1 %s to +1 %s" %(yellow, red),
    "Change2" : "-1 %s to +1 %s" %(red, blue),
    "Change3" : "-1 %s to +1 %s" %(blue, yellow),
    "Bonus1" : "+2 %s" %(man),
    "Bonus2" : "+1 MAX %s %s %s" %(red, blue, yellow),
    "Bonus3" : "+2 MAX %s" %(red),
    "Bonus4" : "+2 MAX %s" %(blue),
    "Bonus5" : "+2 MAX %s" %(yellow),
    "ExChange1" : "-1 MAX %s to +1 %s %s" %(yellow, red, blue),
    "ExChange2" : "-1 MAX %s to +1 %s %s" %(red, yellow, blue),
    "ExChange3" : "-1 MAX %s to +1 %s %s" %(blue, red, yellow),
    #"Last Save1" : "-1 MAX %s to +2 %s" %(red, blue),
   # "Last Save2" : "-1 MAX %s to +2 %s" %(red, yellow),
   # "Last Save3" : "-1 MAX %s to +2 %s" %(blue, red),
   # "Last Save4" : "-1 MAX %s to +2 %s" %(blue, yellow),
   # "Last Save5" : "-1 MAX %s to +2 %s" %(yellow, blue),
   # "Last Save6" : "-1 MAX %s to +2 %s" %(yellow, red),
    "Big Save1" : "-1 %s to +3 %s" %(man, yellow),
    "Big Save2" : "-1 %s to +3 %s" %(man, blue),
    "Big Save3" : "-1 %s to +3 %s" %(man, red),
    "Power UP1" : "-1 MAX %s to +1 %s" %(red, man),
    "Power UP2" : "-1 MAX %s to +1 %s" %(blue, man),
    "Power UP3" : "-1 MAX %s to +1 %s" %(yellow, man),
    "UP1" : "-2 %s to +1 MAX %s" %(red, red),
    "UP2" : "-2 %s to +1 MAX %s" %(blue, blue),
    "UP3" : "-2 %s to +1 MAX %s" %(yellow, yellow),
    "Plus1" : "-2 %s to +1 %s" %(yellow, man),
    "Plus2" : "-2 %s to +1 %s" %(red, man),
    "Plus3" : "-2 %s to +1 %s" %(blue, man),
    "Plus4" : "-3 %s to +2 %s" %(yellow, man),
    "Plus5" : "-3 %s to +2 %s" %(red, man),
    "Plus6" : "-3 %s to +2 %s" %(blue, man),
    "Benefit1" : "-1 %s to +1 MAX %s" %(blue, blue),
    "Benefit2" : "-1 %s to +1 MAX %s" %(red, red),
    "Benefit3" : "-1 %s to +1 MAX %s" %(yellow, yellow),
    "Benefit4" : "-2 %s to +2 MAX %s" %(blue, blue),
    "Benefit5" : "-2 %s to +2 MAX %s" %(red, red),
    "Benefit6" : "-2 %s to +2 MAX %s" %(yellow, yellow),
    "Lucky Change1" : "-1 %s to +2 MAX %s" %(red, red),
    "Lucky Change2" : "-1 %s to +2 MAX %s" %(blue, blue),
    "Lucky Change3" : "-1 %s to +2 MAX %s" %(yellow, yellow),

}
bonus_events = {
    
}
bad_events = {
    "Bad1" : "2 %s to avoid -2 HULL" %yellow,
    "Bad2" : "2 %s to avoid -2 %s" %(blue, man),
    "Bad3" : "2 %s to avoid -1 %s and -1 %s" %(red, blue, yellow),
    #"Bonus1" : "+2 %s" %(man),
    "Defend" : "2 %s to avoid -1 %s" %(red, man),
    #"Bonus2" : "+1 %s %s %s" %(red, blue, yellow)
    "Need Repair" : "2 %s to avoid -1 %s" %(yellow, man),
    "Get Hurt" : "2 %s to avoid -1 %s" %(blue, man),
    "Goduck" : "-1 %s %s %s to avoid -2 %s" %(red, blue, yellow, man),
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
    #uni = ship["hull"][0] > 0 and ship["red"][0] > 0 and ship["blue"][0] > 0 and ship["yellow"][0] > 0 and ship["man"] > 0
    #uni2 = ship["red"][1] > 0 and ship["blue"][1] > 0 and ship["yellow"][1] > 0
    #uni3 = uni and uni2
    if evt == "Generate" and ship["red"][0] > 0 and ship["blue"][0] > 0 and ship["yellow"][0] > 0:
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
        ship["man"] += 2
    elif evt == "Repair" and ship["blue"][0] >= 1 and ship["yellow"][0] >= 1:
        ship["blue"] -= 1
        ship["yellow"] -= 1
        ship["hull"][0] += 1
    elif evt == "Sacrifice" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["red"][1] += 1
        ship["blue"][1] += 1
        ship["yellow"][1] += 1
    elif evt == "Eat Ship" and ship["hull"][0] >= 2:
        ship["hull"][0] -= 1
        ship["blue"][1] += 1
        ship["red"][1] += 1
        ship["yellow"][1] += 1
    elif evt == "Change1" and ship["yellow"][1] >= 1:
        ship["yellow"][0] -= 1
        ship["red"][0] += 1
    elif evt == "Change2" and ship["red"][1] >= 1:
        ship["red"][0] -= 1
        ship["blue"][0] += 1
    elif evt == "Change3" and ship["blue"][1] >= 1:
        ship["blue"][0] -= 1
        ship["yellow"][0] += 1
    elif evt == "Bonus1":
        ship["man"] += 2
    elif evt == "Bonus2":
        ship["yellow"][1] += 1
        ship["red"][1] += 1
        ship["blue"][1] += 1
    elif evt == "Bonus3":
        ship["red"][1] += 2
    elif evt == "Bonus4":
        ship["blue"][1] += 2
    elif evt == "Bonus5":
        ship["yellow"][1] += 2
    elif evt == "ExChange1" and ship["yellow"][1] >= 1:
        ship["yellow"][1] -= 1
        ship["red"][0] += 1
        ship["blue"][0] += 1
    elif evt == "ExChange2" and ship["red"][1] >= 1:
        ship["yellow"][0] += 1
        ship["red"][1] -= 1
        ship["blue"][0] += 1
    elif evt == "ExChange3" and ship["blue"][1] >= 1 :
        ship["yellow"][0] += 1
        ship["red"][0] += 1
        ship["blue"][1] -= 1 
  #  elif evt == "Last Save1" and ship["red"][1] >= 1:
  #      ship["blue"][0] += 2
  #      ship["red"][1] -= 1
  #  elif evt == "Last Save2" and ship["red"][1] >= 1:
  #      ship["yellow"][0] += 2
  #      ship["red"][1] -= 1
  #  elif evt == "Last Save3" and ship["blue"][1] >= 1:
  #      ship["red"][0] += 2
  #      ship["blue"][1] -= 1
  #  elif evt == "Last Save4" and ship["blue"][1] >= 1:
  #      ship["yellow"][0] += 2
  #      ship["blue"][1] -= 1
  #  elif evt == "Last Save5" and ship["yellow"][1] >= 1:
  #      ship["blue"][0] += 2
  #      ship["yellow"][1] -= 1
  #  elif evt == "Last Save6" and ship["yellow"][1] >= 1:
  #      ship["red"][0] += 2
  #      ship["yellow"][1] -= 1
    elif evt == "Big Save1" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["yellow"][0] += 3
    elif evt == "Big Save2" and ship["man"] >= 1: 
        ship["man"] -= 1
        ship["blue"][0] += 3
    elif evt == "Big Save3" and ship["man"] >= 1:
        ship["man"] -= 1
        ship["red"][0] += 3
    elif evt == "Power UP1" and ship["red"][1] >= 1:
        ship["man"] += 1
        ship["red"][1] -= 1
    elif evt == "Power UP2" and ship["blue"][1] >= 1:
        ship["man"] += 1
        ship["blue"][1] -= 1
    elif evt == "Power UP3" and ship["yellow"][1] >= 1:
        ship["man"] += 1
        ship["yellow"][1] -= 1
    elif evt == "UP1" and ship["red"][0] >= 2:
        ship["red"][1] += 1
        ship["red"][0] -= 2
    elif evt == "UP2" and ship["blue"][0] >= 2:
        ship["blue"][1] += 1
        ship["blue"][0] -= 2
    elif evt == "UP3" and ship["yellow"][0] >= 2:
        ship["yellow"][1] += 1
        ship["yellow"][0] -= 2
    elif evt == "Plus1" and ship["yellow"][0] >= 2:
        ship["man"] += 1
        ship["yellow"][0] -= 2
    elif evt == "Plus2" and ship["red"][0] >= 2:
        ship["man"] += 1
        ship["red"][0] -= 2
    elif evt == "Plus3" and ship["blue"][0] >= 2:
        ship["man"] += 1
        ship["blue"][0] -= 2
    elif evt == "Plus4" and ship["yellow"][0] >= 3:
        ship["man"] += 2
        ship["yellow"][0] -= 3
    elif evt == "Plus5" and ship["red"][0] >= 3:
        ship["man"] += 2
        ship["red"][0] -= 3
    elif evt == "Plus6" and ship["blue"][0] >= 3:
        ship["man"] += 2
        ship["blue"][0] -= 3
    elif evt == "Benefit1" and ship["blue"][0] >= 1:
        ship["blue"][0] -= 1
        ship["blue"][1] += 1
    elif evt == "Benefit2" and ship["red"][0] >= 1:
        ship["red"][0] -= 1
        ship["red"][1] += 1
    elif evt == "Benefit3" and ship["yellow"][0] >= 1:
        ship["yellow"][0] -= 1
        ship["yellow"][1] += 1
    elif evt == "Benefit4" and ship["blue"][0] >= 2:
        ship["blue"][0] -= 2
        ship["blue"][1] += 2
    elif evt == "Benefit5" and ship["red"][0] >= 2:
        ship["red"][0] -= 2
        ship["red"][1] += 2
    elif evt == "Benefit6" and ship["yellow"][0] >= 2:
        ship["yellow"][0] -= 2
        ship["yellow"][1] += 2
    elif evt == "Lucky Change1" and ship["red"][0] >= 1:
        ship["red"][1] += 2
    elif evt == "Lucky Change2" and ship["blue"][0] >= 1:
        ship["blue"][1] += 2
    elif evt == "Lucky Change3" and ship["yellow"][0] >= 1:
        ship["yellow"][1] += 2
    else:
        print("no")
        return False
    return True

def bad_event(evt):
    """Trigger Bad Event"""
    if evt == "Bad1" and ship["hull"][0] >= 1:
        ship["hull"][0] -= 1
    elif evt == "Bad2" and ship["man"] >= 2:
        ship["man"] -= 2
    elif evt == "Bad3" and (ship["blue"][1] >= 1 and ship["yellow"][1] >= 1):
        ship["blue"][1] -= 1
        ship["yellow"][1] -= 1
    elif evt == "Defend" and ship["red"][0] >= 2:
        ship["red"][0] -= 2
    elif evt == "Need Repair" and ship["yellow"][0] >= 2:
        ship["yellow"][0] -= 2
    elif evt == "Get Hurt" and ship["blue"][0] >= 2:
        ship["blue"][0] -= 2
    elif evt == "Goduck" and ship["red"][0] >= 1 and ship["blue"][0] >= 1 and ship["yellow"][0] >= 1:
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1

def bonus_event():
    """Random Bonus Event"""
    bonus = random.random()*100
    if bonus <= 40:
        print("Trigger")

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
  #  bg = pygame.transform.scale(pygame.image.load("Space_Background_4.png").convert_alpha(), (1024, 768))
   # ui_1 = pygame.transform.scale(pygame.image.load("hud.png").convert_alpha(), (1024, 768))
    #screen.blit(bg, [0, 0])
    screen.blit(ui_1, [0, 0])
    screen.blit(text("Star %d: %s" %(ship['current']+1, starname[ship['current']]), UIfont, 64, textcolor), (64, 32))
    screen.blit(text("HULL: "+("O"*ship['hull'][0])+"-"*(ship['hull'][1]-ship['hull'][0]), UIfont, 64, white), (256, 576))
    screen.blit(text("%02d %s " %(ship['man'], man), UIfont, 64, green), (256, 640))
    screen.blit(text("%d/%d %s " %(ship['red'][0], ship['red'][1], red), UIfont, 64, white), (704, 580))
    screen.blit(text("%d/%d %s " %(ship['blue'][0], ship['blue'][1], blue), UIfont, 64, white), (704, 620))
    screen.blit(text("%d/%d %s " %(ship['yellow'][0], ship['yellow'][1], yellow), UIfont, 64, white), (704, 660))      
    pygame.display.update()
   # time.sleep(5)
def showused(card):
    """changeName"""
    return "used" if card == False else card
#bg_big = pygame.image.load("Images/Stars/%d.png" %).convert()
def card(selected, cards, bg):
    """card ui"""
    screen.blit(pygame.image.load("Images/Stars/%d.png" %bg).convert(), [0, 0])
    if selected%6 == 0:
        text_1 = text("%s <<" %events.get(cards[0], used), UIfont, 64, selectcolor)
    else:
        text_1 = text("%s" %showused(cards[0]), UIfont, 64, white)
    if selected%6 == 1:
        text_2=text("%s <<" %events.get(cards[1], used), UIfont, 64, selectcolor)
    else:
        text_2 = text("%s" %showused(cards[1]), UIfont, 64, white)
    if selected%6 == 2:
        text_3 = text("%s <<" %events.get(cards[2], used), UIfont, 64, selectcolor)
    else:
        text_3 = text("%s" %showused(cards[2]), UIfont, 64, white)
    if selected%6 == 3:
        text_4 = text("%s <<" %events.get(cards[3], used), UIfont, 64, selectcolor)
    else:
        text_4 = text("%s" %showused(cards[3]), UIfont, 64, white)
    if selected%6 == 4:
        text_5 = text("%s <<" %events.get(cards[4], used), UIfont, 64, selectcolor)
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
