import random

def start():
    print """
        Welcome to random person guesser for Mrs.Zimmermons 4th period class 
Type guess to get a random person from this class"""

def guess():
    person= random.randint(1,25)
    if person == 1:
        print'Ryan'    
    if person == 2:
        print 'Jacob'
    if person == 3:
        print'lucas'
    if person == 4:
        print'aiden'
    if person == 5:
        print'Bucari'
    if person == 6:
        print 'isiah'
    if person == 7:
        print'Devin'
    if person == 8:
        print 'Zach'
    if person == 9:
        print 'kayla'
    if person == 10:
        print 'blake'
    if person == 10:
        pass
    if person == 11:
        pass
    if person == 12:
        pass
    if person == 13:
        pass
while True:
    command= raw_input('>>>')
    
    if command == 'start':
        start()
    if command == 'pick':
        guess()
