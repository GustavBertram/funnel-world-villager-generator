import random

def d(dice = 1, faces = 6):
    total = 0
    for n in range(dice):
        total += random.randint(1,faces)
    return str(total)

def choose(*args):
    return random.choice([args])

def rollstat(name):
    stat = int(d(3,6))
    bonus = [0,0,0,-3,-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3]
    return name, stat, bonus[stat]
