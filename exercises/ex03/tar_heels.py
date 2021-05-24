"""An exercise in remainders and boolean logic."""

__author__ = "730230918"


# Begin your solution here...

from random import randint
Number: int= int(input("Enter an int:")) 
some_int: int = randint(0, 1000)
b: bool = Number % 2 == 0
a: bool = Number % 7 == 0


if b:
    print("TAR")

if a:
    print("HEELS")

if a and b:
    print("TAR HEELS")
else:
    print("CAROLINA")