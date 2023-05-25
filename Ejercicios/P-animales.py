class Animales():
    def __init__(self, clase, edad, genero, size):
        self.__clase = clase
        self.__edad = edad
        self.__genero = genero
        self.__size = size

    def info_general(self):
        print(
            f"INFORMACION:\nEs del grupo taxonomico {self.__clase} tiene {self.__edad} years, su etapa es {self.__size} y es {self.__genero}. ")

    def info_caract(self):
        if self.__clase == "Mamifero":
            print(
                f"\n|-Clase-|\nEl animal corresponde a la clase {self.__clase}, sus caracteristicas \nson: \n   - Pelo - Homeotermia - Viviparidad\n")
        elif self.__clase == "Reptil":
            print(
                f"|-Clase-|\nEl animal corresponde a la clase {self.__clase}, sus caracteristicas \nson: \n   - Escamas - Ectotermia - Colmillos\n")
        elif self.__clase == "Actinopteygii":
            print(
                f"|-Clase-|\nEl animal corresponde a la clase {self.__clase}, sus caracteristicas \nson: \n   - Escamas - Aletas - Branquias \n")
        else:
            print("La especie no esta en la base de datos.")

    def info_fisica(self):
        print(
            f"|-Edad-|\nEl animal tiene {self.__edad} years, su tamano es {self.__size}")

    def info_gen(self):
        print(f"\n|-Genero-|\nEl genero del animal es: {self.__genero}")

    def obt_clase(self):
        return self.__clase

    def obt_edad(self):
        return self.__edad

    def obt_genero(self):
        return self.__genero

    def obt_size(self):
        return self.__size


Koi = Animales("Actinopteygii", "2", "Macho", "Joven")
Cobra = Animales("Reptil", "4", "Hembra", "Joven")
Leon = Animales("Mamifero", "6", "Macho", "Adulto")

Koi.info_general()
Koi.info_caract()
Koi.info_fisica()
Koi.info_gen()

Cobra.info_general()
Cobra.info_caract()
Cobra.info_fisica()
Cobra.info_gen()

Leon.info_general()
Leon.info_caract()
Leon.info_fisica()
Leon.info_gen()


class Granja(Animales):
    def __init__(self, clase, edad, genero, size, zona):
        super().__init__(clase, edad, genero, size)
        self.zona = zona

    def info_general(self):
        print(
            f"INFORMACION:\nEs un {self.obt_clase()} tiene {self.obt_edad()} years, su tamano es {self.obt_size()}, es {self.obt_genero()} y esta en la zona del {self.zona}")

    def info_caract(self):
        print(
            f"\n|-Clase-|\nEl animal corresponde a la especie {self.obt_clase()}. \nSus caracteristicas son:\n- Escamas - Aletas - Branquias ")

    def info_fisica(self):
        print(
            f"\n|-Edad-|\nEl animal tiene {self.obt_edad()} years, su tamano es {self.obt_size()}")

    def info_gen(self):
        print(f"\n|-Genero-|\nEl genero del animal es: {self.obt_genero()}")

    def info_lugar(self):
        if self.zona == "Campo":
            print(
                f"\n|-Zona-|\nEl animal esta en la zona del {self.zona}\n ")
        elif self.zona == "Corral":
            print(
                f"\n|-Zona-|\nEl animal esta en la zona del {self.zona}\n ")
        elif self.zona == "Estanque":
            print(
                f"\n|-Zona-|\nEl animal esta en la zona del {self.zona}\n ")
        else:
            print("La zona no esta en la base de datos.")


Vaca = Granja("Bovino", "6", "Macho", "Adulto", "Campo")
Gallo = Granja("Ave", "2", "Macho", "Adulto", "Corral")
Mojarra = Granja("Pez", "4", "Hembra", "Adulto", "Estanque")

Vaca.info_general()
Vaca.info_caract()
Vaca.info_fisica()
Vaca.info_gen()
Vaca.info_lugar()

Gallo.info_general()
Gallo.info_caract()
Gallo.info_fisica()
Gallo.info_gen()
Gallo.info_lugar()


Mojarra.info_general()
Mojarra.info_caract()
Mojarra.info_fisica()
Mojarra.info_gen()
Mojarra.info_lugar()
