# https://cs50.harvard.edu/python/2022/psets/2/twttr/
# Omits vowels of an input

# Inital data
vowels = ["a", "e", "i", "o", "u"]
output = ""

# Prompt user for an input
input = input("Input: ")

# Iterate over each character
for char in input:

    # Omit character from an output, if it's a vowel
    if char.lower() not in vowels:
        output += char

# Print output
print(f"Output: {output}")