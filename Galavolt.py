"""Galactic Revolt!"""
from math import fabs
import random
import os
import EventDB as edb

def mainloop():
    """Main Loop"""
    stars = 2 #จำนวนดาวที่จะไป
    while edb.ship['current'] < stars or win == True:
        edb.bonus_event()
        cards = edb.sector_cards()
        win = edb.choose_card(cards)
        os.system('cls')
        edb.ship['current']  += 1
    if win == False:
        print("Game Over")
    else:
        print('Boss Stage')

# Game Start
mainloop()