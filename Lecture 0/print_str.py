#First program
print("hello world.")

#Ask a user for their name
#Remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"Hello, {first}.")