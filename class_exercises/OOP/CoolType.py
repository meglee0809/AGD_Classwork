import time
from colorama import Fore,Back,Style

def cooltype(text='Rian',interval=0.03,nextline = True):
    for item in text:
        print(item,end='',flush=True)
        time.sleep(interval)
    if nextline:
        print('\n')
def cooltypecolour(text='Rian',interval=0.05,colour=Fore.MAGENTA,nextline = True):
    print(colour)
    cooltype(text,0.05)
    print(Style.RESET_ALL)
    if nextline:
        print('\n')
def coolinput(text='',interval=0.01):
    for item in text:
        print(item,end='')
        time.sleep(interval)
    return input()

cooltype("megan")

#toms thing
class Player:
    def __init__(self,pname,phealth,pstrength,px,py,pmoves,pcolour,peffects):
        self.name = pname
        self.health = phealth
        self.strength = pstrength
        self.x = px
        self.y = py
        self.moves = pmoves
        self.colour = pcolour
        self.effects = peffects