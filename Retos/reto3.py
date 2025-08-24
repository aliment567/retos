from reto2 import Dog

class Cat:
    def __init__(self):
        self.name = input("¿Cómo se llama el gato? ")
        self.age = input("¿Cuántos años tiene el gato? ")
        self.species = input("¿Cuál es la especie del gato? ")

    def primer_animal(self):
        print(f"El gato se llama {self.name}, tiene {self.age} años y es de la especie {self.species}")


class Bird:
    def __init__(self):
        self.name = input("¿Cómo se llama el pájaro? ")
        self.age = input("¿Cuántos años tiene el pájaro? ")
        self.species = input("¿Cuál es la especie del pájaro? ")

    def segundo_animal(self):
        print(f"El pájaro se llama {self.name}, tiene {self.age} años y es de la especie {self.species}")



class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        print("\nAnimales en el zoológico:")
        for animal in self.animals:
            print(f"- {animal.__class__.__name__}: {animal.name}")
if __name__ == "__main__":
 zoo = Zoo()

 perro = Dog()
 perro.fetch()
 
 gato = Cat()
 gato.primer_animal()
 pajaro = Bird()
 pajaro.segundo_animal() 

 zoo.add_animal(perro)
 zoo.add_animal(gato)
 zoo.add_animal(pajaro)

 zoo.show_animals()
    