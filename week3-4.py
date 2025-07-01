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