# Week 2 – Python Exercises
# ROMAN NUMBER CONVERTER - Converts Roman number to Arabic one.

table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }

while True:
    arabList = []
    arabNo = 0
    flag = 2000
    romanNo = (input('Please type Roman number:')).upper()
    for i in romanNo:  # check if all characters are in Roman numbering
        if i not in table:
            print('\nInvalid input. Try again.')
            break
        else:
            arabList.append(table[i]) # transform string to list of numbers
    flag2 = flag3 = 7
    for i in arabList:  # checks if there are no more than 3 repetitions
        if i == flag == flag2 == flag3:
            print('\nInvalid input. Try again. x4')
            break
        else:
            #print(i, flag, flag2, flag3)
            flag3 = flag2
            flag2 = flag
            flag = i
    for i in arabList:  # checks if there are no repetitions of 5,50,500
        if i == flag and i in (5,50,500):
            print('\nInvalid input. Try again. 5,50,500')
            break
        else:
            flag = i

    flag = 2000
    #for i in arabList:  # checks if consequential numbers are smaller than predecessor
        #if i > flag:
            #print('\nInvalid input. Try again. >>>>')
            #break
        #else:
            #flag = i
    flag = flag2 = 0
    n = 0
    print(arabList)
    for i in arabList:  # checks if consequential numbers are smaller than predecessor
        print('EEE', flag2, flag, i, n)
        if i > flag and flag in (1,10,100,1000) and flag/i in (0.2, 0.1) and \
                (flag2 == 0 or flag2 >= flag * 10) and flag2 > i:
            arabList.pop(n-1)
            arabList.pop(n-1)
            arabList.insert(n-1, i-flag)
            n += 1
            print('---', flag2, flag, i, n)
        else:
            flag2 = flag
            flag = i
            n += 1
    #for i in romanNo:

    print('OK', arabList)
    for i in arabList:
        arabNo += i
    print(arabNo)
