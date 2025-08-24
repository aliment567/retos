class Dog:
    def __init__(self):
        self.name = input("¿Cómo se llama tu perro? ")
        self.age = int(input(f"¿Cuántos años tiene {self.name}? "))
        self.species = "Canino"

    def fetch(self):
        print(f"{self.name} está trayendo la pelota.")

    def compare_age(self, other_dog):
        if self.age > other_dog.age:
            print(f"{self.name} es mayor que {other_dog.name}.")
        elif self.age < other_dog.age:
            print(f"{other_dog.name} es mayor que {self.name}.")
        else:
            print(f"{self.name} y {other_dog.name} tienen la misma edad.")

if __name__ == "__main__":
    dog1 = Dog()
    dog2 = Dog()

    dog1.compare_age(dog2)