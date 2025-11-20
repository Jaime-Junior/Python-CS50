#need students.csv
import csv

name = input("What's your name? ")
house = input("Which is your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})