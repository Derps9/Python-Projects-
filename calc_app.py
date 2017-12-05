
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



def area():
    width = float(raw_input('enter your width of your square'))
    height = float(raw_input('enter your height here'))
    area= width * height

    print ' the area of your square is ' +str(area)


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
              8. sub- a way to subtract 2 numbers"""



          
while True:
    menu=raw_input('>>>')
    if menu == 'help' or 'h':
        menu()
#will maybe add more calculators/solvers
     if menu == 'bmi' or 'BMI':
        bmi()
    if menu == 'area' or 'Area':
        area()
    if menu == 'kec' or 'Kec':
        kec()
    if menu ==  'mult' or 'Mult':
        mult()
    if menu == 'add' or 'Add':
        add()
    if menu == 'div' or 'Div':
        div()
    if menu == 'sub' or 'Sub':
        sub()
