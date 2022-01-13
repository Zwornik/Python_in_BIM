table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }



while True:
    arabList = []
    flag = 2000
    romanNo = (input('Please type Roman number:')).upper()
    for i in romanNo:
        if i not in table:
            print('\nInvalid input. Try again.')
            break
        else:
            arabList.append(table[i])
    for i in arabList:
        if i > flag:
            print('\nInvalid input. Try again. >>>>')
            break
        else:
            flag = i
    flag2 = flag3 = 7
    for i in arabList:
        if i == flag == flag2 == flag3:
            print('\nInvalid input. Try again. x4')
            break
        else:
            print(i, flag, flag2, flag3)
            flag3 = flag2
            flag2 = flag
            flag = i
    print('OK', arabList)