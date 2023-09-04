# https://cs50.harvard.edu/python/2022/psets/4/game/
# Guessing game with random module

from random import randint
from sys import exit


def main():
    # Set random number between 1 and user's input
    number = randint(1, get_positive_int("Level: "))

    while True:
        # Set guess equal to user's input
        guess = get_positive_int("Guess: ")

        # Compare random number and user's guess
        if number > guess:
            print("Too small!")
        elif number < guess:
            print("Too large!")
        else:
            exit("Just right!")


def get_positive_int(prompt):
    while True:
        try:
            i = int(input(prompt))
            if i > 0:
                return i
        except ValueError:
            pass


if __name__ == "__main__":
    main()
