# https://cs50.harvard.edu/python/2022/psets/4/emojize/
# Practice using emoji package

# Import emojize function from emoji package
from emoji import emojize

# Prompt user for an emoji alias (see https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias)
alias = input("Input: ")

# Print emoji
print(emojize(f"Output: {alias}"))
