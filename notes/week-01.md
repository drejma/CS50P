# Week 1 Conditionals

Sources: [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/)

## if Statements

- see [Python Documentation: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
else:
	print("x is equal to y")
```

## and, or, not equal

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
	print("x is not equal to y")
else:
	print("x is equal to y")
```

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
	print("x is not equal to y")
else:
	print("x is equal to y")
```

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
	print("Grade: A")
elif score >=80 and score < 90:
	print("Grade: B")
elif score >=70 and score < 80:
	print("Grade: C")
elif score >=60 and score < 70:
	print("Grade: D")
else:
	print("Grade: F")
```

## Chaining Comparison Operators

```python
score = int(input("Score: "))

if 90 <= score <= 100:
	print("Grade: A")
elif 80 <= score < 90:
	print("Grade: B")
elif 70 <= score < 80:
	print("Grade: C")
elif 60 <= score < 70:
	print("Grade: D")
else:
	print("Grade: F")
```

## Modulo

- modulo `%` operator in programming allows one to see if two numbers divide evenly or divide and have a remainder

```python
x = int(input("What's x? "))

if x % 2 == 0:
	print("Even")
else:
	print("Odd")
```

## Creating Custom Parity Function

```python
def main():
	x = int(input("What's x? "))
	if is_even(x):
		print("Even")
	else:
		print("Odd")


def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False


if __name__ == "__main__":
	main()
```

## Pythonic

- pythonic is a unique way of coding only seen in Python

```python
def main():
	x = int(input("What's x? "))
	if is_even(x):
		print("Even")
	else:
		print("Odd")


def is_even(n):
	return True if n % 2 == 0 else False


if __name__ == "__main__":
	main()
```

- the code above can be optimized as follows:

```python
def main():
	x = int(input("What's x? "))
	if is_even(x):
		print("Even")
	else:
		print("Odd")


def is_even(n):
	return n % 2 == 0


if __name__ == "__main__":
	main()
```

## match

- mechanism similar to `switch` from other programming languages

```python
name = input("What's your name? ")

match name: 
	case "Harry" | "Hermione" | "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
```

- in the code above:
	- `|` stands for "or"
	- `_` stands for "else", the default value
