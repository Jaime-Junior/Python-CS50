#re stands for Regular Expressions
#Validates if inputted email has word username, has @ and ends in .com
import re

email = input("What's your email? ").strip()

#ignore case from email
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")