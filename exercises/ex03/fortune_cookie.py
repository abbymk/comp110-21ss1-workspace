"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730230918"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
#from random import randint

# Begin your solution here...
choice: int = int(input("Pick a number between 1 and 4..."))
if choice == 4 :
     print("Your fortune cookie says...")
     print("The early bird gets the worm, but the second mouse gets the cheese.")
     print ("Now, go spread positive vibes!")
else:
    if choice == 3:
        print("Your fortune cookie says...")
        print("People learn little from success, but much from failure.")
        print("Now, go spread positive vibes!")
    else:
        if choice == 2:
            print("Your fortune cookie says...")
            print("The fortune you seek is in another cookie.")
            print("Now, go spread positive vibes!")
        else:
            if choice == 1:
                print("Your fortune cookie says...")
                print("Don't pursue happiness, create it.")
                print("Now, go spread positive vibes!")
        
        
    

    









