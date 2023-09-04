# https://cs50.harvard.edu/python/2022/psets/3/taqueria/
# Handling exceptions with dicts

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        # Get title-cased input
        item = input("Item: ").title()

        # Get value on an input from dict, add it to total
        total += menu[item]

        # Print total
        print(f"Total: ${total:.2f}")
    except KeyError:
        # If input doesn't exist in dict, continue without warning
        pass
    except EOFError:
        # On CTRL + D, break
        print()
        break