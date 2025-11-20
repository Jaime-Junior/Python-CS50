#Enter last name + first name, program will split and return name + last name
#:= assign the value into a variable and ask a boolean question
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")