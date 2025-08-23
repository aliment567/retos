class Dog:
    name = input("¿Cómo se llama tu perro? ")  
    item = input("¿Qué objeto quieres que traiga? ")
    def fetch(self):
        print(f"{self.name} corre y trae el/la {self.item}.")
name = Dog()
name.fetch()


