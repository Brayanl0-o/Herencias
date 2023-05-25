class Padre:
    def __init__(self, nombre, ocupacion, edad):
        self.nombre = nombre
        self.ocupacion = ocupacion
        self.edad = edad

    def info(self):
        print("Nombre: " + self.nombre + "\nOcupacion: " +
              self.ocupacion+"\nEdad: "+self.edad)

    def name(self):
        print(f"El nombre del padre es {self.nombre}.")

    def trabajo(self):
        print(f"La ocupacion del padre es {self.ocupacion}.")

    def years(self):
        print(f"La edad del padre es {self.edad}.")


padre1 = Padre("Char", "Jefe seguridad", "30")


# padre1.info()
padre1.name()
padre1.trabajo()
padre1.years()


class Hijo(Padre):
    def __init__(self, nombre, ocupacion, edad, grado):
        super().__init__(nombre, ocupacion, edad)
        self.grado = grado
        self.edad = edad

    def info(self):
        print(
            f"Es {self.ocupacion} del Curso: {self.grado} \nSu nombre es: {self.nombre} y tiene {self.edad} years")

    def name(self):
        print(f"El nombre es {self.nombre}.")

    def ocu(self):
        print(f"Es {self.ocupacion}")

    def years(self):
        print(f"La edad es {self.edad}")

    def curso(self):
        print(f"Del curso {self.grado}")


estudiante1 = Hijo("Joel", "estudiante", 15, "Octavo B")

# estudiante1.info()
estudiante1.name()
estudiante1.ocu()
estudiante1.years()
estudiante1.curso()
