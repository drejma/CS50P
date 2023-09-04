# https://cs50.harvard.edu/python/2022/psets/5/test_bank/
# Reimplemented bank.py for unit testing purposes, see week-01/bank/

def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
