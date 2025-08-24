class Bird:
    def __init__(self):
        self.name = input("¿Cómo se llama el pájaro? ")
        self.age = input("¿Cuántos años tiene el pájaro? ")
        self.species = input("¿Cuál es la especie del pájaro? ")

    def segundo_animal(self):
        print(f"El pájaro se llama {self.name}, tiene {self.age} años y es de la especie {self.species}")

    def migrate(self):
        destino = input(f"¿A dónde está migrando {self.name}? ")
        print(f"{self.name} está migrando a {destino}.")

pajaro = Bird()
pajaro.segundo_animal()
pajaro.migrate()
