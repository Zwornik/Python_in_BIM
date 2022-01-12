# Week 2 – Project 2 from the book.
# HAZCHEM SIGNS DECODER - This program decodes EAC (Emergency Action Code) and display advise for fire fighters.

fightWith = {'1': 'coarse spray', '2': 'fine spray', '3': 'foam', '4': 'dry agent'}
safetyPrec = ['P', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']

while True:
    EAC = input("\nPlease type EAC code: ").upper()
    if EAC[0] in fightWith and EAC[1] in safetyPrec and (len(EAC) == 3 and EAC[2] == 'E' or len(EAC) == 2):
        print('\nFire fighting instruction for EAC:', EAC, '\n'
              '----------------------------')
        print('Use', fightWith[EAC[0]])
        print('----------------------------')
        if EAC[1] in ('P', 'S', 'W', 'Y',):
            print('Substance is prone to violent or explosive reaction.')
        if EAC[1] in ('P', 'R', 'W', 'X',):
            print('Wear liquid-tight suit/chemical protection clothing.')
        else:
            print('Wear breathing apparatus & fire kit.\n'
                  '----------------------------')
        if len(EAC) == 3 and EAC[2] == 'E':
            print('Public safety hazard. Warn people to stay indoors with doors & windows shut.\n'
                  '----------------------------')
    else:
        print('This is not the EAC code. Please type again.',EAC)
