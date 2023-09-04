# https://cs50.harvard.edu/python/2022/psets/4/professor/
# "Little Professor" game

import random


def main():
    level = get_level()
    score = 0

    # Generate ten math problems
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        # Three attempts per math problem
        for attempt in range(3):
            try:
                answer = int(input(f"{a} + {b} = "))

                # Increment score and break attempts on correct answer
                if answer == (a + b):
                    score += 1
                    break
                # Print result and break attempts on third incorrect answer
                elif attempt == 2:
                    print(f"{a} + {b} = {a + b}")
                    break
                # Print "EEE" on incorrect answer
                else:
                    print("EEE")

            except ValueError:
                print("EEE")

    # Print score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            i = int(input("Level: "))
            if 1 <= i <= 3:
                return i
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level in [2, 3]:
        return random.randint(10 ** (level - 1), 10**level - 1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
