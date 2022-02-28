from Clases.Persona import Persona

class Profesor(Persona):

    def __init__(self,nombre,edad,sexo,licenciatura,estudios,antiguedad):
        super().__init__(nombre,edad,sexo)
        self.Licenciatura = licenciatura
        self.Estudios = estudios
        self.Antiguedad = antiguedad


    def mostrarDatos(self):
        self.mostrarDatosBasico()
        print("Licenciatura: ", self.Licenciatura)
        print("Estudios: ", self.Estudios)
        print("Antiguedad: ", self.Antiguedad)