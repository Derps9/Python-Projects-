print """
    Welcome to BMI tester """  
height=float(raw_input('enter your height here in inches'))
weight=float(raw_input('enter your weight here in lbs'))
bmi= weight/(height **2) *703
print'your bmi is '+str(bmi) 
if bmi >30:
    print'your some fat boi'
if bmi <30:
    print'u good fam'



