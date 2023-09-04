# Week 5 Unit Tests

Sources: [Lecture 5](https://cs50.harvard.edu/python/2022/notes/5/)

## Unit Tests

- *unit tests* are segments of code written to test other pieces of code, typically a single function or method

```python
# calculator.py (with intentional error in square function)

def main():
	x = int(input("What's x? "))
	print("x squared is", square(x))


def square(n):
	return n + n


if __name__ == "__main__":
	main()
```

```python
# test_calculator.py

from calculator import square


def main():
	test_square()


def test_square():
	if square(2) != 4:
		print("2 squared was not 4")
	if square(3) != 9:
		print("3 squared was not 9")


if __name__ == "__main__":
	main()
```

## assert

- `assert` tells interpreter that some assertion is true; if it is not, it returns `AssertException` error
- for more information, see [Python Documentation: assert](https://docs.python.org/3/reference/simple_stmts.html#assert)

```python
# test_calculator.py

from calculator import square


def main():
	test_square()


def test_square():
	try:
		assert square(2) == 4
	except AssertionError:
		print("2 squared is not 4")
	try:
		assert square(3) == 9
	except AssertionError:
		print("3 squared is not 9")
	try:
		assert square(-2) == 4
	except AssertionError:
		print("-2 squared is not 4")
	try:
		assert square(-3) == 9
	except AssertionError:
		print("-3 squared is not 9")
	try:
		assert square(0) == 0
	except AssertionError:
		print("0 squared is not 0")


if __name__ == "__main__":
	main()
```

## pytest

- `pytest` is a third-party library simplifying unit testing
- it is installed via terminal command `pip install pytest` 
- for more information, see [pytest Documentation](https://docs.pytest.org/)

```python
# test_calculator.py
# run as "pytest test_calculator.py"

from calculator import square


def test_square():
	assert square(2) == 4
	assert square(3) == 9
	assert square(-2) == 4
	assert square(-3) == 9
	assert square(0) == 0
```

- in the code above, `test_square()` function is terminated on first error occurrence, in this case on row `assert square(3 == 9`; therefore, it does not test for other corner cases, such as `-2` nebo `0`
- this can be fixed by dividing `test_square()` into several test functions as follows:

```python
# test_calculator.py
# run as "pytest test_calculator.py"

import pytest
from calculator import square


def test_positive():
	assert square(2) == 4
	assert square(3) == 9


def test_negative():
	assert square(-2) == 4
	assert square(-3) == 9


def test_zero():
	assert square(0) == 0


def test_str():
	with pytest.raises(TypeError):
		square("cat")
```

- in the code above, tests were complemented by `test_str()` function, which raises `TypeError` if `cat` string value is passed on `square()` function; this requires `import pytest`

## Testing Strings

```python
# hello.py

def main():
	name = input("What's your name? ")
	hello(name)


def hello(to="world"):
	print("Hello,", to)


if __name__ == "__main__":
	main()
```

```python
# test_hello.py
# run as "pytest test_hello.py"

from hello import hello


def test_hello():
	assert hello("David") == "Hello, David"
	assert hello() == "Hello, world"
```

- in the code above, testing will not work well since `hello()` function does not **return any value**
- this can be fixed by modifying `hello()` function in `hello.py` as follows:

```python
# hello.py

def main():
	name = input("What's your name? ")
	print(hello(name))


def hello(to="world"):
	return f"Hello, {to}"


if __name__ == "__main__":
	main()
```

- as in the previous case, it is recommended to have several test functions, as follows:

```python
# test_hello.py
# run as "pytest test_hello.py"

from hello import hello


def test_default():
	assert hello() == "Hello, world"


def test_argument():
	assert hello("David") == "Hello, David"
```

## Organizing Tests into Folders

- with `pytest` it is possible to run a whole directory containing multiple test files (e.g. `test/` directory with `test_hello.py` and other test files)
- to make it work, such directory must contain special (empty) `__init__.py` file, that tells Python to treat directory as a package
- it is then run via terminal command `pytest test`
- for more information, see [pytest Documentation: Import Mechanisms](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html?highlight=folder#pytest-import-mechanisms-and-sys-path-pythonpath)
