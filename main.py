#!/usr/bin/env python 
#marr and junn

import random 

def main():
    """start a song guessing game"""
    print("HELLO >< lets play Guess The Song Name ! (SZA edition)")

    SZA = [
        "kill bill",
        "snooze",
        "Open Arms",
        "Big Boy",
        "Good Days",
        "All The Stars",
        "The Weekend",
        ]

    x = random.choice(SZA)
    
    guess = None 

    while x !=guess:

        guess = str(input("what song am i thinking of? : "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!૮ ˶ᵔ ᵕ ᵔ˶ ა ".format(guess))
            break
        else:
            print ("You guessed {}.Unfortunaly you got the wrong answer.please try again!".format(guess))
    
main() 