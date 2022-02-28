from Clases.Persona import Persona

class Alumno(Persona):

    def __init__(self, nombre, edad, sexo, matricula, carrera, semestre):
        super().__init__(nombre, edad, sexo)
        self.Matricula = matricula
        self.Carrera = carrera
        self.Semestre = semestre

    def mostrarDatos(self):
        self.mostrarDatosBasico()
        print("Matricula: ", self.Matricula)
        print("Carrera: ", self.Carrera)
        print("Semestre: ", self.Semestre)

