# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Converts camelCase to snake_case

# Prompt user for camelCase input
input = input("camelCase: ")

# Initiate output
output = ""

# Iterate over each character of an input
for char in input:

    # If character is uppercase, replace it
    if char.isupper():
        output += char.replace(char, "_" + char.lower())

    # Otherwise, keep it as is
    else:
        output += char

# Print output
print(f"snake_case: {output}")