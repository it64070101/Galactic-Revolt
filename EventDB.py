"""Events Database"""
import random
import os
ship = {
        "hull" : [5, 10],
        "red" : [1, 1], #♞ Trooper
        "blue" : [1, 1], #♝ Supporter
        "yellow" : [1, 1], #♜ Engineer
        "man" : 9, #♟
        "current" : 0
    }
red = "♞"
blue = "♝"
yellow = "♜"
man = "♟"

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
    "Recovery" : "2%s to +1%s" %(man, ship["hull"][0]),
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
    "Badass1" : "4%s to avoid -2 HULL" %yellow,
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
        if ship["hull"][0] < 0 or ship["red"][0] < 0 or ship["blue"][0] < 0 or ship["yellow"][0] < 0 or ship["man"] < 0:
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
            for values in bad_events:
                if values in cards:
                    print('------------------------Trigger', values)
                    
        else:
            print("ERROR")

def event(evt): #ใช้งานอีเวนต์
    """Trigger Event"""
    if evt == events["Recruit"]:
        ship["red"][0] -= 1
        ship["blue"][0] -= 1
        ship["yellow"][0] -= 1
        ship["man"] += 1
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
        
