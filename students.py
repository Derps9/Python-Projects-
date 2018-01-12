print' welcome to grade thing lol '
for i in range(10):
    grade= float(raw_input('enter the grade of the student here 1-10'))
    if grade>4.5 and grade >0: 
        print'fail'
    if grade <6.5:
        print ' ok'
    if grade < 8.5:
        print' great'
    if grade <9:
        print'almost perfect/ perfect'
    else:
        print' error incorrect number given'
 
