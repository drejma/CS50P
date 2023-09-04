# https://cs50.harvard.edu/python/2022/psets/3/fuel/
# Handling exceptions

while True:
    try:
        # Prompt user for a fraction, save its dividend and divisor as x, y ints
        x, y = [int(s) for s in input("Fraction: ").split("/", maxsplit=1)]

        # Calculate int percentage
        pct = round(x / y * 100)

    except (ValueError, ZeroDivisionError):
        # On errors, re-prompt user without warnings
        pass

    else:
        # Break re-prompting if x and y are positive and if x is less than or equal to y
        if (x >= 0) and (y > 0) and (x <= y):
            break

# Print how much fuel is in a tank
if pct >= 99:
    print("F")
elif pct <= 1:
    print("E")
else:
    print(f"{pct}%")
