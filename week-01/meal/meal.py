# https://cs50.harvard.edu/python/2022/psets/1/meal/
# Splitting and calculating with strings

def main():
    # Prompt user for time
    time = input("What time is it? ")

    # Calculate time
    converted_time = convert(time)

    # Print time for breakfast/lunch/dinner
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()