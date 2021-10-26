"""Mock-up for present"""
import random
import os
ship = {
        "hull" : [10, 10],
        "red" : [1, 1], #♞ Trooper
        "blue" : [1, 1], #♝ Supporter
        "yellow" : [1, 1], #♜ Engineer
        "man" : 9, #♟
        "current" : 1
    }
red = "♞"
blue = "♝"
yellow = "♜"
man = "♟"

def ship_hud(ship): #สร้างหน้าบอก Resource
    """Make Ship HUD"""
    print("Star %d" %ship['current'])
    print("╔"+"═"*49+"╗")
    print("║HULL: "+("▮"*ship['hull'][0])+"▯"*(ship['hull'][1]-ship['hull'][0]), end="  ║")
    print(" %02d %s ║" %(ship['man'], man), end="")
    print(" %d/%d %s ║" %(ship['red'][0], ship['red'][1], red), end="")
    print(" %d/%d %s ║" %(ship['blue'][0], ship['blue'][1], blue), end="")
    print(" %d/%d %s ║" %(ship['yellow'][0], ship['yellow'][1], yellow))
    print("╚"+"═"*49+"╝")

ship_hud(ship)
print("(1) -1♞ → +1♟")
print("(2) -1♟ → +1MAX♜")
print("(3) -2♝ to avoid -3 HULL")
input()
ship["man"] += 1
ship["red"][0] -= 1
os.system('cls')
ship_hud(ship)
print("(1) -1♟ → +1 MAX♜")
print("(2) -2♝ to avoid -6 HULL")
input()
ship["man"] -= 1
ship["yellow"][1] += 1
os.system('cls')
ship_hud(ship)
print("(1) -2♝ to avoid -6 HULL")
input()
os.system('cls')
ship["hull"][0] -= 6
ship["current"] += 1
ship["red"][0] = ship["red"][1]
ship["yellow"][0] = ship["yellow"][1]
for _ in range(9):
    ship_hud(ship)
    print("(1) Test")
    print("(2) Test")
    print("(3) Test")
    input()
    ship["current"] += 1
    os.system('cls')
print("Boss Stage")
ship["current"] = 0
ship_hud(ship)
print("(1) -7 ♟")
print("(2) -7 ♞")
print("(3) -7 ♝")
print("(4) -7 ♜")
print("(5) -7 ♟ & -7 ♞ & -7 ♝ & -7 ♜")
input()
ship["hull"][0] -= 4
ship["man"] -= 7
os.system('cls')
ship_hud(ship)
print("--Game Over--")