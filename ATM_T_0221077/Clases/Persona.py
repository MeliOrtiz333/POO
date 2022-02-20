from Clases.Cuenta import Cuenta

class Persona:
    def __init__(self,nombre,edad):
        if self.validarNombre(nombre) and self.validarEdad(edad):
            self.__Nombre = nombre
            self.__Edad = edad
            self.cuenta = Cuenta()
        else:
            raise Exception()


    def validarNombre(self,n):
        if len(n) <= 3:
            print("El nombre es muy corto")
            return False
        else:
            return True

    def validarEdad(self,e):
        if e.isdigit():
            if self.esMayor(e):
                return True
        print("La edad no es un dígito válido")
        return False

    def esMayor(self,e=0):
        if e.isdigit():
            return int(e) > 18
        else:
            return self.__Edad > 18

    def resumen(self):
        print("***********************************")
        print("Resumen de la persona")
        print("Titular", self.__Nombre)
        print("\n\tResumen de la Cuenta:\n\t ")
        self.cuenta.resumen()
        print("***********************************")


