"""Galactic Revolt!"""
import random
import os
import EventDB as edb

def mainloop():
    """Main Loop"""
    boss = 1
    while edb.ship['current'] < boss:
        cards = edb.sector_cards()
        edb.choose_card(cards)
        os.system('cls')
        edb.ship['current']  += 1
    print('Boss Stage')

# Game Start
mainloop()
