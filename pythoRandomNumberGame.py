# Create a random number and ask the user to guess it.
# If the user guesses correctly, tell them they won.
# If the user guesses incorrectly, tell them they lost.


import random


def main():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it.")
    guess = 50
    while guess != number:
        guess = int(input("What's your guess? "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("You got it!")
    print("The number was", number)


main()




