# Week 2 Loops

Sources: [Lecture 2](https://cs50.harvard.edu/python/2022/notes/2/)

## while

```python
i = 0
while i < 3:
	print("meow")
	i += 1
```

## for

- `for` loop with `list` variable:

```python
for i in [0, 1, 2]:
	print("meow")
```

- `for` loop with `range()` and with underscore `_` (used in cases where variable does not have any other significance in a code):

```python
for _ in range(3):
	print("meow")
```

- loop with multiplication:

```python
print("meow\n" * 3, end="")
```

## Validating Input

- a common paradigm within Python is to use a `while` loop to validate the input of the user

```python
while True:
	n = int(input("What's n? "))
	if n < 0:
		continue
	else:
		break

for _ in range(n):
	print("meow")
```

- in the code above:
	- `continue` tells Python to go to the next iteration of a loop
	- `break` tells Python to “break out” of a loop early, before it has finished all of its iterations
- `continue` is reduntant in the case above, code can be improved as follows:

```python
while True:
	n = int(input("What's n? "))
	if n > 0:
		break

for _ in range(n):
	print("meow")
```

- code can be further improved by using functions:

```python
def main():
	number = get_number()
	meow(number)


def get_number():
	while True:
		n = int(input("What's n? "))
		if n > 0:
			break
	return n


def meow(n):
	for _ in range(n):
		print("meow")


if __name__ == "__main__":
	main()
```

- in the code above:
	- if conditions are met, `get_number()` function returns `n` variable
	- code can be further simplified by moving `return n` in place of `break`

## Iteration with Lists

- see [Python Documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- `print()` items at certain positions in `list`:

```python
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
```

- `print()` all items in `list`:

```python
students = ["Hermione", "Harry", "Ron"]

for student in students:
	print(student)
```

## len

- see [Python Documentation: len](https://docs.python.org/3/library/functions.html?highlight=len#len)
- `print()` items including their positions in `list`:

```python
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
	print(i + 1, students[i])
```

## Dictionaries

- see [Python Documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- `dict` is a data structure of keys and values

```python
students = {
	"Hermione": "Gryffindor",
	"Harry": "Gryffindor",
	"Ron": "Gryffindor",
	"Draco": "Slytherin"
}

# Print value (house) of a key (Hermione)
print(students["Hermione"])

# Print all keys (students) and their value (houses)
for student in students:
	print(student, students[student], sep=", ")
```

### List of Dictionaries

```python
students = [
	{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
	{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
	print(student["name"], student["house"], student["patronus"], sep=", ")
```

- in the code above:
	- `list[]` of multiple `dict{}` is created
	- `None` expresses an absence of value

## Nested Loops

```python
def main():
	print_column(3)


def print_column(height):
	for _ in range(height):
		print("#")


def print_column_alter(height):
	print("#\n" * height, end="")


if __name__ == "__main__":
	main()
```

```python
def main():
	print_row(4)


def print_row(width):
	print("?" * width)


if __name__ == "__main__":
	main()
```

```python
def main():
	print_square(3)


def print_square(size):
	for i in range(size):
		print_row(size)


def print_row(width):
	print("#" * width)


if __name__ == "__main__":
	main()
```
