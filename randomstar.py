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
    name = ["numa", "preva", "kelso", "lola", "kelli", "kabo", "sere", "siz", "lak", "sof", "nod", "li", "iru", "ka"]
    random.shuffle(name)
    pre = (name.pop()+name.pop()).title()
    suf = "-%02d%s" %(random.randrange(100), random.choice(string.ascii_letters))
    return pre+suf
print(random_star_name())