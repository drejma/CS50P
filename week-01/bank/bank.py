# https://cs50.harvard.edu/python/2022/psets/1/bank/
# Gets char and substring from a string

# Prompt user to input greeting
greeting = input("Greeting: ")

# Remove leading and trailing spaces, make it lowercase
greeting = greeting.strip().lower()

# Check if greeting starts with "hello"
if greeting.startswith("hello"):
    print("$0")
# Else check if greeting starts with "h"
elif greeting.startswith("h"):
    print("$20")
# Else print 100
else:
    print("$100")