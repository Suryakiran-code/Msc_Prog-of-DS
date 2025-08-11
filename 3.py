#1 improve the following code:

def check_t(t)
    if t < 0:
        return "Freezing"
    elif t <= 10:
        result = "Cold"
    elif t <= 20
        result = "Mild"
    elif t <= 30:
    result = "Warm"
    else:
        result = Hot
    return result

## Tip: check for (1) syntax errors (e.g. indents, colons, etc); (2) logical erros; (3) good python practice (intuitive variable names, docstring, etc.)



# 2. dice game
# The following dice-game is a simplified version of Seven-Up for one player. you have starting money. If you roll 7 with two dice, you win Â£7 otherwise you lose the difference between the dice sum and 7.
# write one python function

# How long does it normally take to lose all your money? Run the game a 1000 times and calculate the average number of turns before reaching Â£0

# 3. for and while loops
# write a for loop to calculate 5! (1*2*3*4*5)
# now write a while loop for the same calculation

# 4. dictionaries
# consider the following text from the Guardian:
s = "Alien: Earth â€“ Ridley Scottâ€™s terrifying space monster finally comes to TV â€¦ and itâ€™s properly creepy The most cinematic evil creature ever comes to the small screen, courtesy of the brains behind the excellent revamp of Fargo. Itâ€™s a dread-packed, gory watch thatâ€™s hugely entertaining"

#count the number of occurrences of each character in the letter and store in a dictionary in which the keys are characters and values are the counts.
# use a for-loop

#5. analyse the taxis dataset from seaborn. First look at the dataframe:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset('taxis')
print(taxis.head)
print(taxis.shape)
print(taxis.columns)
print(taxis.dtypes)

# print the mean total fare and distance for each taxi company (color)  #tip: use groupby
# print the mean total fare for cash payments in green taxis #tip use query
# plot a barplot of total fare (y) by taxi color (x), grouped by payment type 
# plot total fare against distance, grouped by taxi color. #tip: use a scatterplot


#### GDPR
# what are the 6 principles of data protection?
# What could form a basis for processing data apart from consent?
# data ethics. Discuss the topics: privacy and data anonymisation / bias & fairness / profiling / governance





