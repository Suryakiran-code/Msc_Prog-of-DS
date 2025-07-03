# Some warnings, tricks and tips
# dont use break statement 
# use below to stop 
i = 0
keep_going = True
while (keep_going and (i<10)):
 print(i)
 if (i==7):
  keep_going = False
 i += 1

"""
Exercises
Exercise 1. We wish to modify our Brute Force string search implementation so that the
INNER for loop (with index k) can end early as soon as a character mismatch is found.
(a) One way to do this would be to introduce a break statement. Explain why this is very
poor programming practice.
 else:
 print(' --> character mismatch')
 match_found = False
 break
(b) Show how you can replace the INNER for loop (with index k) with a while loop to
achieve this modification. The result is the Naïve algorithm for string search.
(c) A “regular expression” (sometimes called “regex”) is a pattern that includes some
“wildcard” characters. For example the wildcard ‘.’ (a single full stop) matches ANY
character. Modify your Python implementation of the Naïve algorithm for string
search to include the ‘.’ wildcard character in the needle (not in the haystack).
Exercise 2. It is claimed that the following Python code is able to swap the values of two
variables. Check whether this claim is true or not by adding some print statements and
considering at least two examples. Include your final code and output in your answer.
a = a + b
b = a - b
a = a - b
Hint: Notice that the question says “values” not “numbers”.
Exercise 3. Consider the Python code given below where each line creates an empty data
structure of a particular type. Rewrite each line in Python so that it does not use any of the
words str, list, set, tuple or dict, but does achieve the same result. Give only Python code in
your answer.
Data Science Python Labs (2023/24 Semester 2)
20
A = str()
B = list()
C = set()
D = tuple()
E = dict()
Exercise 4. Briefly distinguish between the Python “in” operator and the “index” method.
Give Python examples (positive and negative) of both “in” and “index”, using the example
list given below. Which of your examples could not be used directly for the example set
given below? Include both Python code and output in your answer.
A = list('hello')
A = set('hello')
Exercise 5. The Python code given below constructs the famous “Fibonacci sequence” in
mathematics. Briefly explain what F[-2] and F[-1] do in this Python code. Also
investigate how the value F[-1]/F[-2] is related to 1+√5
2
. Include both Python code and
output in your answer.
F = [0,1]
for i in range(2,20):
 F.append(F[-2]+F[-1])
Exercise 6. Consider the following Python code to store the birthdays of group of people.
birthdays = [('Boris', '19 June 1964'),
 ('Harry', '28 July 1993'),
 ('Donald', '14 June 1946'),
 ('Guido', '31 January 1956'),
 ('Guido', '13 April 1570')]
(a) Describe the data structure in the Python code above in words. Hint: pay attention to
the brackets.
Data Science Python Labs (2023/24 Semester 2)
21
(b) Write Python code to print out each name followed by the month of their birthday in
the form “Boris was born in June”. You must extract the name and month from the
data structure using Python.
(c) What issue arises if you convert the data structure above to a dictionary using the
following Python code and why does it occur? Suggest a way to implement the
birthday information above in a dictionary where the key is a person’s name.
D = dict(birthdays)
Exercise 7. Consider the following variant of the dice game “Ship, captain, crew”. A single
player starts by rolling four fair 6-sided dice. The aim of the game is to roll a six (the “ship”)
and a five (the “captain”) with any two of the four dice, and then the score is the sum of the
other two dice (the “ship’s cargo”). If the player gets neither six nor five then they continue
by rolling all four dice again. If they get a six but not a five, then they keep the six and
continue by rolling only three dice with the aim of getting a five. They continue rolling until
they have both a six and a five, and then their score is the sum of the other two dice.
Write a single Python function to implement the dice game described above. Your Python
code should add to (and adapt if you wish) the partial code given below. The output should
include the values of the dice rolled at each roll, when ship and captain have been seen, and
the score (sufficient to check that your code works correctly).
In your answer, please include both Python code and output from two example runs (one
where the ship and captain are collected on the same roll and one where the ship is collected
before the captain is collected).
def ship_game():
 keep_going = True
 num_dice = 4
 while (keep_going):
 if (num_dice==4):
 # -- add your Python code here –-
 elif (num_dice==3):
 # -- add your Python code here –-


Group Challenge. In Exercise 1, we have modified the Brute Force string search Python code
so the INNER for loop (with index k) is replaced by a while loop that is able to end early if a
mismatch of characters is found (this is now the Naïve algorithm).
(a) Modify the Python implementation of the Naïve algorithm so that the OUTER
for loop (with index i) is replaced by a while loop that does the same job.
(b) Consider the special case of a pattern (needle) where all the characters in needle are
different. If a mismatch is found in the INNER loop, it would be possible to skip over
the next few characters of haystack to where needle would have ended. Modify your
Python code to implement this idea.
(c) The idea in part (b) is a special case of the famous Knuth-Morris-Pratt algorithm. In
what way is the general case of Knuth-Morris-Pratt more complicated? Give a small
example but do not write further Python code







"""