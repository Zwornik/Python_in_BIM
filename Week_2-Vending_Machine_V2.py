# Week 2 – Project 1 from the book in Python 3.9
# VENDING MACHINE - this is very clever and profitable vending machine. If it does not contain coins for
# change you will be left with no change and your lost money will add to machine profit :)

coinTypes = ('1p', '2p', '5p', '10p', '20p', '50p', '1gbp', '2gbp')
menu = ('0', '1', '2', '3', '4', '5')
startSnacksIn = {'CHOCOLATE': 5, 'MUESLI BAR': 5, 'APPLE': 5, 'POPCORN': 5,
            'CHEESE PUFFS': 5}  # Snacks in the machine at the beginning of the day
snacksNames = {'1':'CHOCOLATE', '2':'MUESLI BAR', '3':'APPLE', '4': 'POPCORN', '5':'CHEESE PUFFS'}
nominations = {1: 20, 2: 10, 5: 6, 10: 4, 20: 2, 50: 1, 100: 1, 200: 1}  # machine coins container
startMoneyIn = 0  # Money in machine at the start of the day
coins = 0  # sum of user's coins
spent = 0  # money spent by user
moneyReturn = 0  # amount to be returned to user



def menuMessage():
    """display INTRODUCTION MESSAGE"""

    global coins, spent, basket, flag
    coins = spent = 0
    flag = True # prevents from sales summary display during transaction.
    basket = dict.fromkeys(startSnacksIn, 0)  # initiate empty user's shopping basket
    input('\n\nPress enter to start using machine\n__________________________________\n')
    print('\n Welcome new customer! I am perfect Vending Machine. How can I help? \n\n'
          'MENU:\n'
          'Type one of the following to insert a coin: 1p, 2p, 5p, 10p, 20p, 50p, 1GBP or 2GBP\n'
          'or type 1-6 to select an below option:\n'
          '1 - Chocolate bar     - 10p\n'
          '2 - Sesame bar        - 10p\n'
          '3 - Milk bar          - 10p\n'
          '4 - Pure gluten bar   - 10p\n'
          '5 - No gluten bar     - 10p\n'
          '6 - Display sales summary\n'
          '0 - Confirm your choice\n\n'
          'Please insert a coin.')


def coinReturn(aaa):
    """CHANGE RETURN MODULE"""

    global coins
    change = aaa
    noCoins = []  # list of unavailable coins

    if change:
        print('Here you have £{:.2f} change in following coins:'.format(change / 100))

    for i in reversed(nominations):  # "i" is a coin nominal
        if change == i:  # return change of a single coin
            quotient = 1
            change -= i  # reduce balance to return
            if i in (100, 200):  # printing no. of coins to return, plural/singular text formatting
                print('   {q} coins of £{m}'.format(q=quotient, m=int(i / 100)))
            else:
                print('   {q} coins of {m}p'.format(q=quotient, m=i))
            nominations[i] -= 1  # subtracts coin from coins container
        elif change > i:  # return change of more than a single coins
            quotient = change // i
            while quotient > nominations[i]:  # check if coins are available
                quotient -= 1
                if i not in noCoins:
                    noCoins.append(i)  # adds unavailable coin to list of unavailable coins
            change -= i * quotient  # reduces money to return by number of available nominal
            if nominations[i] > 0:  # printing no. of coins to return
                if i in (100, 200):  # plural/singular text formatting
                    print('   {q} coins of £{m}'.format(q=quotient, m=int(i / 100)))
                else:
                    print('   {q} coins of {m}p'.format(q=quotient, m=i))
            nominations[i] -= quotient  # subtracts coins from coins container

    # MESSAGE ABOUT UNAVAILABLE COINS
    if bool(noCoins):
        print('\nCoins of:')
        for i in noCoins:
            if i in (100, 200):  # plural/singular text formatting
                print('   £{}'.format(i / 100))
            else:
                print('   {}p'.format(i))
        print('are unavailable so I gave you change in lower nominations.')

    # MESSAGE ABOUT NO MONEY FOR RETURN AVAILABLE
    if change > 0:
        print(f'Upsss! \n'
              f'I contain no more change so I am not able to give you remaining £{coins} change.\n'
              f'Please write to Prime Minister to get your money back.\n'
              f'SORRY :-(')

