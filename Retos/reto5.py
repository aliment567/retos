class Bird:
    def __init__(self):
        self.name = input("¿Cuál es el nombre del pájaro? ")
        self.age = input("¿Cuántos años tiene el pájaro? ")
        self.species = input("¿Cuál es la especie del pájaro? ")

    def show_info(self):
        print(f"El pájaro se llama {self.name}, tiene {self.age} años y es de la especie {self.species}")


class Parrot(Bird):  
    def __init__(self):
        super().__init__()
        self.phrase = input("¿Qué quieres que diga el loro? ")

    def talk(self):
        print(f"{self.name} dice: {self.phrase}")
        
loro = Parrot()
loro.show_info()
loro.talk()


