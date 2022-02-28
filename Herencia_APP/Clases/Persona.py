class Persona:

    def __init__(self, nombre,edad, sexo):
        self.Nombre = nombre
        self.__Edad = edad
        self.Sexo = sexo

    @property
    def edad(self):
        return self.__Edad

    @edad.setter
    def edad(self,e):
        self.__Edad = e


    def mostrarDatosBasico(self):
        print("Nombre: ", self.Nombre)
        print("Edad: ", self.edad)
        print("Sexo: ", self.Sexo)