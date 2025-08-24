class Cat:
    def __init__(self):
        self.name = input("Cual es el nombre del gato? ")
        self.age = input("Cuantos años tiene el gato? ")
        self.species = input("Cual es la especie del gato? ")

    def info(self):
        print(f"El gato {self.name} tiene {self.age} años y es de la especie {self.species}")

    def sleep(self):
        print(f"El gato {self.name} está durmiendo")
        


gato = Cat()
gato.info()
gato.sleep()

    