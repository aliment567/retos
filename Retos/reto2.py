class Dog:
    def __init__(self):
        self.name = input("¿Cómo se llama tu perro? ")
        self.item = input("¿Qué objeto quieres que traiga? ")

    def fetch(self):
        print(f"{self.name} corre y trae el/la {self.item}.")
if __name__ == "__main__":
 name = Dog()
 name.fetch()