"""Random Star Names"""
import random
import string
def random_star_name():
    
    #alph = ""
    #for _ in range(4):
        #alph += random.choice(string.ascii_letters)
    #alph = alph.upper()
    #num = " %d.%03d" %(random.randrange(10), random.randrange(1000))+random.choice(string.ascii_letters)
    #return alph+num
    name = ['kim', 'su', 'pan', 'kua', 'nai',
    'ni', 'kaun', 'niu', 'naum', 'mii',
    'saa', 'tum','mim', 'sim', 'kuu',
    'sim', 'muu', 'tin', 'tu', 'ka']
    
    random.shuffle(name)
    pre = (name.pop()+name.pop()).title()
    suf = "-%02d%s" %(random.randrange(100), random.choice(string.ascii_letters))
    return pre+suf.lower()
print(random_star_name())
def tolist():
    biglist = []
    while True:
        x = input()
        if x == "END":
            break
        biglist.append(x)
    print(biglist)