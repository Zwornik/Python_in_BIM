# Week 7 – Python Exercises
# Fertiliser Potency - finds how many months fertiliser needs to loose 50% of its effectiveness if it looses 6% per month.

monthPot = 0.06 # loos of the potency per month
potency = 100 # overal potency of the fetaliser after X months
month = 1

while potency > (1-monthPot)*50:
    print('Month {} - potency {:.2f}%'.format(month, potency))
    potency = (1 - monthPot) * potency
    month += 1
