#Code from class Person become usable on classes Name and Professional

class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    def __str__(self):
        return f"{self.name} é um nome muito comum no Brasil."
        
class Name(Person):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city
    
    def __str__(self):
        return f"O {self.name} mora na cidade de {self.city}"

class Professional(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def __str__(self):
        return f"O {self.name} trabalha como {self.position}"

person = Person("Maria")
name = Name("Jaime", "Guarulhos")
professional = Professional("Rodolfo", "Gerente")

print(person)
print(name)
print(professional)
