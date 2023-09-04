# Week 4 Libraries

Sources: [Lecture 4](https://cs50.harvard.edu/python/2022/notes/4/) | [Style](https://cdn.cs50.net/python/2022/x/shorts/style/style.pdf)

## Libraries

- *library* is a collection of packages and modules providing wide functionality

## Modules

- *script* is a `.py` file intended to be run directly
- *module* is a `.py` file intended to be imported into scripts or other modules, and often defines members like classes, functions, and variables intended to be used in other files that import it

## random

- see [Python Documentation: random](https://docs.python.org/3/library/random.html)

### random.choice(seq)

- returns random value from a `seq` list

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

- in the code above:
	- `import random` imports entire content of `random` module
	- module name `random` must be prepended when using `choice(seq)` function

```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

- in the code above:
	- `from random import choice` imports only `choice()` function from `random` module
	- module name `random` can be ommited when using `choice(seq)` function

### random.randint(a, b)

- returns random number between `a` and `b`

```python
import random

number = random.randint(1, 10)
print(number)
```

### random.shuffle(x)

- shuffles `x` list items

```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
	print(card)
```

## statistics

- see [Python Documentation: statistics](https://docs.python.org/3/library/statistics.html)

### statistics.mean(data)

- returns the average of given values

```python
import statistics

print(statistics.mean([100, 90]))
```

## sys

- see [Python Documentation: sys](https://docs.python.org/3/library/sys.html)

### sys.agrv

- allows to read command line arguments

```python
# hello.py

import sys

try:
	print("Hello, ", sys.argv[1])
except IndexError:
    print("Too few arguments")
```

- in the code above:
	- running as `python hello.py David` returns `Hello, David`    
	- `sys.argv[0]` holds name of the program, `sys.argv[1]` holds value of the first parameter
	- `except IndexError` catches `list index out of range` error, which is raised when called parameter is not defined
- arguments in brackets are considered as one, e.g. when running `python hello.py "David Malan"`, `sys.argv[1]` returns `David Malan`

### sys.exit([arg])

- exits a program

```python
# hello.py

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, ", sys.argv[1])
```

## slice

- `slice [:]` is a command that allows to define the start and the end of the `list`, e.g.:
	- `list[1:]` starts with index 1, ends with last index
	- `list[:2]` starts with index 0, ends with index 2
	- `list[:-1]` starts with index 0, ends with penultimate index

```python
# hello.py

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, ", arg)
``` 

## Packages

- *package* is a directory/collection of related modules that work together to provide certain functionality
- in addition to modules, this directory also contains special `__init__.py` file that tells Python to treat directory as a package
- [PyPI](https://pypi.org/) is a repository of all available third-party packages currently available
- `pip` is a package installer for Python

## cowsay

- *cowsay* is a popular for-fun package that allows a cow to talk to the user
- it is installed via terminal command `pip install cowsay`
- for more information, see [PyPI: cowsay](https://pypi.org/project/cowsay/)

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
```

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
```

## requests

- *requests* is a package that allows a program to behave as a web browser would
- it is installed via terminal command `pip install requests`
- for more information, see [Library Documentation: requests](https://docs.python-requests.org/)
- **API** (Application Program Interfaces) allows connecting to the code of others
- e.g. URL [https://itunes.apple.com/search?entity=song&limit=1&term=weezer](https://itunes.apple.com/search?entity=song&limit=1&term=weezer):
	- is constructed according to the Apple's API documentation 
	- is looking for a `song`, with a `limit` of one result, that relates to a `term` caller `weezer`
	- upon opening downloads a **JSON** file (JavaScript Object Notation, text-based format that is used to exchange text-based data between applications)

```python
# itunes.py

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
```

- in the code above:
	- `if len(sys.argv) != 2` checks for whether two command line arguments were given, such as `python itunes.py weezer`
	- `requests.get` returns JSON file and saves it into `response` variable
	- `print(response.json())` displays JSON file as a Python dictionary

## json

- *json* is a package that helps with interpreting JSON files
- for more information, see [Python Documentation: JSON](https://docs.python.org/3/library/json.html)

```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
```

- in the code above:
	- `json.dumps` is implemented such that it utilizes `indent` parameter to make the output more readable
	- the output is a `results` dictionary with several keys, such as `trackName`

```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
```

- in the code above:
	- limit number of results is increased to 50
	- `response.json()` is stored into `o` variable
	- `for result in o["results"]` iterates over all `results` in `o` variable
	- `print(result["trackName"])` prints values of `trackName` keys

## Custom Libraries

- custom module can be created as a `.py` file, such as:

```python
# sayings.py

def main():
	hello("world")
	goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":
	main()
```

- in the code above
	- `__name__` is a special variable with a value automatically set by Python
	- `if __name__ == "__main__"` ensures that `main()` function is called only when the program is run explicitly via `python sayings.py` and **not when the program is imported into another**
- this module can be then imported into other `.py` files as follows:

```python
# say.py

import sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
```

## Style

### PEP 8

- [PEP 8](https://peps.python.org/pep-0008/) (Python Enhancement Proposal) is a style guide for Python code

### pylint

- [pylint](https://docs.pylint.org) is a program (linter) that analyzes code for potencional errors
- it is installed via terminal command `pip install pylint`

### pycodestyle

- [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) is a code formatter
- it is installed via terminal command `pip install pycodestyle`

### black

- [black](https://black.readthedocs.io/en/stable/) is a code formatter
- it is installed via terminal command `pip install black`
