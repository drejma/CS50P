# https://cs50.harvard.edu/python/2022/psets/0/einstein/
# Calculates E = mc2 based on given mass

def main():
    mass = int(input("m: "))
    print(calculate_energy(mass))


def calculate_energy(mass):
    speed = 300000000
    return mass * pow(speed, 2)


main()