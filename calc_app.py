
def bmi():
    print """
        WELCOME TO BMI tester"""
    height= float(raw_input('enter your height here in inches'))
    weight= float(raw_input('enter your weight in lbs'))

    bmi= weight/(height**2) *703
    print ' your bmi is'+str(bmi)

    if bmi >30:
     print ' get off the bigmacs'
    if bmi <30:
        print ' your pretty good keep it up'
def ohm1():
    print'this is to find amps'
    volts= float(raw_input('enter your voltage here'))
    resistance= float(raw_input('enter your resistance here'))
    amps= volts/resistance
    print amps
def ohm2():
    print 'this one finds volts'
    amps= float(raw_input('this is your amps'))
    resistance= float(raw_input('this is your resistance'))
    volts= amps*resistance
    print volts


def ohm3():
    print'this one finds resistance'
    volts= float(raw_input('enter your volts here'))
    amps= float(raw_input('enter your amps here'))
    resistance= volts/amps
    print resistance



def area():
    width = float(raw_input('enter your width of your square'))
    height = float(raw_input('enter your height here'))
    area= width * height

    print ' the area of your square is ' +str(area)

def kec():
    mass= float(raw_input('enter the mass of the object'))
    velocity= float(raw_input('enter your velocity of the object'))
    kinetic= mass * velocity**2 /2
    print ' your velocity is ' +str(kinetic)

def add():
    first=float(raw_input('enter your first number'))
    second=float(raw_input('enter your second number'))
    answer= first + second
    print answer
def mult(): 
    first=float(raw_input('enter your first number'))
    second=float(raw_input('enter your second number'))
    answer= first *  second
    print answer
def div():
    first=float(raw_input('enter your first number'))
    second=float(raw_input('enter your second number'))
    answer= first /  second
    print answer
def sub():
    first=float(raw_input('enter your first number'))
    second=float(raw_input('enter your second number'))
    answer= first -  second
    print answer
def pe():
    mass= float(raw_input('enter your mass here '))
    height= float(raw_input('enter your height here'))

    poten= mass * 96.04 * height
    print poten
def cir():
    diameter= float(raw_input('enter your diameter here'))
    pi=3.14
    circumference= diameter * pi
    print circumference
def menu():
    print """ Welcome to the start menu
              Commands you can do are
              1. help- returns to the menu
              2. bmi- calculates your bmi
              3. area- determines the area of a square
              4. kec- a kinetic energy calculator
              5. Mult- a way to multiply 2 numbers
              6. add- a way to add 2 numbers
              7. div- a way to divide 2 numbers
              8. sub- a way to subtract 2 numbers
              9. pe- a way to find the gravitational potential energy
              10. cir- circumference of a circle
              11. e- to exit the program
              12. ohm1- to find amps
              13. ohm2- to find voltage
              14. ohm3- to find resistance
                WILL ADD MORE IN FUTURE
"""
def credits():
    print' Credits \n made by: Ryan \n of the vsoss company \n version 1.8'


          
while True:
    command=raw_input('>>>')
    if command == 'help':
        menu()
    if command == 'bmi':
        bmi()
    if command == 'area':
        area()
    if command == 'kec':
        kec()
    if command ==  'mult':
        mult()
    if command == 'add':
        add()
    if command == 'div':
        div()
    if command == 'sub':
        sub()
    if command == 'pe':
        pe()
    if command == 'cir':
        cir()
    if command == 'credits':
        credits()
    if command == 'e':
        exit()
    if command == 'ohm1':
        ohm1()
    if command == 'ohm2':
        ohm2()
    if command == 'ohm3':
        ohm3()
    ##################
    #WILL ADD MORE IN# 
    #THE FUTURE THIS #
    #IS VERSION 1.8  #
    # MADE BY RYAN   #
    ##################
