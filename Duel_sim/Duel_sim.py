#!/usr/bin/env python

print """   WELCOME TO 1V1\n    DUELING SIM\n   ############"""
def help():
    print """    These are the Commands you can execute\n    e,q- exit game\n    w- choose your weapon\n    enemy1-3 choose your opponent\n \
   b- start the battle\n    ba- battle command menu"""

def spear():
    namewep1='spear'
    print namewep1
def staff():
    namewep2='staff'
    print namewep2
def mace():
    namewep3='mace'
    print namewep3

def enemy1():
    print 'ENEMY NAME\n Jack\n Difficulty\n Easy\n'
    print 'Has 5hp'
    
def enemy2():
    print 'ENEMYNAME\n Robert\n Difficulty\n Med\n'
    print 'HAS 7HP'

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
    namewep4= 'sword'
    print namewep4

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
        battle_command=raw_input('>>>')
        if battle_command=='u':
            print'you have done 3 dmg with' + spear()
            print'Your enemy staggers and dies'
            victory_credits() 
        if battle_command=='st':
            print'you have done 7 damage with' + spear()
            print'your enemy shreiks and dies squirming on the floor'
            victory_credits()
        if battle_command=='sl':
            print'you have done 4 damage with' + spear()
            print' your enemy grasps his side as he falls to the ground'
            victory_credits
        if battle_command=='d':
            print'Your enemy is cut in half you win the battle with' +spear()
            victory_credits()
        if battle_command=='u1':
            print'you smack him in the legs he falls and dies' + staff()
            print' dealing 3 damage'
            victory_credits()
        if battle_command=='st1':
            print'you stab your enemy with'+ staff()
            print' he throws up his guts everywhere \n you win the match by dealing 7 damage'
            victory_credits() 
        if battle_command=='sl1':
            print 'you smash his ribs and he crumples to the ground you grasp your' + staff()
            print ' as he falls to the ground dealing 4 damage'
            victory_credits()
        if battle_command== 'd1':
            print' your enemy blocks your downward strike but you counter with another and you kill him dealing 5 damage with '+ sword()
            victory_credits()

def kys():
    while True:
        print'Pls Consider suicide'
def victory_credits():
    print"""
        YOU MADE IT 
        GAME:
        DUELING SIM 
        MADE BY:
        RYAN DALE 
        FROM THE VSOSS TEAM 
        THANK YOU FOR PLAYING"""
    x=raw_input('are you sure you want to quit')
    if x=='y' or 'yes':
        exit()

while True:
    command=raw_input('>>>')

    if command=='enemy1':
     enemy1()
     b1()

    if command=='enemy2':
     enemy2()
     b2()

    if command=='enemy3':
     enemy3()
     b3()
    
    if command=='spear':
     spear()
    
    if command=='mace':
     mace()

    if command=='staff':
     staff()

#if command=='e4':
#    e4()
 #   b4()
#if command=='e5':
   # e5()
   # b5()
#will only do 4 and 5 if i have time lol

    if command=='e' or command=='q':

         exit()
    if command=='w':
         w()
    if command=='ba':
        ba()
    if command=='help':
        help()
    if command=='sword':
        sword()
        kys()
    if command=='kys' or command=='boi':
        kys()
