## import relevant modules
import random
import math


## Prompt the user and explain rules
print("""
Welcome to the Number Guessing Game.
Guess a Number between the bounds you entered.
""")

lower = int(input("Enter the Lower Bound: "))
upper = int(input("Enter the Upper Bound: "))

## initialize user attempts and score
user_attempts = 0
user_score = 0

## Generate a random secret number 

random_int = random.randint(lower,upper)

## main game loop: evaluate results and display score

while True:
    user_guess = int(input(f"Guess a number between {lower} and {upper}: "))
    user_attempts +=1

    if user_guess == random_int:
        print(f"Congrats! Your Guess {user_guess} is correct. You made {user_attempts} attempts")

    # calculate the user score based on a simple idea that is lwoer the attempts higher the score

        user_score = 1000/user_attempts
        print(f"Your Score: {user_score:.3f}")
        break

    elif user_guess < random_int:
        print(f"Try Guessing a number higher than {user_guess}")

    else:
        print(f"Try Guessing a number lower than {user_guess}")
