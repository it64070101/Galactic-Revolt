"""Random Star Names"""
import random
import string
def random_star_name():
    name = ['kim', 'su', 'pan', 'kua', 'nai',
    'ni', 'kaun', 'niu', 'naum', 'mii',
    'saa', 'tum','mim', 'sim', 'kuu',
    'sim', 'muu', 'tin', 'tu', 'ka']
    
    random.shuffle(name)
    pre = (name.pop()+name.pop()).title()
    suf = "-%02d%s" %(random.randrange(100), random.choice(string.ascii_letters))
    return pre+suf.lower()

starname = [random_star_name() for _ in range(10)]