class fish:
    name = input("Cual es el nombre del pez? ")
    age = input("Cuantos años tiene el pez? ")
    species = input("Cual es la especie del pez? ")
    swim = 'el esta nadando en su pecera '

    def Nadaremos(sel):
        print(f"El nombre del pez es {sel.name}, tiene {sel.age} años y es de la especie {sel.species} {sel.swim}")

pez = fish()
pez.Nadaremos()