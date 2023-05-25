class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.acabadellegar = False
        self.meconocen = False

    def start_saludar(self):
        self.acabadellegar = True
        print("Hola! Buenos dias!")

    def no_saludar(self):
        self.acabadellegar = False
        print("Ya salude!")

    def start_presentarse(self):
        self.meconocen = False
        print(
            f"Mi nombre es {self.nombre}, mi edad es  {self.edad} y soy {self.profesion}")


persona1 = Persona("Brayan", "18", "Estudiante")
print(persona1.nombre, persona1.edad, persona1.profesion)


persona1.no_saludar()
persona1.start_presentarse()
