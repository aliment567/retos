from reto2 import Dog
from reto3 import Cat, Bird

class Owner:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} ahora tiene a {animal.name}.")

    def feed_animals(self):
        print(f"\n{self.name} está alimentando a sus animales:")
        for animal in self.animals:
            print(f"- {animal.name} está comiendo.")



if __name__ == "__main__":
    owner = Owner("Carlos")

    perro = Dog()
    perro.fetch()
    
    gato = Cat()
    gato.primer_animal()
    
    pajaro = Bird()
    pajaro.segundo_animal()

    owner.add_animal(perro)
    owner.add_animal(gato)
    owner.add_animal(pajaro)

    owner.feed_animals()
