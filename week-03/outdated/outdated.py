# https://cs50.harvard.edu/python/2022/psets/3/outdated/
# Formats date: "M/D/YYYY" or "MMMM D, YYYY" to "YYYY-MM-DD"

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:

        # Assumed "M/D/YYYY" input
        if "/" in date:
            month, day, year = date.strip().split("/")
            month = int(month)

        # Assumed "MMMM D, YYYY" input
        elif "," in date:
            month, day, year = date.replace(",", "").strip().split(" ")
            month = months.index(month) + 1

        # Convert day str to int (applies to both ifs)
        day = int(day)

        # Print and break if day and month as valid values
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    # ValueError: Fails to split input; NameError: Fails to initiate variable
    except (ValueError, NameError):
        pass