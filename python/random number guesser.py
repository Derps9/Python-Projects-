import random
print ('Welcome to guess the number guess a number between 0-9')
for i in range(10):
    print(i)
x=int(raw_input (' Put your answer here:'))
y=random.randint(0,9)
print(y)
if x==y:
    print('Good job')
elif x!=y:
    print('you suck try again')
quit()

    



    

    
    