# LOADING SUPPLIES TO THE MACHINE
iniInput = input('\nPlease load snacks (press 1) or skip (press Enter). \n'
      '5 items of each snack will be automatically loaded if you skip loading procedure\n')
if iniInput == '1':
    for i in startSnacksIn:
        while True:
            iniInput = input(f'How many {i}S are you adding?')
            if iniInput.isdigit():  # Verifying if user typed integer
                startSnacksIn[i] = int(iniInput)  # Loading snacks to machine
                break
            else:
                print('Wrong input. Please type integer number.')
    print(f'You have loaded: {startSnacksIn}')
snacksIn = startSnacksIn.copy()  # Copy initial supplies to current supply

# INITIAL PART
for i in nominations:  # money in the machine at the start of the day
    startMoneyIn = startMoneyIn + i * nominations[i]
print('I contain £{:.2f} of change.'.format(startMoneyIn/100))
menuMessage()

# MAIN MENU
while True:
    print('You have £{:.2f}'.format(coins / 100))
    userIn = input('---->')  # user input
    #print('-' * 14)
    if userIn.lower() in coinTypes:  # user adds a coin
        flag = False
        coin = userIn.lower()  # makes user input case insensitive
        if coin == '1gbp':
            coin = '100'
        elif coin == '2gbp':
            coin = '200'
        coin = coin.strip('pgb')  # get rid of letters
        coin = int(coin)  # converts user input to integer
        nominations[coin] += 1  # adds coin to machine container
        coins += coin   # adds coin to user's coins
        if coins >= 10:
            print('Select a snack (1-5), confirm (0) or insert more coins')
        else:
            print('Add more coins.')
    elif userIn in ('1', '2', '3', '4', '5') and coins >= 10:  # user selected a snack
        flag = False
        snackName = snacksNames[userIn] # Selected snack name
        if snacksIn[snackName] < 1: # checking if selected snack available
            print(f'No more {snackName}S available. \n'
                  f'Please select another snack (1-5), confirm (0) or add a coin')
        else:   # if snack is available
            coins -= 10  # reducing user's money
            basket[snackName] += 1  # adding snack to user's basket
            snacksIn[snackName] -= 1   # reducing amount of available snack
            print('You have selected:')
            spent += 10  # calculating money spent by user
            for i in basket:
                if basket[i] > 0:
                    if basket[i] > 1:  # confirmation of snack selection (plural)
                        message = '{} {}S'
                        print(message.format(basket[i], i))
                    else:  # confirmation of snack selection (singular)
                        print(basket[i], i)
            print('\nConfirm selection (0) or insert a coin.')
            if coins >= 10:
                print('Select another snack (1-5).')
    elif userIn in ('1', '2', '3', '4', '5') and coins < 10:  # user selects snack with no funds
        print('Insufficient founds for a snack.\n'
              'Please insert a coin.')
    elif userIn == '0':  # user confirms snack selection
        flag = False
        if spent == 0:
            print('You have not selected anything')
            coinReturn(coins)
        else:  # dispensing snack
            print('Here is your:')
            for i in basket:
                if basket[i] > 0:
                    if basket[i] > 1:  # info about snack dispensed plural
                        message = '{} {}S'
                        print(message.format(basket[i], i))
                    else:  # info about snack dispensed singular
                        print(basket[i], i)
            print('HAVE A GOOD MEAL!\n')
            coinReturn(coins) # go to change return module
            menuMessage()
    elif userIn == '6' and flag:  # user displays sales summary
        moneyIn = 0  # Money in machine when checked
        print('I sold today:')
        for i in snacksIn:  # printing sold snacks
            if startSnacksIn[i] - snacksIn[i] > 0:
                print('{} {}S'.format(startSnacksIn[i] - snacksIn[i], i))
        for i in nominations:  # calculating money in the machine now from coins in container
            moneyIn += nominations[i] * i
        print(f'for £{(moneyIn - startMoneyIn) / 100}')
        menuMessage()
    else:  # wrong user input
        print('Invalid choice, try again.')
