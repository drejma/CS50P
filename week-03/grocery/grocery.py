# https://cs50.harvard.edu/python/2022/psets/3/grocery/
# Updating dicts

# Create empty dict
grocery_list = {}

# Prompt user for an input until break
while True:
    try:
        item = input().upper()

        # If key exists, increment its value (alt. if item in grocery_list)
        try:
            grocery_list[item] += 1

        # If key doesn't exist, create it with value 1 (alt. else)
        except KeyError:
            grocery_list[item] = 1

    # On CTRL + D, break
    except EOFError:
        break

# Print alphabetically sorted keys with their values
for i in sorted(grocery_list):
    print(grocery_list[i], i, sep = " ")