# Week 2 – Project 2 from the book.
# HAZCHEM SIGNS DECODER - This program decodes EAC (Emergency Action Code) and display advise for fire fighters.

fightWith = {'1': 'coarse spray', '2': 'fine spray', '3': 'foam', '4': 'dry agent'}  # first digit of EAC code
safetyPrec = ['P', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']   # Second letter of EAC code

while True:
    EAC = input("\nPlease type EAC code: ").upper() # User input made case insensitive
    if EAC[0] in fightWith and EAC[1] in safetyPrec and \
            (len(EAC) == 3 and EAC[2] == 'E' or len(EAC) == 2): # check if input is an EAC
        print('\nFire fighting instruction for EAC:', EAC )
        print('-' * 38)
        print('Use', fightWith[EAC[0]])  # Takes message from dictionary for first letter
        print('-' * 38)
        if EAC[1] in ('P', 'S', 'W', 'Y',):  # Check if 2nd letter indicates violent substance
            print('Substance is prone to violent or explosive reaction.')
            print('-' * 38)
        if EAC[1] in ('T', 'R', 'W', 'X',):  # Check what kid of protection 2nd letter indicates
            print('Wear liquid-tight suit/chemical protection clothing.')
        else:
            print('Wear breathing apparatus & fire kit.n')
            print('-' * 38)
        if len(EAC) == 3 and EAC[2] == 'E':   # check if 3rd letter is there and if it is 'E'
            print('Public safety hazard. Warn people to stay indoors with doors & windows shut.')
            print('-' * 38)
    else:
        print('\n', EAC, 'is not valid EAC code. Please type again.')

