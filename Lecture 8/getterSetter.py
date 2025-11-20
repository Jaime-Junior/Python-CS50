class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"{self.name} is from {self.city}"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

def main():
    person = get_person()
    print(person)

def get_person():
    name = input("Enter your name: ")
    city = input("Enter your hometown: ")
    person = Person(name, city)
    return person

if __name__ == "__main__":
    main()