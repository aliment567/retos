from reto2 import Dog
from reto3 import Cat, Bird
class Veterinarian:
    def checkup(self, animal):
        print(f"El veterinario está revisando a {animal.name}, que es un {animal.__class__.__name__}.")


if __name__ == "__main__":
    perro = Dog()
    gato = Cat()
    pajaro = Bird()
    
    
    perro = Dog()
    perro.fetch()
    
    gato = Cat()
    gato.primer_animal()
    
    pajaro = Bird()
    pajaro.segundo_animal()


    vet = Veterinarian()

    vet.checkup(perro)
    vet.checkup(gato)
    vet.checkup(pajaro)