# 21 file 
# 7143CEM Programming for Data Science
# Live coding -- Week 11 -- Monday

# Reminder to Mark --> RECORD SESSION


# Recap and Support


# Menu:
#   (1) Portfolio submission box
#   (2) Exam information


#---
# 1. Portfolio support

#---
# 2. Python examples
#    * More sources for Python practice


# dictionary
D = {'name': 'Iron Man',
     'name': 'Anthony Hopkins'}
print(D)
D['city'] = 'Coventry'
D['city'] = 'London'
print(D)
D = {'name': ['Iron Man','Anthony Hopkins']}
print(D)
print(D['name'][0])

# dice game
import random
def dice_game():
    '''docstring goes here'''
    prize_money = 0
    count_rolls = 0
    keep_going = True
    while (keep_going):
        a = random.randint(1,6)
        b = random.randint(1,6)
        count_rolls = count_rolls + 1
        print('Dice:',a,b)
        prize_money = prize_money + a**2 - b**2
        print('Prize money:',prize_money)
        if (prize_money>=200):
            print('WINNER')
            keep_going = False
        elif (prize_money<=-200):
            print('LOSER')
            keep_going = False
    return(count_rolls)

print(dice_game())

# dice game with numpy to roll many dice
import numpy as np
def another_dice_game():
    prize_money = 0
    count_rolls = 0
    keep_going = True
    while (keep_going):
        dice = np.random.randint(1,7,10)
        count_rolls = count_rolls+1
        print(dice)
        prize_money = prize_money + np.mean(dice)
        if (np.min(dice)>=4):
            keep_going = False
    return(count_rolls)

print(another_dice_game())

# -- the end --


