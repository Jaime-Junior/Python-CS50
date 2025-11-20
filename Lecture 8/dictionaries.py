def main():
    person = get_person()
    print(f"{person["name"]} is from {person["house"]}.")

def get_person():
    name = input("Enter your name: ")
    city = input("Enter your hometown: ")
    return {"name": name, "city": city}

if __name__ == "__main__":
    main()