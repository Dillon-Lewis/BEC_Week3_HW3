import re

#Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


# valid = re.search(r"[A-Z]\w+(\s)[A-Z](\s)[A-Z]\w+", names)

# valid = re.match(r"[A-Z]\w+(\s)[A-Z](\s)[A-Z]\w+", names)

def correct_format(names):
    for name in names:
        if re.match(r"[A-Z]\w+(\s)|[A-Z](\s)[A-Z]\w+", name):
            print(name)
        else:
            print("Invalid input")

correct_format(names)

