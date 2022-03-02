class Felidae:

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):

        self.Nombre = nombre
        self.Hábitat = hábitatN
        self.Padre = padre
        self.Madre = madre
        self.Alimentación = alimentación
        self.Peso = peso
        self.Altura = altura
        self.Recinto = recinto
        self.Velocidad = velocidadP

    @property
    def peso(self):
        return self.Peso

    @peso.setter
    def peso(self,p):
        self.Peso = p

    @property
    def altura(self):
        return self.Altura

    @altura.setter
    def altura(self,a):
         self.Altura = a

    @property
    def velocidad(self):
        return self.Velocidad

    @velocidad.setter
    def velocidad(self,v):
        self.Velocidad = v



    def alimentar(self):
        return "El animal ha sido alimentado\n\t"

    def sedar(self):
        return "Se ha aplicado la inyección para sedar al animal\n\t"

    def transladar(self):
        return "Se ha transladado el animal a otro zoológico\n\t"

    def revisiónMP(self):
        return "Hay una revisión médica pendiente\n\t"

    def revisiónMC(self):
        return "No hay revisiones médicas pendientes\n\t"

class perro(Felidae):

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):
        super(). __init__(nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP)

    def mostrarDatosPerro(self):
        print("---------------------------------------------")
        print("Nombre del perro: ", self.Nombre)
        print("Hábitat Natural del animal: ", self.Hábitat)
        print("Padre del animal:  ", self.Padre)
        print("Madre del animal: ", self.Madre)
        print("Alimentado: ", self.Alimentación)
        print("Peso del animal (kg): ", self.Peso)
        print("Altura del animal (cm):  ", self.Altura)
        print("Recinto del zoologico: ",self.Recinto)
        print("Velocidad promedio del animal:  ", self.Velocidad)


class oso(Felidae):

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):
        super(). __init__(nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP)

    def mostrarDatosOso(self):
        print("---------------------------------------------")
        print("Nombre del Oso: ", self.Nombre)
        print("Hábitat Natural del animal: ", self.Hábitat)
        print("Padre del animal:  ", self.Padre)
        print("Madre del animal: ", self.Madre)
        print("Alimentado: ", self.Alimentación)
        print("Peso del animal (kg): ", self.Peso)
        print("Altura del animal (cm):  ", self.Altura)
        print("Recinto del zoologico: ",self.Recinto)
        print("Velocidad promedio del animal:  ", self.Velocidad)


class león(Felidae):

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):
        super(). __init__(nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP)

    def mostrarDatosLeón(self):
        print("---------------------------------------------")
        print("Nombre del León: ", self.Nombre)
        print("Hábitat Natural del animal: ", self.Hábitat)
        print("Padre del animal:  ", self.Padre)
        print("Madre del animal: ", self.Madre)
        print("Alimentado: ", self.Alimentación)
        print("Peso del animal (kg): ", self.Peso)
        print("Altura del animal (cm):  ", self.Altura)
        print("Recinto del zoologico: ",self.Recinto)
        print("Velocidad promedio del animal:  ", self.Velocidad)


class tortuga(Felidae):

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):
        super(). __init__(nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP)

    def mostrarDatosTortuga(self):
        print("---------------------------------------------")
        print("Nombre de la Tortuga: ", self.Nombre)
        print("Hábitat Natural del animal: ", self.Hábitat)
        print("Padre del animal:  ", self.Padre)
        print("Madre del animal: ", self.Madre)
        print("Alimentado: ", self.Alimentación)
        print("Peso del animal (kg): ", self.Peso)
        print("Altura del animal (cm):  ", self.Altura)
        print("Recinto del zoologico: ",self.Recinto)
        print("Velocidad promedio del animal:  ", self.Velocidad)


class cebra(Felidae):

    def __init__(self,nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP):
        super(). __init__(nombre, hábitatN, padre, madre, alimentación, peso, altura, recinto, velocidadP)


    def mostrarDatosCebra(self):
        print("---------------------------------------------")
        print("Nombre de la Cebra: ", self.Nombre)
        print("Hábitat Natural del animal: ", self.Hábitat)
        print("Padre del animal:  ", self.Padre)
        print("Madre del animal: ", self.Madre)
        print("Alimentado: ", self.Alimentación)
        print("Peso del animal (kg): ", self.Peso)
        print("Altura del animal (cm):  ", self.Altura)
        print("Recinto del zoologico: ",self.Recinto)
        print("Velocidad promedio del animal:  ", self.Velocidad)