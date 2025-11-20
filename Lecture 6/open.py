#Execute multiple times to increment names.txt
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()