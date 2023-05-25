
class Animal:
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")


class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu!")


# Creamos una lista de animales
animales = [Perro(), Gato(), Vaca()]

# Llamamos al método hacer_sonido() de cada animal
for animal in animales:
    animal.hacer_sonido()
