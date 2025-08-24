class Bird:
    def __init__(self):
        self.name = input("Nombre del pájaro: ")
        self.age = input("Edad del pájaro: ")
        self.species = input("Especie del pájaro: ")

    def show_info(self):
        print(f"El nombre del pájaro es {self.name}, tiene {self.age} años y es de la especie {self.species}")



class Eagle(Bird):
    def __init__(self):
        super().__init__()  
        self.altitude = int(input("¿A qué altitud está volando el águila? (en metros): "))

    def show_altitude(self):
        print(f"El águila {self.name} está volando a {self.altitude} metros de altura.")



eagle = Eagle()
eagle.show_info()
eagle.show_altitude()

