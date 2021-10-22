"""Events Database"""
import random
import os
ship = {
        "hull" : 7,
        "red" : 10, #♞
        "blue" : 10, #♝
        "yellow" : 10, #♜
        "man" : 10, #♟
        "maxhull" : 10,
        "current" : 0
    }
EV1 = "♞ + ♝ + ♜ = ♟"
EV2 = "♞♞ = ♝"
def ship_hud(ship):
    """Make Ship HUD"""
    print("Stage %d" %ship['current'])
    print("╔"+"═"*20)
    print("║HULL: "+("▮"*ship['hull'])+"▯"*(ship['maxhull']-ship['hull']), end="  ║")
    print(" %d ♟ ║" %ship['man'], end="")
    print(" %d ♞ ║" %ship['red'], end="")
    print(" %d ♝ ║" %ship['blue'], end="")
    print(" %d ♜ ║" %ship['yellow'])
    print("╚"+"═"*20)

def sector_cards():
    """Draw Sector Cards"""
    all_event = [EV1, EV1, EV1, EV1, EV1, EV1] #["Ev%d" %ele for ele in range(10)]
    num = random.random()*100
    if num >= 0 and num < 25:
        num = 3
    elif num >= 25 and num < 75:
        num = 4
    else:
        num = 5
    cards = random_event(all_event, num)
    return cards

def random_event(all_event, num):
    """Random Event"""
    cards = []
    random.shuffle(all_event)
    for _ in range(num):
        cards.append(all_event.pop())
    return cards

def choose_card(cards):
    """Choose Card"""
    while cards:
        ship_hud(ship)
        print("Please choose a card")
        for i in range(len(cards)):
            print("(%d): %s" %(i+1, cards[i]))
        choose = int(input())
        if choose == 0:
            break
        elif choose-1 in range(len(cards)):
            event(cards[i])
            del cards[choose-1]
            #os.system('cls')
        else:
            print("ERROR")

def event(evt):
    """Execute Event"""
    print(evt, EV1)
    if evt == EV1:
        ship["red"] -= 1
        ship["blue"] -= 1
        ship["yellow"] -= 1
        ship["man"] += 1
    else:
        print("no")

# เพิ่มเฉพาะสี
# เพิ่มคน
# เพิ่มค่า Max ของสี
# ทำให้อนาคตเกิดผลดี (บอสลดการ์ด)
# เพิ่มจำนวนการ์ดในอนาคต
