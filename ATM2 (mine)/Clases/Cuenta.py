import random
class Cuenta:

    def __init__(self):
        self.__Numero = self.generarNumero()
        self.__Monto = 0.0
        self.__Depositar = self.Depositar()
        self.__Retiro = self.Retirar()


    @property
    def monto(self,m):
        if m.isdigit():
            self.__Monto += m

    @monto.setter
    def monto(self,m):
        if m.isdigit():
            self.__Monto += m

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






    def Retirar(self):

        retiro = int(input("Ingrese la cantidad que desea retirar: \n\t"))
        self.__Monto -= retiro


        while (retiro > int(self.__Monto)):
            print("No es posible retirar esa cantidad, ya que no existe, intente otra vez")

            retiro = int(input("Ingrese la cantidad que desea retirar: \n\t"))

    def SolicitarPres(self):
        prestamo = int(input("Digite la cantidad que desea solicitar a prestamo"))
        self.__Monto += prestamo

    def Deuda(self):
        Deuda = self.__Monto + 0.4 * 100
        print("Su deuda con intereses es:  ",Deuda)
        calcularNR = Deuda + 0.4 * 100



    def resumen(self):
        print("Numero de cuenta: ", self.__Numero)
        print("Balance: ", self.__Monto)
        print("El monto ingresado es: ", self.__Depositar)
        print("El monto retirado es: ", self.__Retiro)
