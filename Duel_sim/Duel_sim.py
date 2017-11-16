print"""
    WELCOME TO 1V1
    DUELING SIM
    ############
    """
def help():
    print"""
    These are the Commands you can execute
    e- exit game
    w- choose your weapon
    e1-e5 choose your opponent
    b- start the battle
    ba- battle command menu
    """
while True:
    command=raw_input('>>>')
if command=='e1':
     e1()
     b1()
if command == 'e2':
    e2()
    b2()
if command =='e3':
    e3()
    b3()
#if command=='e4':
#    e4()
 #   b4()
#if command=='e5':
   # e5()
   # b5()
#will only do 4 and 5 if i have time lol
if command=='e':
     quit()
if command=='w':
    w()
if command=='ba':
    ba()
if command=='help':
    help()

def e1():
    print'ENEMY NAME\n Jack\n Difficulty\n Easy\n'
    print'Has 5hp'
    
def e2():
    print'ENEMYNAME\n Robert\n Difficulty\n Med\n'
    print'HAS 7HP'

def w():
    print"""These are the weapons that you can choose from
    1. Sword
    2. Spear
    3. Staff
    4. Mace """




def ba():
    print"""
    This is the battle command menu
    u- upward strike does 3dmg 
    d- downward strike does 5 dmg
    sl- side slash does 4 dmg 
    st- stab does 7 dmg 
"""

def b1():
    pass


def b2():
    pass


def b3():
   print"""
    You walk into the arena and you wield your weapon
get stabbed ammediatly"""




def kys():
    while True:
        print'Pls Consider suicide'
