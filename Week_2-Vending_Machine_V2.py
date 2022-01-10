# Week 2 – Project 1 from the book.
# VENDING MACHINE
coinTypes = ('1p', '2p', '5p', '10p', '20p', '50p', '1gbp', '2gbp')
menu = ('0', '1', '2', '3', '4', '5')
snacksNames = {'1':'CHOCOLATE BAR', '2':'SESAME BAR', '3':'MILK BAR', '4': 'PURE GLUTEN BAR', '5':'NO GLUTEN BAR'}
nominations = {1:20 , 2:10, 5:6, 10:4, 20:2, 50:1, 100:1, 200:1 } # machine coins container
startMoneyIn = 0    # Money in machine at the start of the day
moneyIn = 0         # Money in machine when checked
coins = 0   # sum of user coins
spent = 0   # money spent by user
moneyReturn = 0 # amount to be returned to user

def menuMessage():  # introduction message
    global coins, spent, basket
    coins = spent = 0
    basket = {'CHOCOLATE BAR': 0, 'SESAME BAR': 0, 'MILK BAR': 0, 'PURE GLUTEN BAR': 0,
              'NO GLUTEN BAR': 0}  # user shopping basket

    input('\n\nPress enter')
    print('\n Welcome new customer! I am perfect Vending Machine. How can I help? \n\n'
      'MENU:\n'
      'Type one of the following to insert a coin: 1p, 2p, 5p, 10p, 20p, 50p, 1GBP or 2GBP\n'
      'or type one of below to select an option:\n'
                 '1 - Chocolate bar     - 10p\n'
                 '2 - Sesame bar        - 10p\n'
                 '3 - Milk bar          - 10p\n'
                 '4 - Pure gluten bar   - 10p\n'
                 '5 - No gluten bar     - 10p\n'
                 '6 - Display sales summary\n'
                 '0 - Confirm your choice\n\n'
      'Please insert a coin.')

def coinReturn(coins):
    toReturn = coins
    #print(nominations)
    if toReturn:
        print('Here you have £{:.2f} change in following coins:'.format(toReturn/100))
    noCoins = []
    for i in reversed(nominations):
        if toReturn == i:  # return change of a single coin
            quotient = 1
            toReturn = toReturn - i  # reduce balance to return
            if i in (100, 200):  # plural singular text format
                print('   {q} coins of £{m}'.format(q=quotient, m=int(i / 100)))
            else:
                print('   {q} coins of {m}p'.format(q=quotient, m=i))
            nominations[i] = nominations[i] - 1  # subtracts coin from coins container
        elif toReturn > i:  # return change of more than a single coins
            quotient = toReturn // i
            while quotient > nominations[i]:  # check if coins are available
                quotient -= 1
                if i not in noCoins:
                    noCoins.append(i)
            toReturn = toReturn - i * quotient
            if nominations[i] > 0:
                if i in (100, 200):  # plural singular text format
                    print('   {q} coins of £{m}'.format(q=quotient, m=int(i / 100)))
                else:
                    print('   {q} coins of {m}p'.format(q=quotient, m=i))
            nominations[i] = nominations[i] - quotient  # subtracts coin from coins container
    if bool(noCoins):
        print('\nCoins of:')
        for i in noCoins:
            if i in (100, 200):
                print('   £{}'.format(i / 100))
            else:
                print('   {}p'.format(i))
        print('are unavailable so I gave you change in lower nominations.')
    if toReturn > 0:
        print(f'Upsss! \n'
              f'I contain no more change so I am not able to give you remaining £{toReturn} change.\n'
              f'Please write to Prime Minister to get your money back.')
    return toReturn

for i in nominations:                   #money in machine at the start of the day
    startMoneyIn = startMoneyIn + i * nominations[i]
print('start money =',startMoneyIn)
menuMessage()

while True:
    print('You have £{:.2f}'.format(coins / 100))
    #print('spent:', spent)
    #print(nominations)
    userIn = input()                    #user input
    if userIn.lower() in coinTypes:     # main menu
        coin = userIn.lower()          # makes case insensitive
        if coin == '1gbp':
            coin = '100'
        elif coin == '2gbp':
            coin = '200'
        coin = coin.strip('pgb')  # get rid of letters
        coin = int(coin)  # convert to integer
        nominations[coin] += 1 # adds coins to machine container
        coins = coins + coin
        if coins >= 10:
            print('Type 1 to 5 to select a snack, or type 0 to confirm, or insert more coins')
        else:
            print('Add more coins.')
    elif userIn in ('1', '2', '3', '4', '5') and coins >= 10:   # selecting a snack
        coins = coins - 10
        basket[snacksNames[userIn]] = basket[snacksNames[userIn]] + 1
        print('You have selected:')
        spent = spent + 10
        for i in basket:
            if basket[i] > 0:
                if basket[i] > 1:                               # selection plural info
                    message = '{} {}S'
                    print(message.format(basket[i], i))
                else:                                           # selection info
                    print(basket[i], i)
        print('\nType "0" to confirm your selection, or insert a coin or')
        if coins >= 10:
            print('type 1 to 5 to select another snack.')
    elif userIn in ('1', '2', '3', '4', '5') and coins < 10:    # snack with no funds
        print('Insufficient founds for a snack.\n'
              'Please insert a coin.')
    elif userIn == '0':                                         # confirm selection
        if spent == 0:
            print('You have not selected anything')
            coinReturn(coins)
        else:
            print('Here is your:')
            for i in basket:
                if basket[i] > 0:
                    if basket[i] > 1:                           # selection plural info
                        message = '{} {}S'
                        print(message.format(basket[i], i))
                    else:                                       # selection info
                        print(basket[i], i)
            print('HAVE A GOOD MEAL!\n')
            coinReturn(coins)
            menuMessage()
    elif userIn == '6':                                         # display sales summary
        moneyIn = 0
        for i in nominations:
            moneyIn = moneyIn + nominations[i] * i
        print(f'I sold for £{(moneyIn-startMoneyIn)/100} today')
        menuMessage()
    else:                                                       # wrong user input
        print('Invalid choice, try again.')


