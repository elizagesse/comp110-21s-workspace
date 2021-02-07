"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730386298"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

fortune_cookie: int = randint(1,4)

if fortune_cookie == 1:
    print("good things are coming your way")
else:
    if fortune_cookie == 2:
        print("yummy food is in your future")
    else:
        if fortune_cookie == 3:
            print("good news is close by")
        else:
            print("look forward to tomorrow")

print("Now, go spread positive vibes! ")


