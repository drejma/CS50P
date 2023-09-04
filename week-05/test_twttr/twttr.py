# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
# Reimplemented twttr.py for unit testing purposes, see week-02/twttr/

def main():
    input = input("Input: ")
    print(f"Output: {shorten(input)}")


def shorten(str):
    vowels = ["a", "e", "i", "o", "u"]
    str_short = ""
    for char in str:
        if char.lower() not in vowels:
            str_short += char
    return str_short


if __name__ == "__main__":
    main()
