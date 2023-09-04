# https://cs50.harvard.edu/python/2022/psets/4/figlet/
# Practice using pyfiglet package and black code formatter

import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
supported_option = ["-f", "--font"]
supported_font = figlet.getFonts()

# No arguments - set random font
if len(sys.argv) == 1:
    figlet.setFont(font=choice(supported_font))

# Two arguments - set font based on second argument
elif (
    len(sys.argv) == 3
    and sys.argv[1] in supported_option
    and sys.argv[2] in supported_font
):
    figlet.setFont(font=sys.argv[2])

# Otherwise, exit with a warning
else:
    sys.exit("Invalid usage")

# Prompt user for an input and print it in set font
text = input("Input: ")
print(figlet.renderText(text))
