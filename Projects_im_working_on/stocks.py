import random
print""" WELCOME TO THE STOCK MARKET EXCHANGE SIMULATOR"""
def rules():
    print"""
 you have 50 days to watch the stock prices rise and fall between the different companies you can choose to invest
 in these companies to make there chances of failing less but you can only invest in one company per day once to
 see how which companies end up the highest"""
def menu():
    print ' welcome to the stock exchange game'
    print""" these are the companies you can invest in 
            1. Apple
            2. Microsoft
            3. Amazon
            4. Target
            5. Walmart"""
def Apple():
    stock=random.randint(1,100)
    if stock >50:
        print'Apple stock price has gone up'
    if stock <50:
        print'Apple stock has gone down'
def Microsoft():
    stock=random.randint(1,100)
    if stock >50:
        print'Microsoft stock price has gone up'
    if stock <50:
        print'Microsoft stock has gone down'
#make it working for the rest of the companies
def Amazon():
    pass   
def Target():
    pass
def Walmart():
    pass
for i in range(50):
    command= raw_input('>>>')
    if command == 'nxtday':
        Apple()
        Microsoft()
        Amazon()
        Target()
        Walmart()
    if command == 'rules':
        rules()
    if command == 'investApple':
       # investApple()
        pass
    if command == 'investMicrosoft':
        pass
    if command == 'fullsim':
        for i in range(50):
            Apple()
            Microsoft()
    if command == 'exit':
            quit()


