# https://cs50.harvard.edu/python/2022/psets/2/coke/
# Prompting user until conditions are met

# Inital data
coins = [5, 10, 25]
total = 50

while True:
    # Print due amount
    print(f"Amount Due: {total}")

    # Prompt user for input
    insert = int(input("Insert Coin: "))

    # Deduct from total if input is in list of accepted coins
    if insert in coins:
        total -= insert

    # Print owed amount and exit if total is less than or equal to 0
    if total <= 0:
        print(f"Change Owed: {-total}")
        break