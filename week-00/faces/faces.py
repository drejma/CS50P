# https://cs50.harvard.edu/python/2022/psets/0/faces/
# Replaces input smileys

def main():
    coverted_input = convert(input())
    print(coverted_input)


def convert(what):
    return what.replace(":)", "🙂").replace(":(", "🙁")


main()