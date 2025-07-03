# sumpy library for computer algebra
'''Count the number of dice rolls needed until you see a 6.'''
"""
Exercise 1. Consider the Python function given below. What conclusion can you draw from
the output of this Python code? Do not attempt to explain how this code works.
import sympy

for x in range(1,42):
 p = x**2 - x + 41
 print(x,p,sympy.isprime(p))

Exercise 2. Using nested loops, print a triangle of the character T where the triangle is one
character wide at top and seven characters wide at the bottom.
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT 

Exercise 3. The variable kingdoms is the list defined as follows.
kingdoms = ['Bacteria','Protozoa','Chromista','Plantae','Fungi','Animalia']
Using kingdoms and either slicing or indexing with positive indices, write expressions that
produce the following.
(a) The first item of kingdoms.
(b) The last item of kingdoms.
(c) The list ['Bacteria','Protozoa','Chromista']
(d) The list ['Chromista','Plantae','Fungi']
(e) The list ['Fungi','Animalia']
(f) The empty list.

Exercise 5. Consider the Python string given below. Write Python code that combines the
string methods split() and replace() to return a list of words from this string without
punctuation. Then modify your Python code to make sure all words are converted to
lowercase and all duplicate words are removed.
S = 'First, solve the problem. Then, write the code.'

Exercise 6. Consider the five data structures indicated in the example Python code below.
A = 'dog cat'
B = ['dog','cat']
C = {'dog','cat'}
D = ('dog','cat')
E = {'dog': 'cat'} 
Write Python code to demonstrate whether each of the five data structures used above are
mutable or immutable (one line of Python code per data structure). Each line of Python
code should be executed separately and result in a TypeError if the data structure is
immutable.

Exercise 7. In this exercise, we are interested in calendars.
Image from: https://www.freepik.com/
(a) Recall that we have already looked at the definition of leap years. Explain why there
are exactly 97 leap years over the next 400 year period. Write Python code to
calculate how many days there are in a 400 year period. Is 400 years a whole number
of weeks?
(b) We see from the calendar for 2023 that 1 January 2023 is a Sunday. We can use a
mathematical formula called “Zeller’s algorithm” to calculate the day of the week
(Saturday, Sunday, etc) of any date. To use this algorithm we must treat January and
February as months 13 and 14 of the previous year.

The Python code given below applies Zeller’s algorithm to calculate the day of the
week of 1 January in the given year. Modify this Python code so that it is contained
in a function where year is the input to the function, and the function returns a string
with the name of the day, e.g., ‘Sunday’.
year = 2023
Y = year-1
c = Y//100
y = Y%100
d = 1
m = 13
w = ((13*(m+1))//5 + y//4 + c//4 + d + y - 2*c) % 7
# 0=Sat 1=Sun 2=Mon ... 6=Fri

(c) Since there are 7 days in a week that 1 January could fall on, and each year either is
or is not a leap year, there must only be 14 possible calendars (ignoring things like
public holidays). Suppose you are the owner of a 2023 calendar. Write a Python
loop that calls your function from part (b) and the function from lectures to
determine whether a given year is a leap year, to find the next year that you can
reuse your 2023 calendar. Also determine what calendar from a previous year that
you could reuse for 2024

Group Challenge. Suppose you start with any three-digit number, using at least two
different digits (leading zeros may be needed). Arrange the digits in descending and then
in ascending order to get two three-digit numbers, adding leading zeros if necessary.
Subtract the smaller number from the larger number. Then repeat from the step of
arranging the digits into descending and ascending order. Continue until the same threedigit number is repeated.
For example: start with 023
320 – 023 = 297
 972 – 279 = 693
 963 – 369 = 594
 954 – 459 = 495
 954 – 459 = 495
Hint: This challenge is really about type conversions between int, str and list.
 Step 1. Start with int.
 Step 2. Convert to string, possibly pad it out with zeros. You might find the string
method zfill() useful.
 Step 3. Convert to list, make a copy of this list and sort each list (ascending and
descending). You might find the list methods copy() and sort() useful.
 Step 4. Convert to string and then to int.
 Step 5. Subtract two ints and go back to Step 2.

"""
