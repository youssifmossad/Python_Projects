"""
===========================================================
Number Guessing Game
===========================================================

Description:
------------
This is a simple Python console game where the computer
randomly selects a number between 1 and 100, and the user
tries to guess it.

Features:
---------
- Random number generation (1 to 100)
- User input for guessing
- Feedback after each guess (higher/lower hints)
- Tracks number of attempts
- Ends when the correct number is guessed

Author:
-------
(Youssif Mossad)

Date:
-----
(6/12/2026)

===========================================================
"""
import random
number=random.randint(1,100)
n=0
while True:
    n+=1
    x= int(input("enter the number plz: "))
    if x== number :
        print("You Win")
        break
    elif x>number:
        print("You are Higher")
    elif x<number:
        print("You are Lower")    
    else:    
        print("Try Again")
print("You have tried ",n," times")
print("Thanks for playing the game")        