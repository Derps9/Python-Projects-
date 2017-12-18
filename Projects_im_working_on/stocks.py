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
def Amazon():
    stock=random.randint(1,100)
    if stock >50:
        print'Amazon stock price has gone up'
    if stock <50:
        print'Amazon stock has gone down'
def Target():
    stock=random.randint(1,100)
    if stock >50:
        print'Target stock price has gone up'
    if stock <50:
        print'Target stock has gone down'
def Walmart():
    stock=random.randint(1,100)
    if stock >50:
        print'Walmart stock price has gone up'
    if stock <50:
        print'Walmart stock has gone down'
def credits():
    print"""
        CREDITS
        MADE BY: RYAN
         FROM THE 
        VSOSS TEAM"""
def applestock():
    pass
def start():
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
            applestock()

        if command == 'investMicrosoft':
            microsoftstock()

        if command ==  'investTarget':
            targetstock()

        if command == 'investAmazon':
            amazonstock()

        if command == ' investWalmart':
            walmartstock()

        if command == 'fullsim':
            for i in range(50):
                Apple()
                Microsoft()
                Amazon()
                Walmart()
                Target()
        if command == 'exit':
            quit()
        if command == 'credits':
            credits()
for i in range(10000):
    command1 = raw_input('>>>')
    if command1 == 'start':
        start()
    if command1 ==  'rules':
        rules()
    if command1 == 'menu':
        menu()
    if command1 ==  'credits':
        credits()
print'this is the menu'
