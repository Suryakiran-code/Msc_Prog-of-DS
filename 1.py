
# 23 file from revision

#7143CEM Programming for Data Science
# Live coding -- Week 12 -- Wednesday

# Reminder to Mark --> RECORD SESSION


# REVISION


#---
# 1. Practice Exam (current format)

# Q1
import math
s = 2
A = 2*(1+math.sqrt(2))*s**2
D = s*math.sqrt(4+2*math.sqrt(2))
print(A)
print(D)
# A = 20 (count squres or approx)
# D = 5 (use fingers)

# Country, Fossil, Nuclear, Renewables
D = {'Brazil': [ 8700, 169, 8431 ],
'China': [ 25344, 733, 4974 ],
'India': [ 6319, 82, 743 ],
'South Africa': [ 21063, 422, 866 ],
'UK': [ 22509, 1769, 5820 ],
'USA': [ 63836, 6006, 8912 ],
'Europe': [ 28721, 3258, 6345 ]}
print(D)

total_fossil = 0
total_nuclear = 0
total_renew = 0
for k in D:
    L = D[k]
    total_fossil = total_fossil + L[0]
    total_nuclear = total_nuclear + L[1]
    total_renew = total_renew + L[2]
energy = {'Fossil': total_fossil,
          'Nuclear': total_nuclear,
          'Renewables': total_renew}
print(energy)

# Q2
import random
def seven_up_with_boost(money):
    '''Play the seven-up dice game with boost.'''
    keep_going = True
    count_rolls = 0
    boost_used = False
    while(keep_going):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        count_rolls = count_rolls + 1
        print('Dice:',dice1,dice2)
        if (dice1+dice2==7):
            money = money + 7
        elif (dice1+dice2>7):
            money = money - (dice1+dice2-7)
        else:
            money = money - (7-dice1-dice2)
        print('Money:',money)
        if ((money<5) and (boost_used==False)):
            money = money + 10
            boost_used = True
        if (money<=0):
            keep_going = False
    return(count_rolls)

print(seven_up(10))

# -- the end --
