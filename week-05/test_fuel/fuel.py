# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
# Reimplemented fuel.py for unit testing purposes, see week-03/fuel/

def main():
    while True:
        try:
            pct = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(pct))


def convert(fraction):
    x, y = fraction.split("/", maxsplit=1)
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if (x < 0) or (y < 0) or (x > y):
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
