#Assignment 1:  Guessing game

#randomly generate number between 0 and 100
from random import random
num_to_guess =  int(random()*100)


correct_guess = False
num_guess = 0

while( not correct_guess ):

    #Ask for guess
    guess = eval( input(" What is your guess: ") )
    
    #Check for valid input
    if( (guess < 0)  or  (guess > 100) ):
        print("You moron!")

    elif( guess < num_to_guess ):
        print(" Too low bruh !!!")
    

    elif( guess > num_to_guess ):
        print(" Too high bruh !!!")

    elif( guess == num_to_guess ):
        correct_guess = True
        

    num_guess = num_guess + 1

#if here, correct guess
print("Correct!!!")
print("Num Guesses:  ", num_guess )






