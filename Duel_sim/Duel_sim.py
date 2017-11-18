print """
    WELCOME TO 1V1
    DUELING SIM
    ############"""
def help():
    print """
    These are the Commands you can execute
    e- exit game
    w- choose your weapon
    e1-e5 choose your opponent
    b- start the battle
    ba- battle command menu"""

def spear():
    namewep1='spear'

def staff():
    namewep2='staff'

def mace():
    namewep3='mace'

def enemy1():
    print'ENEMY NAME\n Jack\n Difficulty\n Easy\n'
    print'Has 5hp'
    
def enemy2():
    print'ENEMYNAME\n Robert\n Difficulty\n Med\n'
    print'HAS 7HP'

def enemy3():
    print'ENEMYNAME\n KEKBOI MCRARE PEPE Difficulty\n Hard'
    print'HAS 10GBP'

def w():
    print"""These are the weapons that you can choose from
    1. Sword
    2. Spear
    3. Staff
    4. Mace """
def sword():
    print"""
    This is the sword 
    this is one of the weapons you can use in 
    your battle scenarios
    
"""
def ba():
    print"""
    This is the battle command menu
    u- upward strike does 3dmg 
    d- downward strike does 5 dmg
    sl- side slash does 4 dmg 
    st- stab does 7 dmg"""

def b1():
    pass

def b2():
    pass

def b3():
    for i in range(10):
     battle_command1=raw_input('>>>')
     if battle_command1=='u':
         print'you have done 3 dmg with' + spear()

def kys():
    while True:
        print'Pls Consider suicide'
while True:
    command=raw_input('>>>')

    if command=='enemy1':
     enemy1()
     b1()

    if command == 'enemy2':
     enemy2()
     b2()

    if command =='enenmy3':
     enemy3()
     b3()
    
    if command =='spear':
     spear()
    
    if command =='mace':
     mace()

    if command =='staff':
     staff()

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
    if command == 'sword':
        sword()
    if command == 'boi'
        pass

