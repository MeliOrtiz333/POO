import random

class Cuenta:

    tasa = 0.04



    def __init__(self):
        self.__Numero = self.generarNumero()
        self.__Monto = 0.0
        self.__Deuda = 0.0


    @property
    def monto(self):
        return self.__Monto

    @monto.setter
    def monto(self,m):
        if m.isdigit():
            self.__Monto += m

    @property
    def deuda(self):
        return self.__Deuda

    @deuda.setter
    def deuda(self, d):
        self.__Deuda = d

    def generarNumero(self):
        num = " "
        for i in range(8):
            c = random.randint(0,9)
            num += chr(c)
        return num


    def Depositar(self):

        depósito = int(input("Ingrese la cantidad que desea depositar: \n\t"))
        self.__Monto += depósito

        while (depósito < 0):
            print("El monto ingresado es negativo intente de nuevo")

            depósito = int(input("Ingrese la cantidad que desea depositar: \n\t"))



    def resumen(self):
        print("\tNumero de cuenta: ", self.__Numero)
        print("\tBalance: ", self.__Monto)
        print("\tDeuda: ", self.__Deuda)
        print("\tTasa: ", self.tasa*100, "%")



    def depositar(self, m = 0):
        if m == 0:
           m = input("Ingrese el monto a depositar:  ")
           if m.isdigit() and m != "":
              if float(m) > 0:
                self.__Monto += float(m)
                return
           print("El monto ingresado es incorrecto")
        else:
           self.__Monto += m



    def retirar(self, m= " "):
        if m == " ":
            m = input("Ingrese la cantidad a retirar: ")
            if m.isdigit() and m != "":
                if float(m) > 0 and float(m) < self.__Monto:
                    self.__Monto -= float(m)
                    return
                print("El monto ingresado es incorrecto")

        else:
            self.__Monto -= m



