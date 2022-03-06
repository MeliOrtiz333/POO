import random

class Felidae():

    def __init__(self):
        self.ID= self.genCodigo()
        r = input("¿Quiere completar datos ahora? s/n")
        if r == "s":
            self.completarDatos()


    def genCodigo(self):
        id = " "
        for i in range(8):
            id = id+str(random.randit(0,9))
            return id

    def completarDatos(self):
        self.nombre = input("Nombre del felino: ")
        self.sexo = input("Sexo (H/M:")
        self.revisionMedica()

     def mostrarDatos(self):
         print("---------------------------")


class Leopardo(Felidae):

    def __init__(self):
        super().__init__()

    def revisionMedica(ejemplar):
        ejemplar.peso = random.randit(36,88)
        ejemplar.altura =random.randit(75,90)




class Puma(Felidae):

    def __init__(self):
        super().__init__()

    def revisionMedica(ejemplar):
        ejemplar.peso = random.randit(25,50)




class Gato(Felidae):

    def __init__(self):
        super().__init__()

    def revisionMedica(ejemplar):
        ejemplar.peso = random.randit(2, 8)



class Tigre(Felidae):
    def __init__(self):
        super().__init__()

    def revisionMedica(ejemplar):
        ejemplar.peso = random.randit(2, 8)




class León(Felidae):

    def __init__(self):
        super().__init__()

    def revisionMedica(ejemplar):
        ejemplar.peso = random.randit(2, 8)

