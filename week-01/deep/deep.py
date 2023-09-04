# https://cs50.harvard.edu/python/2022/psets/1/deep/
# If-else practice

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.strip().lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")