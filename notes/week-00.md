# Week 0 Functions, Variables

Sources: [Lecture 0](https://cs50.harvard.edu/python/2022/notes/0/)

## Command Line

- `code hello.py` creates or opens hello.py
- `python hello.py` executes (interprets) hello.py

## Hello World

```python
print("Hello, world")
```

- in the code above, `print()` is a function that displays its arguments (in brackets) on the screen

## Variables and Comments

- see [Python Documentation: Data Types](https://docs.python.org/3/library/datatypes.html)

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("Hello, " + name)
```

- in the code above:
	- `#` indicates a comment
	- `name` is a variable
	- `input()` is a function that returns user's input

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("Hello,", name)
```

- in the code above, some functions such as `print()` can take multiple arguments, separated by a comma

## Named Parameters

- values of named parameters can be overwritten in order to change function's behaviour
- by default, `print()` function uses named parameter `end` with a value `'\n'`, which automatically creates a line break when run

```python
# Ask the user for their name
name = input("What's your name? ")

print("Hello,", end="")
print(name)
```

- by default, `print()` function also uses named parameter `sep` with a value `' '`, which automatically separates arguments with a blank space

```python
# Ask the user for their name
name = input("What's your name? ")

print("Hello,", name)
print("Hello, ", name, sep="")
```

- for more information, see [Python Documentation: print](https://docs.python.org/3/library/functions.html#print)

## Strings

- see [Python Documentation: str](https://docs.python.org/3/library/stdtypes.html#str)

### Escape Character

- backslash `\` tells the compiler that the following character should be considered a quotation mark in the string

```python
print("Hello, \"friend\"")
```

### Formatting Strings

- f-string `f` is the most elegant way to work with strings

```python
# Ask the user for their name
name = input("What's your name? ")

print(f"Hello, {name}")
```

### String Methods

- methods are built-in functions
- some of the `str` methods are:
	- `strip` strips all the whitespaces on the left and right of the string
	- `title` title cases the string
	- `split` divides a string based on a separator

```python
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Print the output
print(f"hello, {first}")
```

## Integers

- see [Python Documentation: int](https://docs.python.org/3/library/functions.html?highlight=float#int)

### Interactive Mode

- text editor window in a compiler is not needed to run Python code
- terminal command `python` activates a mode to run live, interactive code

```
$ python
>>> 1 + 1
2
>>> print("Hello, world")
Hello, world
```

### Basic Operations and Type Casting

- `input()` function always returns a string
- to convert string to an integer, type casting such as `int()` is needed

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

## Float

- see [Python Documentation: float](https://docs.python.org/3/library/functions.html?highlight=float#float)

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")
```

- in the code above:
	- `float()` converts (casts) `input` string to a float
	- `round(number[, ndigits]` rounds a `number` to `ndigits`; if `ndigits` parameter is not specified (in documentation, `[]` means *optional*), `number` is rounded to the closest integer
	- `f"{z:,}"` is an f-string for thousands separator (in this case, `1000` -> `1,000`)

### Floating Imprecision

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
```

- in the code above, `f"{z:.2f}"` is an f-string for decimal places (in this case, `0.66666...` -> `0.66`)

## def

- custom functions

```python
def main():
	name = input("What's your name? ")
	hello(name)


def hello(to="world"):
	print("Hello,", to)


if __name__ == "__main__":
	main()
```

- in the code above:
	1. `main()` function, which holds the main code, is defined
	2. `hello()` function, which accepts `to` parameter (of a default value `"world`), is defined
	3. `main()` function is called

### Scope

- **variable exists only in the context, in which it was defined**

### Returning Values

```python
def main():
	x = int(input("What's x? "))
	print("x squared is", square(x))


def square(n):
	return n * n


if __name__ == "__main__":
	main()
```

- in the code above:
	- `return` returns a value from a function
	- `n * n` can be replaced by `n ** 2`, or `pow(n, 2)`
	