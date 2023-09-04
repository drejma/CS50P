# Week 3 Exceptions

Sources: [Lecture 3](https://cs50.harvard.edu/python/2022/notes/3/)

## Exceptions

- see [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

### SyntaxError

- `SyntaxError` is raised when the parser encounters a syntax error
- example: `print("Hello, world)`

### ValueError

- `ValueError` is raised when an operation or function receives an argument that has the right type but an inappropriate value
- example: `x = int(input("What's x?"))` with user inputting `cat`

### NameError

- `NameError` is raised when a local or global name is not found
 - example: `print(f"x is {x}")` with undefined `x` variable

## try

```python
try:
	x = int(input("What's x?"))
except ValueError:
	print("x is not an integer")
else:
	print(f"x is {x}")
```

- in the code above:
	- `try` defines a block of code where an exception might occur
	- `except ValueError` defines a block of code that runs if `ValueError` is raised in a `try` block
	- `else` defines a block of code that runs if no exceptions occur in a `try` block

## Reprompting

```python
def main():
	x = get_int()
	print(f"x is {x}")


def get_int():
	while True:
		try:
			x = int(input("What's x?"))
		except ValueError:
			print("x is not an integer")
		else:
			return x


if __name__ == "__main__":
	main()
```

- in the code above, `while True` loop is nested in a function - in this case, `return` also breaks out of the loop (`break` is not needed)
- code can be further simplified as follows:

```python
def main():
	x = get_int()
	print(f"x is {x}")


def get_int():
	while True:
		try:
			return int(input("What's x?"))
		except ValueError:
			print("x is not an integer")


if __name__ == "__main__":
	main()
```

## pass

- see [Python Documentation: pass](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
- `pass` statement does nothing; tt can be used when a statement is required syntactically but the program requires no action

```python
def main():
	x = get_int("What's x? ")
	print(f"x is {x}")


def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			pass


if __name__ == "__main__":
	main()
```

## raise

- `raise` allows to programatically raise errors

```python
raise ValueError()
```
