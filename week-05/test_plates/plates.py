# https://cs50.harvard.edu/python/2022/psets/5/test_plates/
# Reimplemented plates.py for unit testing purposes, see week-02/plates/

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Must contain 2-6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Must start with at least 2 letters, must not contain special symbols
    if not s[:2].isalpha() or not s.isalnum():
        return False

    # Find first number
    first_num = ""
    for c in s:
        if c.isnumeric():
            first_num = c
            break

    # Must not contain 0 as first number
    if first_num == "0":
        return False

    # Must not contain anything but numbers after the first one
    if first_num != "" and not s[s.index(first_num):].isnumeric():
        return False

    # Otherwise, plate is valid
    return True


if __name__ == "__main__":
    main()