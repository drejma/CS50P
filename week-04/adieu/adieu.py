# https://cs50.harvard.edu/python/2022/psets/4/adieu/
# Practice with inflect package

import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names)}")