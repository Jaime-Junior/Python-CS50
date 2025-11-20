def main():
    person = get_person()
    print(f"{person[0]} is from {person[1]}.")

def get_person():
    name = input("Enter your name: ")
    city = input("Enter your hometown: ")
    return [name, city]

if __name__ == "__main__":
    main()