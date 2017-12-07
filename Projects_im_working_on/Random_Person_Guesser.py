import random

def start():
    print """
        Welcome to random person guesser for Mrs.Zimmermons 4th period class 
Type guess to get a random person from this class"""

def guess():
    person= random.randint(1,28)
    if person == 1:
        print'Faheem'    
    if person == 2:
        print 'Andrew'
    if person == 3:
        print'David'
    if person == 4:
        print'Ryan'
    if person == 5:
        print'Bakarri'
    if person == 6:
        print 'Alex'
    if person == 7:
        print'Jordyn'
    if person == 8:
        print 'isiah'
    if person == 9:
        print 'Ben'
    if person == 10:
        print 'Ana'
    if person == 11:
        print'Charity'
    if person == 12:
        print 'Gabriella'
    if person == 13:
        print 'Devin'
    if person == 14:
        print 'Zach'
    if person == 15:
        print 'Amy'
    if person == 16:
        print 'Sydney'
    if person == 17:
        print 'Austin'
    if person == 18:
        print 'Aiden'
    if person == 19:
        print ' Alyssa'
    if person == 20:
        print 'Ashlyn'
    if person == 21:
        print 'Lucas'
    if person == 22:
        print 'Jacob'
    if person == 23:
        print 'Christine'
    if person == 24:
        print 'Blake'
    if person == 25:
        print 'Kayla'
    if person == 26:
        print 'Jaden'
    if person == 27:
        print 'Hailey'
    if person == 28:
        print 'Brianna'
    if person == 29:
        print 'pagoaga'

while True:
    command= raw_input('>>>')
    
    if command == 'start':
        start()
    if command == 'pick':
        guess()
