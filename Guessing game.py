import random

target = random.randint(1, 100) #Generate a random number from 1 to 100

finished = None #None = false; initial boolean control for the while loop

'''
The game starts here.
You guess the number that was generated at the beginning
There will be prompts to tell you if the guessed number
is higher or lower than the target number.
'''
while not finished:
    guess = int(input("Guess from 1 to 100! "))

    if guess == target:
        print("You got it!")
        finished = True
    elif guess > target:
        print("Too big.")
    elif guess < target:
        print("Too low")
        
