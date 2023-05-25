class Bebidas():
    def __init__(self, marca, sabor, size, precio):
        self.__marca = marca
        self.__sabor = sabor
        self.__size = size
        self.__precio = precio

    def info(self):
        print(
            f"Bebida {self.__marca} de sabor {self.__sabor} y su precio es de {self.__precio} .")

    def marcas(self):
        print(
            f"Es {self.__marca}.")

    def precios(self):
        print(
            f"Su precio es de {self.__precio}.")

    def tamano(self):
        print(
            f"Su tamano es de {self.__size}.\n")

    def obt_marca(self):
        return self.__marca

    def obt_precio(self):
        return self.__precio

    def obt_sabor(self):
        return self.__sabor

    def obt_size(self):
        return self.__size


bebida1 = Bebidas("Coca Cola", "Normal", "1 litro", 7000)

bebida1.info()
bebida1.marcas()
bebida1.precios()
bebida1.tamano()


class BebidasA(Bebidas):
    def __init__(self, tipo, marca, sabor, size, precio, porcentaje):
        super().__init__(marca, sabor, size, precio)
        self.__porcentaje = porcentaje
        self.__tipo = tipo

    def info(self):
        print(
            f"Bebida {self.__tipo} de la marca {self.obt_marca()} con {self.__porcentaje} de alcohol y su precio es de {self.obt_precio()}.")

    def marcas(self):
        print(
            f"Es marca {self.obt_marca()}.")

    def precios(self):
        print(
            f"Su precio es de {self.obt_precio()}.")

    def tamano(self):
        print(
            f"Su tamano es de {self.obt_size()}.")

    def alcohol(self):
        print(
            f"Contiene un porcentaje de alcohol del {self.__porcentaje}.")


bebida1 = BebidasA("Wisky", "JackDaniel's", "", "1 Litro",
                   "50.000", "30%")

bebida1.info()
bebida1.marcas()
bebida1.precios()
bebida1.tamano()
bebida1.alcohol()
