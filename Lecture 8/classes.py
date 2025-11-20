class Person:
    def __init__(self, name, city):
        if not name:
            raise ValueError("Missing name")
        if not city:
            raise ValueError("Missing hometown")
        self.name = name
        self.city = city

def main():
    person = get_person()
    print(f"{person.name} is from {person.city}")

def get_person():
    name = input("Enter your name: ")
    city = input("Enter your hometown: ")
    person = Person(name, city)
    return person

if __name__ == "__main__":
    main()