# questions from week 3 - 4 from all aula pages ------------------
"""
Module - A module is a collection of variables and functions that are grouped together in a single file.
  The math module provides access to lots of mathematical functions and constants (such 𝜋). 
"""

"""import math;
print(math.sqrt(16))
print(math.pi)"""

"""import random
print(random.randint(1,6))"""
"""
import random
def count_dice_rolls(value_wanted):
    finished = False
    count=0
    while(not finished):
        d=random.randint(1,6)
        count=count+1
        print("rolled",d)
        print("count so far is",count)
        finished=(d==value_wanted)
    return(count)
print(count_dice_rolls(3))"""


# A set is an unordered collection of distinct items.

"""vowels={"a","e","i","o","u"}

print(vowels)"""

#A dictionary is an unordered mutable collection of key/value pairs

car={"make":"audi","model":"A3"}
print(car["make"])
print(car.keys())
print(car.values())

def leap_year(year):
    '''Calculate whether a given year is a leap year.'''
    if (year%400==0):
        result = True
    elif (year%100==0):
        result = False
    elif (year%4==0):
        result = True
    else:
        result = False 
    return(result)
print('========')
print(leap_year(2024))
print(leap_year(1900))
print(leap_year(2023))
print(leap_year(2000))


# WORKING OUT NOTES:
#
#   do something 30 times
#   each time through loop one of cd, cw, cl
#     increased by 1
#   cd+cw+cl = 30 at end
#
#       a=0  a=1  a=2
#   b=0  cd   cw   cl
#   b=1  cl   cd   cw
#   b=2  cw   cl   cd
#
#   diagonal is cd, when a==b
#   each of cd,cw,cl appears once in each row
#     and once in each column
#   if we swap value of a and b - swap cw/cl
#
#   game: win, loss, draw
#     cw = count_win
#     cl = count_loss
#     cd = count_draw

#===================

import random
def rock_paper_scissors():
    '''Play rock paper scissors and count
    number of wins, losses, and draws.'''
    count_draw = 0
    count_win  = 0
    count_loss = 0
    for i in range(30):
        a = random.randint(0,2)  # player A
        b = random.randint(0,2)  # player B
        # 0=rock, 1=paper, 2=scissors
        # --> count wins for player A
        #       rock beats/smashes scissors
        #       scissors beats/cuts paper
        #       paper beats/covers rock
        if (a==0):
            if (b==0):
                count_draw = count_draw+1
            elif (b==1):
                count_loss = count_loss+1
            else:
                count_win = count_win+1
        elif (a==1):
            if (b==0):
                count_win = count_win+1
            elif (b==1):
                count_draw = count_draw+1
            else:
                count_loss = count_loss+1
        else:
            if (b==0):
                count_loss = count_loss+1
            elif (b==1):
                count_win = count_win+1
            else:
                count_draw = count_draw+1
    return(count_win,count_draw,count_loss)

print(rock_paper_scissors())


